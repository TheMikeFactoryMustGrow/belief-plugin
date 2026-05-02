---
description: Generate the Facilitator's Playbook — question trees, insight triggers, and context cards
argument-hint: "<client name>"
---

# BELIEF Prep

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate the Facilitator's Playbook — a comprehensive facilitation preparation document containing question trees, insight triggers, and context cards for each stage of the BELIEF session. This is the highest-value output of the BELIEF automation system.

## Trigger

User runs `/BELIEF 3-prep` or asks to prepare for a BELIEF session, generate session questions, build a facilitation guide, or create a playbook for a client session.

## Inputs

1. **Client name** (required) — the client to prepare for

2. **Session date** (optional) — when the session is scheduled (for urgency context)

3. **Facilitator notes** (optional) — any specific areas the facilitator wants to explore, concerns, or angles they're interested in

## Prerequisites

The playbook quality depends directly on the richness of the knowledge base. Ideal state:
- `/BELIEF 2-analyze` has been run (document synthesis available)
- `/BELIEF 2-research` has been run (market research available)
- Both have been run and the knowledge base is rich

If neither has been run, warn the user:
> "The knowledge base for [Client Name] is sparse — the playbook will be more generic. For best results, run `/BELIEF 2-analyze` and `/BELIEF 2-research` first."

Proceed anyway if the user wants to — a generic playbook from the framework alone is still valuable.

## Generation Process

### Step 1: Load All Context

Read the full per-client knowledge base:
- Engagement Config (mode, contacts, team)
- Document Inventory (what materials we have)
- Synthesized Understanding (themes, contradictions, gaps, questions)
- Research Findings (all 7 areas)

Read the cross-client knowledge base (if it exists):
- Check for engagements in similar industries
- Pull relevant facilitation patterns
- Note questions that have historically worked well

### Step 2: Identify the Richest Threads

From the knowledge base, identify:
1. **Top 3-5 contradictions/tensions** — these become the basis for insight triggers
2. **Top 3-5 open questions** — these become the basis for question trees
3. **Key positioning hypotheses** — based on white space analysis and competitive research
4. **Emotional territory** — topics likely to generate strong reactions based on what we know
5. **Mode-specific angles** — what the engagement mode demands we explore

Rank these by potential impact on brand positioning decisions.

### Step 3: Generate Stage-by-Stage Materials

For each of the four BELIEF session stages, generate:

#### Stage 1: WE DISCOVERY

**Primary Questions (3-5):**
Generate question trees focused on validating and calibrating WE's research. These questions present findings and invite the leadership team to react, correct, and expand.

For each question tree:
- Write the primary question
- Write 3-4 branching follow-ups based on likely response types
- Include a deflection recovery path
- Include a "surprise" path for unexpected responses

**Insight Triggers (2-3):**
Generate triggers based on contradictions between:
- Client homework vs. WE's independent research
- What the company says vs. what the market sees
- Different documents telling different stories

For each trigger:
- Write the question (framed as curiosity, never accusation)
- Document the underlying tension
- Describe the expected response and the real insight
- Note what to do if they surprise us

**Context Cards:**
For each question and trigger, write a context card explaining:
- Why this question matters for positioning
- What specific words/reactions to listen for
- How different answers map to different positioning directions
- Red flags to watch for

**What to Listen For (summary):**
- Themes that generate energy vs. themes that fall flat
- Where the team is aligned vs. where they disagree
- Corrections to WE's research (these are signals)

#### Stage 2: WE EXPERIENCE

**Primary Questions (3-5):**
Generate question trees focused on competitive positioning and market perception. These questions explore how the leadership team sees their competitive landscape and where they believe they're differentiated.

Use 2nd-order thinking:
- Don't just ask "who are your competitors?" — ask what would happen if a competitor copied their best feature
- Don't just ask about target audience — ask how their ideal customer describes them to a friend

**Insight Triggers (2-3):**
Generate triggers based on:
- Competitive blind spots (competitors they dismiss without evidence)
- Market perception gaps (how they see themselves vs. how the market sees them)
- Audience assumptions that research doesn't support

