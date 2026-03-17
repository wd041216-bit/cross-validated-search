---
name: free-web-search-ultimate
version: "8.0.0"
description: >
  Zero-cost, privacy-first web search and browsing for AI agents.
  Supports text, news, books, and videos search types with region targeting.
  Powered by official ddgs with concurrent multi-page fetching and robust error handling.
homepage: https://github.com/wd041216-bit/free-web-search-ultimate
---

# Free Web Search Ultimate v8.0 (Super Workflow Upgraded)

**Zero API Keys. High Reliability. Books & Videos Support. Thread-Safe Architecture.**

This skill provides AI agents with reliable web search and page browsing capabilities without relying on expensive API keys or external services.

## What's New in v8.0
- **New Search Types**: Added `--type books` and `--type videos` support, allowing agents to search for academic materials and multimedia content.
- **Removed Dead Engines**: Completely removed the deprecated Yahoo HTML scraper, replacing it with concurrent multi-page DDGS fetching for higher reliability and speed.
- **Thread-Safe Architecture**: Fixed a critical concurrency bug in DDGS client initialization, ensuring stable parallel requests.
- **Enhanced Content Extraction**: Relaxed filtering rules in `browse_page.py` to retain more useful content from complex sites (like documentation pages), while fully supporting gzip decompression.
- **Metadata for Agents**: JSON output now includes `metadata.engines_used` and `metadata.errors` to help agents understand search execution status.

## Features

- **Precise Intent Control**: Choose `text` (general), `news` (recent events), `books` (academic/publications), or `videos` (multimedia).
- **Region Targeting**: Get results tailored to specific languages and locations.
- **Time Filters**: Find the most recent information easily.
- **Cross-Validation**: Automatically groups and validates results to ensure credibility.
- **Clean Browsing**: Extracts pure text content from web pages, stripping out scripts and styles while preserving useful context.

## Quick Start

### 1. Web Search

Use `search_web.py` to search the internet. It returns cross-validated results with summaries.

```bash
# Basic usage (defaults to text search)
python scripts/search_web.py "Python 3.12 new features"

# Search for recent news
python scripts/search_web.py "OpenAI" --type news

# Search for books/academic materials
python scripts/search_web.py "machine learning" --type books

# Search for videos
python scripts/search_web.py "how to tie a tie" --type videos

# Search with region and time limit (Chinese results from past week)
python scripts/search_web.py "人工智能" --region zh-cn --timelimit w

# JSON output for agent parsing
python scripts/search_web.py "Python 3.12 new features" --json
```

**Agent Best Practices:**
- Use default `--type text` for technical documentation, tutorials, and general knowledge.
- Use `--type news` ONLY when searching for current events, breaking news, or recent company updates.
- Use `--type books` when looking for in-depth knowledge, authors, or publication years.
- Always use `--region` when searching in languages other than English (e.g., `--region zh-cn` for Chinese).

### 2. Browse Page

Use `browse_page.py` to read the full content of a specific URL.

```bash
# Read a page (default max 10,000 chars)
python scripts/browse_page.py "https://docs.python.org/3/whatsnew/3.12.html"

# JSON output
python scripts/browse_page.py "https://docs.python.org/3/whatsnew/3.12.html" --json
```

## Requirements

- Python 3.8+
- `beautifulsoup4`
- `lxml`
- `ddgs`

```bash
pip install -r requirements.txt
```
```
```
