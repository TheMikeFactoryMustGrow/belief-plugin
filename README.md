# BELIEF Plugin

A plugin for [Cowork](https://claude.com/product/cowork) that automates the Wasson Enterprise BELIEF brand discovery process. Handles document ingestion, market research, facilitator preparation, post-session synthesis, and cross-engagement learning.

## Installation

In Claude Code or Cowork, add this repo as a marketplace and install the plugin:

```
/plugin marketplace add TheMikeFactoryMustGrow/belief-plugin
/plugin install BELIEF@belief-plugin
```

The plugin requires the Google Workspace MCP server to be configured globally — see [`plugins/belief/CONNECTORS.md`](plugins/belief/CONNECTORS.md) for the full integration list.

## Commands

| Command | Description |
|---|---|
| `/BELIEF intake` | Set up a new BELIEF engagement — configure client, mode, and create Drive structure |
| `/BELIEF analyze` | Ingest and analyze all documents in a client's BELIEF folder |
| `/BELIEF research` | Conduct independent 7-area market research for a client |
| `/BELIEF prep` | Generate the Facilitator's Playbook — question trees, insight triggers, and context cards |
| `/BELIEF synthesize` | Process post-session notes and transcripts into structured insights |
| `/BELIEF distill` | Generate candidate brand essence statements and brand foundation draft |
| `/BELIEF status` | Dashboard view of all BELIEF engagements and their lifecycle stage |
| `/BELIEF learn` | Capture cross-client learnings after engagement completion |

## Skills

| Skill | Description |
|---|---|
| `knowledge-base` | Per-client knowledge base schema, update conventions, and Google Drive integration patterns |
| `brand-discovery` | BELIEF methodology, session stages, engagement modes, and facilitation principles |
| `question-generation` | Socratic questioning framework, question trees, insight triggers, and context cards |
| `research-methodology` | 7-area market research framework with mode-specific guidance |

## Engagement Modes

All commands support three engagement modes that change analytical emphasis while keeping the same session structure:

- **new-brand** — Building a brand from scratch. Focus on market white space, founder intent, competitive differentiation.
- **rebrand-tweak** — Refining an existing brand. Focus on what's working, perception gaps, evolution opportunities.
- **rebrand-pivot** — Transforming to a new identity. Focus on why the old brand no longer fits, signaling change to audiences.

## How It Works

The plugin maintains two compounding knowledge bases:

1. **Per-client knowledge base** — A Google Doc in each client's BELIEF folder. Every command reads from and writes to it. When Kathryn runs `/BELIEF analyze` and Stacy later runs `/BELIEF research`, Stacy's research benefits from Kathryn's analysis. The knowledge base is the single source of synthesized context.

2. **Cross-client knowledge base** — A Google Doc on the WE Marketing shared drive. After each engagement, `/BELIEF learn` captures facilitation patterns, industry intelligence, and process improvements. When generating playbooks for new clients, the system draws on patterns from similar past engagements.

## Typical Workflow

```
/BELIEF intake          # T-5 weeks: Set up engagement
/BELIEF analyze         # T-3 weeks: Ingest client homework and materials
/BELIEF research        # T-3 weeks: Independent market research (parallel)
/BELIEF analyze         # T-2 weeks: Re-analyze after new materials arrive
/BELIEF prep            # T-1 week:  Generate Facilitator's Playbook
                        # Day 0:     BELIEF session (human-led)
/BELIEF synthesize      # +24 hours: Process session notes
/BELIEF distill         # Week 1:    Generate brand foundation draft
/BELIEF learn           # Week 8:    Capture cross-client learnings
```

## MCP Integrations

This plugin uses the globally configured Google Workspace MCP server for all Drive, Docs, and Slides operations. No additional MCP servers are required, though web search capabilities are used for the `/BELIEF research` command.
