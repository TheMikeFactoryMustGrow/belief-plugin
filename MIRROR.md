# Pull-only mirror

This checkout exists so agents working under `_claude_config/` can read plugin
context incrementally. It is **not** a second place to invent commits.

- **Canonical remote:** same GitHub repo as `~/.claude/plugins/marketplaces/…`
- **Edit rule:** prefer marketplace path for Claude/Grok runtime; if you commit here, **push immediately** then `git pull --ff-only` the marketplace clone.
- **Never** let this tip diverge silently. Fleet health treats tip mismatch as red.

Synced after MCP rename push: 2026-07-09
