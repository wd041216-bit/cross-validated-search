---
name: free-web-search-ultimate
version: "4.0.0"
description: >
  Zero-cost, privacy-first web search and browsing for AI agents.
  Uses DuckDuckGo, Yahoo, and Qwant with cross-validation.
  No API keys required.
homepage: https://github.com/wd041216-bit/free-web-search-ultimate
---

# Free Web Search Ultimate v4.0

**Zero API Keys. High Reliability. Cross-Validated Results.**

This skill provides AI agents with reliable web search and page browsing capabilities without relying on expensive API keys or external services.

## Features

- **Multi-Engine Search**: Parallel queries to DuckDuckGo, Yahoo, and Qwant.
- **Cross-Validation**: Automatically groups and validates results across different engines to ensure credibility.
- **Smart Parsing**: Resolves redirect URLs to provide real, clickable links.
- **Anti-Bot Bypass**: Uses randomized User-Agents and identity headers to minimize blocking.
- **Clean Browsing**: Extracts pure text content from web pages, stripping out scripts, styles, and boilerplate.

## Quick Start

### 1. Web Search

Use `search_web.py` to search the internet. It returns cross-validated results with summaries.

```bash
# Basic usage
python scripts/search_web.py "Python 3.12 new features"

# JSON output for agent parsing
python scripts/search_web.py "Python 3.12 new features" --json
```

### 2. Browse Page

Use `browse_page.py` to read the full content of a specific URL.

```bash
# Read a page (default max 10,000 chars)
python scripts/browse_page.py "https://docs.python.org/3/whatsnew/3.12.html"

# JSON output
python scripts/browse_page.py "https://docs.python.org/3/whatsnew/3.12.html" --json
```

## Why Use This Skill?

Many web search skills rely on paid APIs (like Brave, Google, or Bing API) or use single engines that often get blocked. 

**Free Web Search Ultimate** solves this by:
1. Not requiring any API keys.
2. Using parallel requests to multiple engines.
3. Automatically decoding redirect links so agents can actually browse the results.

## Requirements

- Python 3.8+
- `beautifulsoup4`
- `lxml`

```bash
pip install beautifulsoup4 lxml
```
