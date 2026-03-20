# Cross-Validated Search for GitHub Copilot

Use cross-validated search when you need to verify facts or find recent information.

## Installation

```bash
pip install free-web-search-ultimate
```

## Commands

```bash
# Cross-validated web search
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

Use cross-validated search for:
- Factual questions about events, versions, releases
- Recent news (< 1 year)
- Statistics, numbers, dates
- Verification of claims
- Finding authoritative sources

## Confidence Levels

| Score | Meaning | Action |
|-------|---------|--------|
| ✅ Verified | 3+ sources agree, high authority | Cite as fact |
| 🟢 Likely True | 2 sources agree, medium confidence | Cite with note |
| 🟡 Uncertain | Single source or minor conflicts | Flag as unverified |
| 🔴 Likely False | Major contradictions or no sources | Do not use |

## Anti-Hallucination Guarantees

1. **Multi-Source Verification** — Facts verified against multiple independent sources
2. **Confidence Scoring** — Clear indication of reliability
3. **Source Attribution** — Every claim includes verifiable URLs
4. **Conflict Detection** — Conflicting information flagged
5. **Time-Sensitive Results** — Recent results for current events

## Example Usage

```python
# In Copilot chat
# User: What's the latest version of Python?

# Copilot runs:
# search-web "latest Python version" --type news

# Copilot responds:
# Based on cross-validated sources:
# - ✅ Python 3.13.2 is the latest stable release (March 2026)
# - Sources: python.org, Wikipedia, tech news (3 sources agree)
```

## MCP Integration

For VS Code with MCP support:

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