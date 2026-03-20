<div align="center">
  <img src="assets/banner.png" alt="Cross-Validated Search" width="100%"/>
  <h1>🔍 Cross-Validated Search</h1>
  <p><strong>The Only Search Skill That Prevents LLM Hallucinations</strong></p>
  <p><em>Multi-source verification. Zero hallucinations. Free forever.</em></p>
  
  [![PyPI version](https://badge.fury.io/py/cross-validated-search.svg)](https://pypi.org/project/cross-validated-search/)
  [![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://python.org)
  [![MCP Ready](https://img.shields.io/badge/MCP-Ready-purple.svg)](https://modelcontextprotocol.io/)
  [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
</div>

<br/>

> **Stop hallucinations. Start verification.**

Every LLM hallucinates facts—Claude, GPT-4, Gemini, Llama—all of them. This plugin introduces **Cross-Validated Search**: every claim is verified against multiple independent sources before being presented as fact.

## 🏗️ Architecture

<div align="center">
  <img src="assets/architecture.png" alt="Architecture Diagram" width="90%"/>
</div>

One plugin, every ecosystem. Whether you use Claude Code, Cursor, Copilot, Gemini, OpenClaw, or a custom agent, this plugin connects your LLM to verified facts through cross-validation.

## 🌟 Supported Platforms

| Platform | Support | Configuration |
|----------|---------|--------------|
| **Claude Code** | ✅ Native | `.claude-plugin/SKILL.md` |
| **Cursor** | ✅ Native | `.cursor/rules/` |
| **GitHub Copilot** | ✅ Native | `.github/copilot/` |
| **Gemini CLI** | ✅ Native | `.gemini/SKILL.md` |
| **Continue** | ✅ Native | `.continue/skills/` |
| **Kiro** | ✅ Native | `.kiro/steering/` |
| **OpenCode** | ✅ Native | `.opencode/instructions.md` |
| **Codex** | ✅ Native | `.codex/SKILL.md` |
| **OpenClaw** | ✅ Native | `free_web_search/skills/SKILL.md` |
| **MCP Servers** | ✅ MCP | `free-web-search-mcp` |
| **CLI** | ✅ Universal | `search-web`, `browse-page` |
| **LangChain** | ✅ Tool wrapper | Python integration |
| **OpenAI Function Calling** | ✅ JSON schema | Function definitions |

## 🌟 The Cross-Validation Paradigm

| Old Paradigm (Standard LLM) | New Paradigm (Cross-Validated Search) |
|---|---|
| Answers from training data | Answers from real-time web search |
| May hallucinate facts | **Cross-validates facts across sources** |
| Single knowledge source | **Multiple independent sources** |
| No confidence score | **Confidence score per fact: ✅ 🟢 🟡 🔴** |
| User must trust blindly | **Cites all sources for verification** |

When this plugin is installed, the AI agent:

1. **Never Claims Unverified Facts** — Every factual claim is checked against multiple sources
2. **Cross-Validates** — Facts must appear in 2+ sources to be marked as verified
3. **Assigns Confidence** — Each fact gets a confidence score based on source agreement
4. **Cites All Sources** — Every claim comes with verifiable URLs

## 📦 Installation

```bash
pip install free-web-search-ultimate
```

> **Requirements:** Python 3.10+

Or install from source:

```bash
git clone https://github.com/wd041216-bit/cross-validated-search.git
cd cross-validated-search
pip install -e .
```

### 🚀 Enhanced Version (with API Providers)

Need more search providers? Check out the **[with-api-providers](https://github.com/wd041216-bit/cross-validated-search/tree/with-api-providers)** branch:

```bash
# Install enhanced version with Tavily support
pip install git+https://github.com/wd041216-bit/cross-validated-search@with-api-providers
```

**Enhanced features:**
- 🔍 **Tavily API** — Premium search quality (requires `TAVILY_API_KEY`)
- 🔄 **Parallel execution** — Multiple engines running concurrently
- 📊 **Better relevance** — Advanced search depth options

> **Note:** The enhanced version requires API keys. The main branch remains **free and keyless**.

## 🔌 Integration Guide

### Claude Code

The `.claude-plugin/SKILL.md` is automatically detected. Just install the package:

```bash
pip install free-web-search-ultimate
```

### Cursor

Copy `.cursor/rules/cross-validated-search.md` to your project, or install globally:

```bash
pip install free-web-search-ultimate
```

### GitHub Copilot

The `.github/copilot/instructions.md` is automatically detected by VS Code Copilot.

### Gemini CLI

The `.gemini/SKILL.md` is automatically detected when installed.

### Continue

Copy `.continue/skills/cross-validated-search/` to your Continue skills directory.

### OpenClaw (CLI-Anything)

```bash
pip install free-web-search-ultimate
```

The skill is auto-discovered from the bundled `SKILL.md`.

### MCP Integration (Claude Desktop, Cursor, Continue)

Add to your `claude_desktop_config.json` or MCP settings:

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

### LangChain / Custom Agents

```python
from langchain.tools import Tool
import subprocess, json

def cross_validate_search(query: str) -> str:
    result = subprocess.run(
        ["search-web", query, "--json"],
        capture_output=True, text=True
    )
    data = json.loads(result.stdout)
    return data.get("answer", "No results found.")

search_tool = Tool(
    name="cross_validate_search",
    func=cross_validate_search,
    description="Search the web with cross-validation. Every fact is verified against multiple sources."
)
```

### OpenAI Function Calling

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "cross_validate_search",
            "description": "Search the web with multi-source cross-validation. Prevents hallucinations by verifying facts across independent sources.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query"},
                    "type": {"type": "string", "enum": ["text", "news", "images", "videos", "books"], "default": "text"}
                },
                "required": ["query"]
            }
        }
    }
]
```

## 💻 CLI Usage

### `search-web` — Cross-Validated Web Search

```bash
# General knowledge (3+ sources, cross-validated)
search-web "What is the population of Tokyo?"

# Breaking news (multiple news sources)
search-web "OpenAI GPT-5" --type news --timelimit w

# Images (verified sources)
search-web "neural network diagram" --type images

# Chinese search
search-web "人工智能最新进展" --region zh-cn

# JSON output for programmatic use
search-web "quantum computing" --json
```

### `browse-page` — Deep Page Reading

```bash
# Read full page content
browse-page "https://arxiv.org/abs/2303.08774"

# JSON output
browse-page "https://example.com/article" --json
```

## 🎯 Confidence Scoring System

| Score | Meaning | When to Use |
|-------|---------|-------------|
| ✅ Verified | 3+ sources agree, high authority | Cite as fact |
| 🟢 Likely True | 2 sources agree, medium confidence | Cite with confidence note |
| 🟡 Uncertain | Single source or minor conflicts | Flag as unverified |
| 🔴 Likely False | Major contradictions or no sources | Do not use |

## 🏆 Why This Over Alternatives?

| Feature | Cross-Validated Search | Tavily API | Serper API | Bing Search API |
|---------|------------------------|-----------|------------|-----------------|
| Cost | **Free** | $0.01/req | $0.001/req | $3/1000 req |
| **Cross-Validation** | **Yes** | No | No | No |
| **Confidence Score** | **Yes** | No | No | No |
| **Hallucination Prevention** | **Yes** | No | No | No |
| API Key Required | **No** | Yes | Yes | Yes |
| IDE Support | **10+** | Limited | No | No |
| MCP Support | **Yes** | Partial | No | No |

## 📄 License

MIT-0 License — free for personal and commercial use. No attribution required.