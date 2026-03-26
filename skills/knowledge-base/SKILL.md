---
name: knowledge-base
description: Per-client knowledge base schema, update conventions, and Google Drive integration patterns for BELIEF engagements. Use when reading, creating, or updating a client's knowledge base, or when managing the cross-client learning repository.
---

# Knowledge Base Skill

Schema definitions, conventions, and integration patterns for the BELIEF knowledge base system. Every BELIEF command reads from and writes to the knowledge base — it is the compounding layer that makes each team member's work available to everyone else.

## Two-Level Architecture

### Per-Client Knowledge Base

A single Google Doc per client, stored in their `BELIEF/` folder on the WE Marketing shared drive. Path: `Shared drives/WE Marketing/Clients/[Client Name]/BELIEF/BELIEF Knowledge Base — [Client Name]`

This is the single source of synthesized context for a client engagement. Every BELIEF command reads it first and updates it after completing its work.

### Cross-Client Knowledge Base

A single Google Doc on the WE Marketing shared drive. Path: `Shared drives/WE Marketing/WE BELIEF/BELIEF Cross-Client Learnings`

Accumulates facilitation patterns, industry intelligence, and process improvements across all engagements. Read by `/belief prep` to enhance playbooks with cross-engagement intelligence.

## Per-Client Knowledge Base Schema

```markdown
# BELIEF Knowledge Base — [Client Name]

## Engagement Config
- **Mode**: [new-brand | rebrand-tweak | rebrand-pivot]
- **Session Date**: [YYYY-MM-DD]
- **Client Contacts**: [Name — Role, Name — Role]
- **WE Team**: [Name — Role, Name — Role]
- **Drive Folder**: [folder name or path]
- **Created**: [YYYY-MM-DD] | **Last Updated**: [YYYY-MM-DD by command-name]

## Document Inventory

| # | Document | Type | Date Ingested | Contributor | Summary |
|---|----------|------|--------------|-------------|---------|
| 1 | [filename] | [homework/materials/research/team-note] | [date] | [who added it] | [one-line summary] |

## Synthesized Understanding

### What We Know
[Key facts, confirmed positions, clear signals about who this company is]

### What's Missing (Gaps)
[Information we need but don't have yet — specific questions to pursue]

### Key Themes
[Recurring patterns across documents — what keeps coming up]

### Contradictions & Tensions
[Places where documents, homework, or research tell conflicting stories — these are gold for insight triggers]

### Open Questions
[Questions that the BELIEF session should answer — generated from gaps and tensions]

## Research Findings

### Company Overview
[History, leadership, size, stage, culture signals]

### Current Brand Expression
[How they present themselves today — website, materials, messaging, visual identity]

### Competitive Landscape
[Key competitors, positioning map, differentiation claims]

### Target Audience Signals
[Who they serve, audience demographics, behavioral signals, unmet needs]

### Market & Industry Trends
[Macro trends, regulatory shifts, technology changes affecting their space]

### White Space Analysis
[Positioning opportunities — where competitors aren't, what audiences need that nobody delivers]

### Past Campaigns & Creative
[Previous marketing efforts, what worked, what didn't, creative direction history]

## Session Insights

### Key Decisions Made
[Strategic decisions reached during the BELIEF session]

### Themes & Emotional Moments
[What resonated, what provoked strong reactions, breakthrough moments]

### Confirmed vs. Surprised
[Where pre-session research was validated vs. where reality differed]

### Commitments & Next Steps
[Who committed to what, with dates if specified]

## Brand Foundation Draft

### Brand Essence Statements
[The 2-3 distilled statements that capture who this company is]

### Purpose
[Why the company exists beyond making money]

### Vision
[What the world looks like if the company succeeds]

### Mission
[What the company does, for whom, and how]

### Core Values
[The non-negotiable principles that guide decisions]

### Positioning
[For [audience], [company] is the [category] that [differentiator] because [reason to believe]]

### Pillars & Reasons to Believe
[The proof points and supporting evidence for the brand's claims]
```

## Cross-Client Knowledge Base Schema