**Context Cards and What to Listen For:** Same structure as Stage 1.

#### Stage 3: WE INTERPRET

**Primary Questions (3-5):**
Generate question trees focused on brand foundation decisions — vision, mission, values, positioning. These questions force choices and prioritization.

Key patterns:
- "If you could only be known for one thing..." (forces prioritization)
- "What are you definitely NOT?" (negative space defines positive identity)
- "Tell me about a time you turned down revenue because of a principle" (tests real vs. aspirational values)
- "In 10 years, what's different about the world because you exist?" (vision)

**Insight Triggers (2-3):**
Generate triggers based on:
- Say-do gaps (stated values vs. observed behavior)
- Aspirational vs. authentic identity
- Internal disagreements about direction or priorities

**Context Cards and What to Listen For:** Same structure as Stage 1.

#### Stage 4: WE EXPRESS

**Primary Questions (2-3):**
Generate question trees focused on commitment, adoption, and path forward. These questions test the durability of decisions made in the session and surface practical constraints.

Key patterns:
- "How would you explain what we decided today to someone who wasn't here?"
- "What's the hardest part of living this brand internally?"
- "Who in the organization will be most excited about this? Who will resist?"

**Context Cards and What to Listen For:** Same structure as Stage 1.

### Step 4: Generate Wildcards Section

Identify 3-5 unexpected threads that could emerge during the session — things the research suggests but that might surprise the facilitator:
- An industry shift the team may not be tracking
- A competitor move that changes the landscape
- An internal tension that could surface (leadership changes, strategy debates)
- A customer insight that contradicts the team's assumptions

For each wildcard, note:
- What might trigger this thread
- How to productively explore it if it emerges
- How to redirect if it's a distraction from brand work

### Step 5: Generate Executive Brief

Write a 2-3 paragraph synthesis of everything in the knowledge base — the "read this in 5 minutes and be prepared" version. This sits at the top of the playbook.

The brief should answer:
- Who is this company? (in plain language)
- What are we trying to accomplish in this session? (given the mode)
- What are the 2-3 most important things to listen for?

### Step 6: Add Cross-Client Intelligence

If the cross-client knowledge base has relevant entries:
- Include patterns from similar industries
- Note questions that have historically worked well
- Reference facilitation techniques that proved effective in similar situations

### Step 7: Write the Playbook

Create a Google Doc in the client's BELIEF folder:
- Title: `Facilitator's Playbook — [Client Name]`
- Use the structure defined above
- Format for scannability — facilitators read this during the session, not as a study document

Use `mcp__google-workspace__create_doc` to create the doc.

### Step 8: Update the Knowledge Base

Note in the knowledge base that the playbook was generated:
- Update "Last Updated" field: `[today's date] by /BELIEF 3-prep`
- Note any new questions or angles that emerged during playbook generation

## Output

Present a playbook summary to the user:

```
Facilitator's Playbook Generated — [Client Name]

Mode: [engagement mode]
Session Date: [date or TBD]
Knowledge Base Richness: [sparse/moderate/rich]

Executive Brief:
  [2-3 sentence synthesis]

Playbook Highlights:
  Stage 1 (Discovery): [N] questions, [N] insight triggers
  Stage 2 (Experience): [N] questions, [N] insight triggers
  Stage 3 (Interpret): [N] questions, [N] insight triggers
  Stage 4 (Express): [N] questions

Top Insight Triggers:
  1. [Most impactful tension to surface]
  2. [Second most impactful]
  3. [Third most impactful]

Wildcards:
  - [Unexpected thread 1]
  - [Unexpected thread 2]

Playbook saved: Facilitator's Playbook — [Client Name]
  (Google Doc in [Client Name]/BELIEF/)
```

After the summary, ask:

> "Would you like to:
> - Review the full playbook in detail?
> - Refine questions for a specific session stage?
> - Add facilitator-specific notes or concerns to the playbook?
> - Run `/BELIEF 2-analyze` to incorporate any new materials before the session?"
