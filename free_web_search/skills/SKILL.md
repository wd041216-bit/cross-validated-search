---
name: free-web-search-ultimate
version: "10.0.0"
description: >
  Zero-cost, privacy-first web search and browsing for AI agents.
  Supports text, news, books, videos, and IMAGES search types with region targeting.
  Powered by official ddgs with optimized single-request fetching and un-truncated URLs.
homepage: https://github.com/wd041216-bit/free-web-search-ultimate
---

# Free Web Search Ultimate v10.0 (CLI-Anything Harness)

**Standard Python Package. PATH Execution. REPL Mode. Auto-Discoverable SKILL.**

This skill provides AI agents with reliable web search and page browsing capabilities without relying on expensive API keys or external services.

## What's New in v10.0
- **CLI-Anything Standard**: Fully refactored to match the CLI-Anything methodology. The project is now a standard Python package with `entry_points`.
- **PATH Execution**: After `pip install -e .`, agents can directly run `search-web` and `browse-page` from anywhere in the terminal, without needing the exact script path.
- **REPL Mode**: Running `search-web` without arguments now enters an interactive REPL mode, allowing continuous searching without re-initializing the environment.
- **Auto-Discoverable SKILL**: `SKILL.md` is now packaged inside the Python module via `package_data`. When agents install this tool, the skill definition is automatically discoverable.

## Features

- **Precise Intent Control**: Choose `text` (general), `news` (recent events), `images` (visuals), `books` (academic/publications), or `videos` (multimedia).
- **Region Targeting**: Get results tailored to specific languages and locations.
- **Time Filters**: Find the most recent information easily.
- **Cross-Validation**: Automatically groups and validates results to ensure credibility.
- **Clean Browsing**: Extracts pure text content from web pages, stripping out scripts and styles while preserving useful context.

## Quick Start

### 1. Web Search

Use `search-web` to search the internet. It returns cross-validated results with summaries.

```bash
# Basic usage (defaults to text search)
search-web "Python 3.12 new features"

# Search for recent news
search-web "OpenAI" --type news

# Search for images (with advanced filters)
search-web "Python logo" --type images --size Large --color Blue

# Search for books/academic materials
search-web "machine learning" --type books

# Search for videos
search-web "how to tie a tie" --type videos

# Search with region and time limit (Chinese results from past week)
search-web "人工智能" --region zh-cn --timelimit w

# JSON output for agent parsing
search-web "Python 3.12 new features" --json
```

**Agent Best Practices:**
- Use default `--type text` for technical documentation, tutorials, and general knowledge.
- Use `--type news` ONLY when searching for current events, breaking news, or recent company updates.
- Use `--type images` when the user explicitly asks for pictures, photos, logos, or diagrams.
- Use `--type books` when looking for in-depth knowledge, authors, or publication years.
- Always use `--region` when searching in languages other than English (e.g., `--region zh-cn` for Chinese).

### 2. Browse Page

Use `browse-page` to read the full content of a specific URL.

```bash
# Read a page (default max 10,000 chars)
browse-page "https://docs.python.org/3/whatsnew/3.12.html"

# JSON output
browse-page "https://docs.python.org/3/whatsnew/3.12.html" --json
```

## Requirements

- Python 3.8+
- `beautifulsoup4`
- `lxml`
- `ddgs`

```bash
pip install -r requirements.txt
```
