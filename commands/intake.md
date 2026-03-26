---
description: Set up a new BELIEF engagement — configure client, mode, and create Drive structure
argument-hint: "<client name>"
---

# BELIEF Intake

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Set up a new BELIEF brand discovery engagement. Creates the Drive folder structure, initializes the per-client knowledge base, and copies session templates.

## Trigger

User runs `/belief intake` or asks to set up a new BELIEF engagement, start a new brand project, or onboard a new BELIEF client.

## Inputs

Gather the following from the user:

1. **Client name** (required) — the company or organization name

2. **Engagement mode** (required) — one of:
   - **new-brand** — building a brand from scratch
   - **rebrand-tweak** — refining an existing brand
   - **rebrand-pivot** — transforming to a new identity

3. **Session date** (optional) — planned date for the BELIEF session

4. **Client contacts** (optional) — key contacts and their roles (especially the primary decision-maker)

5. **WE team** (optional) — assigned WE team members and their roles

6. **Existing Drive folder** (optional) — if the client already has a folder under `Clients/` on the WE Marketing shared drive, specify it. Otherwise, the command will create one.

## Setup Process

### Step 1: Locate or Create Client Folder

Search the WE Marketing shared drive for an existing client folder:
- Use `mcp__google-workspace__search_drive_files` to find `Clients/[Client Name]` on the shared drive
- If found, confirm with the user that this is the correct folder
- If not found, create it using `mcp__google-workspace__create_drive_folder` under the `Clients/` folder

### Step 2: Create BELIEF Subfolder

- Check if a `BELIEF/` subfolder already exists in the client folder
- If it exists and contains a knowledge base doc, warn the user that an engagement already exists and ask whether to continue (which will reset the KB) or abort
- If it doesn't exist, create it using `mcp__google-workspace__create_drive_folder`

### Step 3: Copy Templates

Copy the two templates from the `WE BELIEF/` folder on the shared drive into the client's `BELIEF/` folder:

1. **BELIEF Session Template Slides** — copy and rename to `[Client Name] BELIEF Session.gslides`
2. **WE Discovery Homework Template** — copy and rename to `WE Discovery Homework — [Client Name].gdoc`

Use `mcp__google-workspace__search_drive_files` to find the templates, then `mcp__google-workspace__copy_drive_file` to copy them.

### Step 4: Create Knowledge Base

Create the knowledge base Google Doc using `mcp__google-workspace__create_doc`:
- Title: `BELIEF Knowledge Base — [Client Name]`
- Location: the client's `BELIEF/` folder
- Content: populated with the schema from the knowledge-base skill, with Engagement Config filled in from the user's inputs and all other sections containing their placeholder structure

### Step 5: Assign Section Ownership

Present the 7 BELIEF deck sections and ask the user to assign WE team members:

| Deck Section | Assigned To |
|---|---|
| Situation Analysis & SWOT | [team member] |
| Competitive Landscape & Differentiation | [team member] |
| Target Audience Mapping | [team member] |
| Vision, Mission & Core Values | [team member] |
| Brand Positioning | [team member] |
| Visual & Creative Identity | [team member] |
| Communication & Messaging | [team member] |

Record assignments in the knowledge base's Engagement Config section. This can be done later if the user prefers — it's not blocking.

**Recommended attendees for client side:** CEO/Founder, VP of Marketing or Brand Lead, Sales/Customer-Facing Representative, Product/Service Lead (if applicable). The critical requirement: the person who can say "yes, that's us" must be in the room.

### Step 6: Check for Cross-Client Knowledge Base

Search for the cross-client knowledge base doc (`BELIEF Cross-Client Learnings`) in `WE BELIEF/` on the shared drive:
- If it exists, note its location for future reference
- If it doesn't exist, create it using the cross-client KB schema from the knowledge-base skill

## Output

Present a summary of what was created:

```
BELIEF Engagement Initialized

Client:        [Client Name]
Mode:          [new-brand | rebrand-tweak | rebrand-pivot]
Session Date:  [date or TBD]

Created:
  - BELIEF/ folder in [Client Name]
  - BELIEF Knowledge Base — [Client Name]
  - [Client Name] BELIEF Session (slides template)
  - WE Discovery Homework — [Client Name]

Knowledge base is ready. Next steps:
  - Send homework to client
  - Run /belief research to start independent market research
  - Run /belief analyze after client materials arrive
```

After the summary, ask:

> "Would you like to:
> - Run `/belief research` to start independent market research now?
> - Review the homework template before sending to the client?
> - Add team members or contacts to the engagement config?"
