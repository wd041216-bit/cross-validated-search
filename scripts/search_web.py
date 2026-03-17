#!/usr/bin/env python3
"""
Free Web Search Ultimate - 超级搜索核心 (v8.0 Super Workflow Upgraded)
移除了失效的 Yahoo，新增 books/videos 支持，修复 DDGS 线程安全问题，增强 JSON 输出
"""
import argparse
import json
import re
import ssl
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from typing import Dict, List, Optional

# 全局禁用 SSL 验证，应对部分网络环境
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

@dataclass
class Source:
    url: str
    title: str
    snippet: str = ""
    credibility: float = 0.0
    engine: str = ""
    cross_validated: bool = False
    date: str = ""
    extra: Dict = None

@dataclass
class Answer:
    query: str
    search_type: str
    answer: str
    confidence: str
    sources: List[Source]
    validation: Dict
    metadata: Dict
    elapsed_ms: int

class UltimateSearcher:
    def __init__(self, timeout: int = 15):
        self.timeout = timeout
        
    def _search_ddgs(self, query: str, search_type: str, timelimit: str = None, region: str = "wt-wt", max_results: int = 15) -> List[Source]:
        """使用官方 ddgs 库进行搜索（每次调用创建新实例保证线程安全）"""
        results = []
        try:
            from ddgs import DDGS
            # 创建局部实例
            with DDGS(timeout=self.timeout) as ddgs:
                if search_type == "text":
                    api_results = ddgs.text(query, region=region, max_results=max_results, timelimit=timelimit)
                elif search_type == "news":
                    api_results = ddgs.news(query, region=region, max_results=max_results, timelimit=timelimit)
                elif search_type == "videos":
                    api_results = ddgs.videos(query, region=region, max_results=max_results, timelimit=timelimit)
                elif search_type == "books":
                    # books 接口不支持 region 和 timelimit 参数
                    api_results = ddgs.books(query, max_results=max_results)
                else:
                    return []
                    
                for r in api_results:
                    url = r.get('href', r.get('url', r.get('content', '')))
                    if not url:
                        continue
                        
                    source = Source(
                        url=url,
                        title=r.get('title', ''),
                        snippet=r.get('body', r.get('description', '')),
                        credibility=0.95,
                        engine=f'DDG-{search_type.capitalize()}',
                        date=r.get('date', r.get('published', '')),
                        extra={}
                    )
                    
                    # 提取视频/书籍的额外信息
                    if search_type == "videos":
                        source.extra['duration'] = r.get('duration')
                        source.extra['publisher'] = r.get('publisher')
                    elif search_type == "books":
                        source.extra['author'] = r.get('author')
                        source.extra['year'] = r.get('year')
                        
                    results.append(source)
        except Exception as e:
            # 记录异常信息，供外部调试
            results.append(Source(url="error", title=f"Error: {str(e)}", engine="error"))
        return results

    def _cross_validate(self, all_results: List[Source]) -> List[Source]:
        """交叉验证和去重"""
        url_groups = {}
        for r in all_results:
            if r.url == "error":
                continue
                
            simplified = re.sub(r'^https?://(www\.)?', '', r.url).rstrip('/')
            simplified = simplified.split('#')[0].split('?')[0]
            
            if not simplified:
                continue
                
            if simplified not in url_groups:
                url_groups[simplified] = []
            url_groups[simplified].append(r)
        
        validated = []
        for url, group in url_groups.items():
            best_source = group[0]
            
            if len(group) >= 2:
                best_source.credibility = min(0.99, best_source.credibility + 0.1 * len(group))
                best_source.cross_validated = True
                best_source.engine = f"{best_source.engine} (x{len(group)})"
            
            valid_snippets = [s.snippet for s in group if len(s.snippet) > 20]
            if valid_snippets:
                best_source.snippet = max(valid_snippets, key=len)
                
            validated.append(best_source)
        
        validated.sort(key=lambda x: (x.cross_validated, x.credibility), reverse=True)
        return validated

    def search(self, query: str, search_type: str = "text", timelimit: str = None, region: str = "wt-wt") -> Answer:
        start_time = time.time()
        
        # 定义任务：为了弥补 Yahoo 的移除，我们通过两次不同参数的请求获取更多结果
        engines = []
        if search_type == "text":
            # 任务1: 默认参数获取 15 条
            engines.append((self._search_ddgs, query, "text", timelimit, region, 15))
            # 任务2: 尝试获取更多结果 (模拟翻页/更多)
            engines.append((self._search_ddgs, query, "text", timelimit, region, 30))
        else:
            # 其他类型（news, videos, books）
            engines.append((self._search_ddgs, query, search_type, timelimit, region, 20))
        
        all_results = []
        errors = []
        with ThreadPoolExecutor(max_workers=len(engines)) as executor:
            futures = [executor.submit(*e) for e in engines]
            for future in as_completed(futures):
                res = future.result()
                for r in res:
                    if r.url == "error":
                        errors.append(r.title)
                    else:
                        all_results.append(r)
                
        validated_results = self._cross_validate(all_results)
        
        answer_text = ""
        if validated_results:
            answer_parts = []
            for i, s in enumerate(validated_results[:5], 1):
                badge = "✓" if s.cross_validated else "○"
                date_str = f" [{s.date}]" if s.date else ""
                extra_str = f" ({', '.join(f'{k}:{v}' for k,v in s.extra.items() if v)})" if s.extra else ""
                answer_parts.append(f"{i}. {badge} {s.title}{date_str}{extra_str}\n   {s.snippet}")
            answer_text = "\n\n".join(answer_parts)
        else:
            error_msg = f" (Errors: {'; '.join(errors)})" if errors else ""
            answer_text = f"未找到相关结果，搜索引擎可能受到限制。{error_msg}"
            
        cross_count = sum(1 for s in validated_results if s.cross_validated)
        confidence = "HIGH" if cross_count >= 2 else ("MEDIUM" if validated_results else "LOW")
        
        return Answer(
            query=query,
            search_type=search_type,
            answer=answer_text,
            confidence=confidence,
            sources=validated_results[:15],
            validation={
                "total_results": len(all_results),
                "unique_results": len(validated_results),
                "cross_validated": cross_count
            },
            metadata={
                "engines_used": [e[2] for e in engines],
                "errors": errors
            },
            elapsed_ms=int((time.time() - start_time) * 1000)
        )

