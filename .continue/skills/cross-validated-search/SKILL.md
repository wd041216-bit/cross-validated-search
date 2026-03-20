---
name: cross-validated-search
description: >
  Cross-Validated Web Search for Hallucination-Free LLM Responses.
  Multi-source verification prevents AI hallucinations.
  Zero-cost, privacy-first, supports text/news/images/books/videos.
version: "15.0.0"
user-invocable: true
---

# Cross-Validated Search for Continue

Work like a researcher: Always verify facts with multiple sources before answering.

## Installation

```bash
pip install free-web-search-ultimate
```

## Commands

```bash
# General knowledge (cross-validated)
search-web "What is the population of Tokyo?"

# News search with time filter
search-web "OpenAI GPT-5 release date" --type news --timelimit w

# Images (verified sources)
search-web "neural network architecture diagram" --type images

# Academic sources
search-web "transformer attention mechanism" --type books

# Region-specific
search-web "人工智能最新进展" --region zh-cn

# JSON output
search-web "quantum computing" --json

# Read full page content
browse-page "https://arxiv.org/abs/2303.08774"
```

## When to Use

**Trigger:**
- Factual questions about events, people, dates, statistics
- Questions about recent events (< 1 year)
- Questions requiring verification
- User asks for sources or citations

## Confidence Levels

| Score | Meaning | Action |
|-------|---------|--------|
| ✅ Verified | 3+ sources agree, high authority | Report as fact |
| 🟢 Likely True | 2 sources agree, medium confidence | Cite with note |
| 🟡 Uncertain | Single source or minor conflicts | Flag as unverified |
| 🔴 Likely False | Major contradictions or no sources | Do not use |

## Anti-Hallucination Guarantees

1. **Multi-Source Verification** — Facts verified against multiple independent sources
2. **Confidence Scoring** — Clear indication of reliability
3. **Source Attribution** — Every claim includes verifiable URLs
4. **Conflict Detection** — Conflicting information flagged
5. **Time-Sensitive Results** — Recent results for current events

## MCP Integration

For Continue with MCP support:

```json
{
  "mcpServers": {
    "free-web-search": {
      "command": "free-web-search-mcp",
      "args": []
    }
  }
}
```

## Requirements

- Python 3.10+
- `beautifulsoup4`, `lxml`, `ddgs`, `mcp>=1.1.2`

## License

MIT-0 — Free to use, modify, and redistribute.