```markdown
# BELIEF Cross-Client Learnings

**Last Updated**: [YYYY-MM-DD]

## Facilitation Patterns

### Questions That Consistently Surface Good Insights
[Question types and framings that work across engagements]

### Facilitation Techniques
[Approaches to managing group dynamics, drawing out quiet voices, redirecting tangents]

### Common Pitfalls
[Patterns that lead to unproductive sessions — what to avoid]

## Industry Intelligence

### [Industry Name]
- **Common Positioning Patterns**: [how companies in this industry typically position]
- **Typical White Space**: [where opportunities tend to exist]
- **Audience Expectations**: [what customers in this space expect from brands]
- **Relevant Engagements**: [client names for reference]

## Process Improvements

### Timeline Optimizations
[What scheduling or sequencing changes improved outcomes]

### Prep Improvements
[What research or analysis approaches produced the best session inputs]

### Delivery Improvements
[What changes to post-session workflow improved deliverable quality]

## Engagement Log

| Client | Industry | Mode | Session Date | Key Takeaway |
|--------|----------|------|-------------|--------------|
| [name] | [industry] | [mode] | [date] | [one-line insight] |
```

## Client Homework Questions (Completeness Checklist)

The homework document sent to clients 3 weeks prior covers these areas. Use this to audit homework completeness in `/belief analyze`:

1. **SWOT Analysis**: Strengths (advantages, what we do better), Weaknesses (what to improve/avoid), Opportunities (trends, market gaps), Threats (obstacles, competitor moves)
2. **Value Proposition**: What do we currently do? How do we do it? For whom? What's our value?
3. **Purpose**: Why do we do what we do?
4. **Vision**: What does the company aspire to be? (may differ from current state)
5. **Strategy**: How can the company "win"?
6. **Audience**: Who are current customers? Who do we want them to be? How do customers find the brand? How do we talk to customers? How do we explain what we do?
7. **Competitors**: Who are they? (with website links and descriptions)

**Key principle from the workflow:** "Encourage clients to answer instinctively rather than aspirationally." When analyzing homework, flag responses that sound like marketing copy vs. genuine reflection.

Ideally, each attendee fills out their own homework separately. When multiple homework docs exist, cross-reference for alignment and tension.

## Client Materials Checklist (5 Categories)

Use this checklist in `/belief analyze` to score materials completeness and identify gaps.

### 1. Core Business Documents
- [ ] Company overview or "about us" document
- [ ] Organizational chart or team structure
- [ ] Summary of core products/services
- [ ] Client onboarding process documentation
- [ ] Customer support workflows
- [ ] Pitch deck or sales presentation
- [ ] Investor presentations or financial overview
- [ ] Sell sheets, one-pagers, outreach materials

### 2. Existing Brand Materials
- [ ] Current messaging for different audiences (customers, investors, partners)
- [ ] Taglines, positioning statements, mission/vision language
- [ ] Marketing plans or campaign briefs
- [ ] Brand guidelines (logo, color, typography, voice/tone)
- [ ] Advertising creative (digital, print, video, radio, OOH)
- [ ] Social media strategy or direction
- [ ] Customer portal screenshots or app interface
- [ ] Educational content (onboarding guides, FAQs)

### 3. Market & Competitive Context
- [ ] Primary direct competitors identified
- [ ] Differentiation from competitors articulated
- [ ] Cross-industry brand inspirations
- [ ] Regulatory/compliance environment documented
- [ ] Market adoption barriers identified

### 4. Performance & Impact Data
- [ ] Key performance indicators (KPIs)
- [ ] Quality/delivery metrics
- [ ] Customer/revenue growth trends
- [ ] Market penetration rates
- [ ] Customer acquisition and conversion data

### 5. Additional Strategic Context
- [ ] Planned product/service expansions
- [ ] Innovation initiatives or R&D priorities
- [ ] Geographic/market expansion plans
- [ ] Target customer segments for growth
- [ ] Partnership/acquisition strategy
- [ ] Long-term vision and goals

**Scoring:** Count completed items. >70% = strong inputs. 50-70% = adequate with gaps to flag. <50% = recommend postponing session or escalating to get materials.

## Section Ownership Model

Each BELIEF deck section is assigned to a WE team member who owns it end-to-end: they review relevant materials, develop probing questions, and facilitate that segment.