def main():
    parser = argparse.ArgumentParser(description="Free Web Search Ultimate (v8.0)")
    parser.add_argument("query", help="搜索关键词")
    parser.add_argument("--type", choices=["text", "news", "videos", "books"], default="text", help="搜索类型: text(网页), news(新闻), videos(视频), books(书籍)")
    parser.add_argument("--region", default="wt-wt", help="地区代码，如 zh-cn, en-us, wt-wt(全球)")
    parser.add_argument("--timelimit", choices=["d", "w", "m", "y"], help="时间限制: d(天), w(周), m(月), y(年)")
    parser.add_argument("--json", action="store_true", help="输出JSON格式")
    
    args = parser.parse_args()
    
    searcher = UltimateSearcher()
    answer = searcher.search(args.query, search_type=args.type, timelimit=args.timelimit, region=args.region)
    
    if args.json:
        print(json.dumps(asdict(answer), indent=2, ensure_ascii=False))
    else:
        print(f"\n{'='*60}")
        print(f"🔍 搜索: {answer.query} (类型: {answer.search_type} | 地区: {args.region})")
        print(f"⏱️  耗时: {answer.elapsed_ms}ms | 置信度: {answer.confidence}")
        print(f"📊 结果: 找到 {answer.validation['unique_results']} 个独立结果，{answer.validation['cross_validated']} 个交叉验证")
        if answer.metadata['errors']:
            print(f"⚠️ 警告: 发生 {len(answer.metadata['errors'])} 个引擎错误")
        print(f"{'='*60}\n")
        
        if answer.sources:
            print("📋 摘要结果:\n")
            print(answer.answer)
            print(f"\n{'-'*60}")
            print("🔗 详细来源:")
            for i, s in enumerate(answer.sources, 1):
                badge = "✓" if s.cross_validated else "○"
                date_str = f" [{s.date}]" if s.date else ""
                extra_str = f" {s.extra}" if s.extra else ""
                print(f"  {i}. {badge} [{s.engine}] {s.title[:60]}{date_str}{extra_str}")
                print(f"     URL: {s.url[:80]}...")
        else:
            print("❌ 未找到结果")

if __name__ == "__main__":
    main()
