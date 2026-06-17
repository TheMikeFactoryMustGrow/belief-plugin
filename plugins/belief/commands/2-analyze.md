---
description: Ingest and analyze all documents in a client's BELIEF folder
argument-hint: "<client name>"
---

# BELIEF Analyze

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Ingest all documents in a client's BELIEF folder, produce a structured synthesis, and update the per-client knowledge base. Supports incremental re-analysis — only processes new or changed documents since the last run.

## Trigger

User runs `/belief:2-analyze` or asks to review client materials, ingest documents, analyze homework, audit what's been uploaded, or check for gaps in client materials.

## Inputs

1. **Client name** (required) — the client whose BELIEF folder to analyze

2. **Focus area** (optional) — if the user wants to focus on specific documents or themes rather than analyzing everything

## Analysis Process

### Step 1: Read the Knowledge Base

- Find the client's knowledge base doc (`BELIEF Knowledge Base — [Client Name]`) using `mcp__google_work__search_drive_files`
- Read the full content using `mcp__google_work__get_doc_as_markdown`
- Extract the Engagement Config (mode, contacts) and Document Inventory (what's already been ingested)
- If no knowledge base exists, prompt the user to run `/belief:1-intake` first

### Step 2: Inventory the BELIEF Folder

- List all files in the client's `BELIEF/` folder using `mcp__google_work__list_drive_items`
- Also check the parent client folder for BELIEF-related files that may not have been moved into the subfolder
- Compare the current file list against the Document Inventory in the knowledge base
- Identify new files (not yet in the inventory) and potentially changed files

**Completeness audit:** Score the folder contents against the 5-category Client Materials Checklist in the knowledge-base skill (Core Business Docs, Existing Brand Materials, Market & Competitive Context, Performance & Impact Data, Additional Strategic Context). Report the completeness percentage and flag the most impactful missing items.

**Homework audit:** If homework documents are present, check completeness against the 7 homework question areas (SWOT, Value Proposition, Purpose, Vision, Strategy, Audience, Competitors). Flag any areas that were skipped or given only superficial answers. If multiple team members submitted separate homework, cross-reference for alignment and tension.

Skip these system files (don't analyze them):
- The knowledge base doc itself
- The session template slides (empty template)
- The homework template (empty template)
- Previously generated playbooks or brand foundation drafts

### Step 3: Read New Documents

For each new or changed document:

**Google Docs** (`.gdoc`): Read using `mcp__google_work__get_doc_as_markdown`

**Google Slides** (`.gslides`): Read using `mcp__google_work__get_drive_file_content` — focus on text content and speaker notes

**Google Sheets** (`.gsheet`): Read using `mcp__google_work__get_drive_file_content` — look for data tables and key metrics

**PDFs and DOCX**: Check the local Google Drive mount at `~/Library/CloudStorage/GoogleDrive-mike@wassonenterprise.com/`. Read using local file access. If the file is not accessible locally, note it as a gap and tell the user.

**Gemini meeting notes**: These are Google Docs with names like `[Client] BELIEF Session - [date] - Notes by Gemini`. Read as Google Docs. Flag these separately — they contain session content that feeds `/belief:4-synthesize`.

For each document read, record:
- Filename and type
- Date ingested (today)
- Contributor (if identifiable from the document or its Drive metadata)
- One-line summary of the document's content

### Step 4: Synthesize Understanding

With all document contents loaded, produce a structured synthesis following the knowledge base schema. Consider the engagement mode when analyzing:

**For all modes:**
- **What We Know**: Extract confirmed facts, positions, and clear signals. What is this company? What do they believe? Who do they serve?
- **What's Missing (Gaps)**: What information would we want that isn't in these documents? What questions remain unanswered?
- **Key Themes**: What patterns recur across multiple documents? What words and ideas keep appearing?
- **Contradictions & Tensions**: Where do documents tell conflicting stories? Where does the homework contradict the materials? Where does the stated mission differ from observed behavior? **These are the most valuable findings — they become insight triggers for the Facilitator's Playbook.**
- **Open Questions**: What should the BELIEF session explore? What can only be answered through direct conversation with the leadership team?

**Mode-specific emphasis:**

- **new-brand**: Focus on founder/leadership intent, aspirational language, unspoken assumptions about identity, and gaps where the company hasn't yet defined who they are.
- **rebrand-tweak**: Focus on what's working in the current brand (keep), what's outdated (update), and perception gaps between how they see themselves vs. how materials present them.
- **rebrand-pivot**: Focus on why the current brand no longer fits, what has changed (market, leadership, strategy), what they want to leave behind, and what the new identity should signal.

### Step 5: Merge with Existing Knowledge Base

If the knowledge base already has content in the synthesis sections (from a previous run):
- **Merge** new insights with existing ones — don't overwrite
- **Note** what changed since the last analysis
- **Elevate** themes that strengthened with new evidence
- **Flag** new contradictions that emerged

### Step 6: Update the Knowledge Base

Update the knowledge base doc:
1. Add new entries to the Document Inventory table
2. Update the Synthesized Understanding sections with merged content
3. Update the "Last Updated" field: `[today's date] by /belief:2-analyze`

Use `mcp__google_work__modify_doc_text` for targeted updates.

## Output

Present a structured summary to the user:

```
BELIEF Analysis Complete — [Client Name]

Documents processed: [N new] ([M total in inventory])
Mode: [engagement mode]

Key Themes:
  - [Theme 1]
  - [Theme 2]
  - [Theme 3]

Contradictions Found:
  - [Tension 1 — brief description]
  - [Tension 2 — brief description]

Gaps Identified:
  - [Missing info 1]
  - [Missing info 2]

Open Questions for the BELIEF Session:
  - [Question 1]
  - [Question 2]

Knowledge base updated: BELIEF Knowledge Base — [Client Name]
```

After the summary, ask:

> "Would you like to:
> - Run `/belief:2-research` to fill gaps with independent market research?
> - Run `/belief:3-prep` to generate the Facilitator's Playbook?
> - Dive deeper into any of the contradictions or themes identified?
> - Re-analyze after additional materials arrive?"
