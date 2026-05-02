---
description: Dashboard view of all BELIEF engagements and their lifecycle stage
argument-hint: ""
---

# BELIEF Status

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Display a dashboard of all BELIEF engagements across the WE Marketing shared drive, showing lifecycle stage, engagement mode, and completeness indicators.

## Trigger

User runs `/belief status` or asks to see all BELIEF engagements, check on project status, or view the BELIEF pipeline.

## Inputs

1. **Filter** (optional) — filter by stage (e.g., "active only", "completed only") or by client name

## Dashboard Process

### Step 1: Find All Knowledge Bases

Search the WE Marketing shared drive for all files named `BELIEF Knowledge Base — *` using `mcp__google-workspace__search_drive_files`.

### Step 2: Read Each Knowledge Base

For each knowledge base found, read using `mcp__google-workspace__get_doc_as_markdown` and extract:
- Client name (from title)
- Engagement mode
- Session date
- Last updated date and by which command
- Which sections have content (to determine lifecycle stage)

### Step 3: Determine Lifecycle Stage

Derive the stage from knowledge base content:

| Stage | Indicator |
|-------|-----------|
| `intake` | KB exists but Document Inventory and Research Findings are empty |
| `researching` | Document Inventory or Research Findings have content |
| `prepped` | A Facilitator's Playbook doc exists in the folder |
| `session-complete` | Session Insights section has content |
| `delivered` | Brand Foundation Draft section has content |
| `closed` | Engagement appears in the cross-client knowledge base's Engagement Log |

### Step 4: Assess Completeness

For active engagements, note what's been done and what's missing:
- Documents analyzed? (Y/N, count)
- Research completed? (Y/N, areas covered)
- Playbook generated? (Y/N)
- Session synthesized? (Y/N)
- Brand foundation drafted? (Y/N)
- Learnings captured? (Y/N)

## Output

```
BELIEF Engagement Dashboard

Active Engagements:

| Client | Mode | Stage | Session Date | Last Activity | Next Step |
|--------|------|-------|-------------|---------------|-----------|
| [Name] | [mode] | [stage] | [date] | [date + cmd] | [recommendation] |
| [Name] | [mode] | [stage] | [date] | [date + cmd] | [recommendation] |

Completed Engagements:

| Client | Mode | Session Date | Closed Date |
|--------|------|-------------|-------------|
| [Name] | [mode] | [date] | [date] |

Summary:
  Active: [N] engagements
  Completed: [N] engagements
  Next session: [Client Name] on [date]
```

After the dashboard, ask:

> "Would you like to:
> - Drill into a specific engagement?
> - Run the recommended next step for any active engagement?
> - Set up a new engagement with `/belief intake`?"
