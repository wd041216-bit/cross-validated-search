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

## Installation

1. Clone this repository to your agent's workspace.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

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

## Why Use This Skill?

Many web search skills rely on paid APIs (like Brave, Google, or Bing API) or use outdated HTML scraping methods that often get blocked. 

**Free Web Search Ultimate** solves this by:
1. Not requiring any API keys.
2. Using the official `ddgs` library as the primary engine for extreme stability.
3. Implementing thread-safe concurrent fetching for maximum speed.
4. Providing dedicated endpoints for text, news, books, and videos.

## License

MIT License
