---
name: cross-validated-search
description: >
  Cross-Validated Web Search for Hallucination-Free LLM Responses.
  Multi-source verification prevents AI hallucinations.
  Zero-cost, privacy-first, supports text/news/images/books/videos.
version: "15.0.0"
user-invocable: true
allowed-tools: "Bash"
hooks:
  UserPromptSubmit:
    - hooks:
        - type: command
          command: |
            if echo "$CLAUDE_USER_PROMPT" | grep -qiE 'search|find|lookup|what is|who is|when did|where is|how many|latest|recent|最新|搜索|查询|查找'; then
              echo '[cross-validated-search] Factual query detected. Consider using cross-validated search for accuracy.'
              echo 'Run: search-web "<query>" [--type news|text|images|videos|books]'
            fi
---

# Cross-Validated Search for Claude Code

Work like a researcher: Always verify facts with multiple sources before answering.

## Installation

```bash
pip install free-web-search-ultimate
```

## Quick Start

```bash
# General knowledge (cross-validated)
search-web "What is the population of Tokyo?"

# News search with time filter
search-web "OpenAI GPT-5 release date" --type news --timelimit w

# Images (verified sources)
search-web "neural network architecture diagram" --type images

# Chinese content
search-web "人工智能最新进展" --region zh-cn
```

## When to Use

**Trigger Conditions:**
- Factual questions about events, people, dates, statistics
- Questions about recent events (< 1 year)
- Questions requiring verification
- User asks for sources or citations
- Claims that need fact-checking

**Decision Tree:**

```
User asks a question
        │
        ▼
Is it creative/hypothetical?
   YES → Answer directly (no search needed)
   NO  ▼
Does it involve facts, events, versions, or data?
   YES ▼
Run: search-web "<query>" [--type news if recent]
        │
        ▼
What is the confidence score?
   ┌─────────────────────────────────────────────────────────┐
   │ ✅ Verified    → Report as fact, cite all sources       │
   │ 🟢 Likely True → Report with confidence, cite sources   │
   │ 🟡 Uncertain   → Report with caveat, suggest verification│
   │ 🔴 Likely False→ Do not use, explain contradictions      │
   └─────────────────────────────────────────────────────────┘
        │
        ▼
Are there conflicting sources?
   YES → Present both viewpoints with citations
   NO  → Synthesize answer with unified citation
```

## Confidence Levels

| Score | Meaning | Action |
|-------|---------|--------|
| ✅ Verified | 3+ sources agree, high authority | Safe to cite as fact |
| 🟢 Likely True | 2 sources agree, medium confidence | Cite with confidence note |
| 🟡 Uncertain | Single source or minor conflicts | Flag as "unverified" |
| 🔴 Likely False | Major contradictions or no sources | Do not use, flag as unreliable |

## Commands

### `search-web` — Cross-Validated Web Search

```bash
# Basic search
search-web "query"

# Search types
search-web "query" --type text      # General knowledge
search-web "query" --type news      # Current events
search-web "query" --type images    # Visual references
search-web "query" --type videos    # Tutorials, presentations
search-web "query" --type books     # Academic, in-depth

# Time filters (for news)
search-web "query" --type news --timelimit d  # Day
search-web "query" --type news --timelimit w  # Week
search-web "query" --type news --timelimit m  # Month

# Region-specific
search-web "query" --region zh-cn   # Chinese
search-web "query" --region ja-jp   # Japanese
search-web "query" --region de-de   # German

# JSON output
search-web "query" --json
```

### `browse-page` — Deep Page Reading

```bash
# Read full content of a URL
browse-page "https://arxiv.org/abs/2303.08774"

# JSON output
browse-page "https://example.com/article" --json
```

## Anti-Hallucination Guarantees

When using this skill, you get:

1. **No Single-Source Claims** — Every fact is verified against multiple sources
2. **Confidence Transparency** — You know exactly how confident the system is
3. **Source Attribution** — Every claim comes with verifiable URLs
4. **Conflict Detection** — Conflicting information is flagged, not hidden
5. **Recency Guarantee** — For time-sensitive topics, results are from the specified time window

## MCP Integration

For Claude Desktop or other MCP-compatible tools:

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

## Example Usage in Claude Code

```
User: What's the latest version of Python?

Claude: Let me search for that with cross-validation...

$ search-web "latest Python version" --type news

[Results with confidence scores]

Based on cross-validated sources:
- ✅ Python 3.13.2 is the latest stable release (March 2026)
- Sources: python.org, Wikipedia, tech news (3 sources agree)

User: Who won the 2025 Nobel Prize in Physics?

Claude: Let me verify that with multiple sources...

$ search-web "2025 Nobel Prize Physics winner" --type news

[Results with confidence scores]

Based on cross-validated sources:
- ✅ The 2025 Nobel Prize in Physics was awarded to [verified winner]
- Sources: nobelprize.org, major news outlets (5 sources agree)
```

## Requirements

- Python 3.10+
- `beautifulsoup4`, `lxml`, `ddgs`, `mcp>=1.1.2`

## License

MIT-0 — Free to use, modify, and redistribute.