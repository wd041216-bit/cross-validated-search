# Gemini Submission Checklist

This repository is prepared for the current Gemini CLI extension-gallery path.

## What Gemini needs

- public GitHub repository
- root `gemini-extension.json`
- root `skills/` directory with at least one skill
- clear context file for Gemini users
- tagged release and installable package
- stable README with a fast verification path

## What is already done here

- Public repo: `wd041216-bit/cross-validated-search`
- Extension manifest: [`gemini-extension.json`](../gemini-extension.json)
- Root skill: [`skills/cross-validated-search/SKILL.md`](../skills/cross-validated-search/SKILL.md)
- Gemini context: [`GEMINI.md`](../GEMINI.md) and [`.gemini/SKILL.md`](../.gemini/SKILL.md)
- Package published: [`cross-validated-search` on PyPI](https://pypi.org/project/cross-validated-search/)
- Tagged release: [`v16.0.0`](https://github.com/wd041216-bit/cross-validated-search/releases/tag/v16.0.0)
- Fast verification path: [`README.md`](../README.md) and [`docs/ecosystem-readiness.md`](./ecosystem-readiness.md)
- Free dual-provider path: [`docs/searxng-self-hosted.md`](./searxng-self-hosted.md)

## Recommended repo metadata

- Homepage: `https://pypi.org/project/cross-validated-search/`
- Topic: `gemini-cli-extension`
- Keep `gemini-cli`, `mcp`, `web-search`, and `fact-checking`

## Fast reviewer command

```bash
pip install cross-validated-search
evidence-report "Python 3.13 stable release" --claim "Python 3.13 is the latest stable release" --deep --json
```

## Notes

- The package keeps `free_web_search` compatibility aliases for existing users, but all new documentation points to `cross-validated-search`.
- The recommended free setup for stronger evidence reports is `ddgs + self-hosted SearXNG`.
