# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. For example, `~~cloud storage` might mean Google Drive, Dropbox, or any other storage platform with an MCP server.

This plugin primarily uses the **Google Workspace MCP server**, which is expected to be configured globally (not in this plugin's `.mcp.json`). The `mcp__google-workspace__*` tools provide access to Google Drive, Docs, Sheets, and Slides.

## Connectors for this plugin

| Category | Placeholder | Expected server | Other options |
|----------|-------------|----------------|---------------|
| Cloud storage & docs | `~~cloud storage` | Google Workspace (global) | OneDrive, Dropbox |
| Web research | `~~web research` | Web search / Web fetch (built-in) | Similarweb, Ahrefs |
| Chat | `~~chat` | Slack | Microsoft Teams |