| Deck Section | Suggested Role | Materials to Review | Probing Question Focus |
|---|---|---|---|
| Situation Analysis & SWOT | — | Business plan, strategic plan, homework (goals, obstacles) | What's driving the business? Where does leadership feel friction? |
| Competitive Landscape & Differentiation | — | Competitor research, brandscape, homework (differentiators) | What do competitors claim? Where is the client genuinely different? |
| Target Audience Mapping | — | CRM data, testimonials, case studies, homework (audience) | Who is buying and why? Who is the best client — and why do they stay? |
| Vision, Mission & Core Values | — | Leadership bios, company history, homework (vision/aspiration) | What does the future look like? What beliefs are non-negotiable? |
| Brand Positioning | — | Existing messaging, website, sales deck, competitive snapshot | How is the brand perceived vs. how it wants to be perceived? |
| Visual & Creative Identity | Creative Director | Logo files, brand guidelines, past campaigns, visual assets | What works visually? What no longer reflects who the brand is? |
| Communication & Messaging | — | Sales collateral, email campaigns, social content, one-pagers | How does the brand speak today? Is the voice consistent? |

The `/belief intake` command should prompt for section ownership assignments.

## Existing AI Prompt Patterns

These prompts are already in use by the WE Marketing team. The plugin should enhance them, not replace them.

**Homework Synthesis Prompt:**
> "Review the following client homework responses. Identify: (1) the top 3 strategic themes, (2) any contradictions or tensions in how they describe their brand, (3) the 5 most important questions the WE Marketing team should probe in the live session."

**Deck Question Generation Prompt:**
> "Based on this research summary and client homework, generate 3 probing questions for each of the following BELIEF deck sections: Situation Analysis, Competitive Landscape, Target Audience, Vision/Mission, Positioning, and Visual Identity. Questions should challenge assumptions and uncover what the client may not have thought to articulate."

The plugin's `/belief analyze` and `/belief prep` commands should produce outputs that are strictly superior to these prompts — more context-aware, more nuanced, and building on the full knowledge base rather than a single paste.

## Update Conventions

### Reading the Knowledge Base

1. Use `mcp__google-workspace__search_drive_files` to find the knowledge base doc by name
2. Use `mcp__google-workspace__get_doc_as_markdown` to read the full content
3. Parse the structured sections to extract what you need

### Updating the Knowledge Base

1. Read the current state first — never overwrite without reading
2. Use `mcp__google-workspace__modify_doc_text` for targeted section updates
3. Update the "Last Updated" field in Engagement Config with the current date and command name
4. For the Document Inventory table, append new rows — never remove existing ones
5. For synthesis sections (What We Know, Themes, etc.), merge new insights with existing ones — don't replace

### Creating a New Knowledge Base

1. Use `mcp__google-workspace__create_doc` with the client name in the title
2. Populate the Engagement Config section with intake data
3. Leave other sections with their placeholder text — they get populated by subsequent commands

### Incremental Updates

The knowledge base is designed for incremental enrichment:
- `/belief intake` creates the doc and populates Engagement Config
- `/belief analyze` populates Document Inventory, Synthesized Understanding
- `/belief research` populates Research Findings
- `/belief prep` reads everything, writes the playbook as a separate doc
- `/belief synthesize` populates Session Insights
- `/belief distill` populates Brand Foundation Draft
- `/belief learn` reads the full KB, writes to the cross-client KB

Each command should check what already exists and merge rather than overwrite. If a section already has content from a previous run, integrate new findings with existing ones and note what changed.

## Google Drive Conventions

### Folder Structure

Client BELIEF materials live at: `Shared drives/WE Marketing/Clients/[Client Name]/BELIEF/`

The `/belief intake` command creates this folder if it doesn't exist and populates it with:
- `BELIEF Knowledge Base — [Client Name]` (Google Doc)
- Copy of `BELIEF Session Template Slides` (from `WE BELIEF/`)
- Copy of `WE Discovery Homework Template` (from `WE BELIEF/`)

### Finding Files

- Use `search_drive_files` with `includeSharedDrives=true` to find files by name
- Use `list_drive_items` to enumerate folder contents
- For PDFs and DOCX that can't be read via the MCP API, check the local Drive mount at `~/Library/CloudStorage/GoogleDrive-mike@wassonenterprise.com/`

### File Naming

- Knowledge base: `BELIEF Knowledge Base — [Client Name]`
- Playbook: `Facilitator's Playbook — [Client Name]`
- Brand foundation: `Brand Foundation Draft — [Client Name]`
- Standardize folder name as `BELIEF/` (not `B.E.L.I.E.F./`)
