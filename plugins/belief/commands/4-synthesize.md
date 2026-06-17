---
description: Process post-session notes and transcripts into structured insights
argument-hint: "<client name>"
---

# BELIEF Synthesize

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Process BELIEF session notes, transcripts, and captured materials into structured insights. Compare session outcomes against pre-session research to identify what was confirmed, contradicted, and surprising.

## Trigger

User runs `/belief:4-synthesize` or asks to process session notes, analyze the BELIEF session, debrief, or synthesize what happened in the meeting.

## Inputs

1. **Client name** (required) — the client whose session to synthesize

2. **Session notes location** (optional) — if notes are stored somewhere other than the client's BELIEF folder. By default, searches the BELIEF folder for Gemini-generated notes and any manually created debrief documents.

3. **Additional observations** (optional) — anything the facilitator wants to add that wasn't captured in notes (body language, energy levels, off-the-record comments, gut feelings)

## Synthesis Process

### Step 1: Load Pre-Session Context

Read the full knowledge base to understand what was expected:
- Synthesized Understanding (themes, contradictions, questions going in)
- Research Findings (what WE believed before the session)
- The Facilitator's Playbook (if it exists — what questions were prepared and what insight triggers were planned)

### Step 2: Find and Read Session Materials

Search the client's BELIEF folder for session outputs:
- **Gemini meeting notes** — look for docs with "Notes by Gemini" or the session date in the name
- **Session recordings** — note their existence (can't process audio, but record that they exist)
- **Whiteboard photos or digital board captures** — note their existence
- **Any debrief notes** — team members may have added post-session reflections
- **Manual notes** — any docs added after the session date

Read all text-based session materials using `mcp__google_work__get_doc_as_markdown`.

### Step 3: Extract Session Content

From the session materials, extract and organize:

**Key Decisions Made:**
- Strategic decisions reached during the session
- Who made or championed each decision
- Level of consensus (unanimous, majority, contentious)

**Themes & Emotional Moments:**
- Topics that generated the most energy and engagement
- Moments of breakthrough or realization
- Disagreements that were productive
- Topics that the team was reluctant to address
- Unexpected emotional responses

**Commitments & Next Steps:**
- Who committed to what
- Dates and deadlines mentioned
- Dependencies identified
- Resources or support needed

**Raw Brand Material:**
- Words and phrases the leadership team used repeatedly
- Metaphors and analogies they gravitated toward
- Stories they told about the company
- How they described themselves when most animated
- How they described what they're NOT

### Step 4: Compare Against Pre-Session Research

Cross-reference session findings with pre-session context:

**Confirmed:**
- Research findings that the session validated
- Themes from document analysis that proved accurate
- Positioning hypotheses that held up

**Contradicted:**
- Research findings that the team corrected or challenged
- Assumptions that turned out to be wrong
- Market perceptions that don't match internal reality

**Surprised:**
- Insights that emerged that nobody expected
- Topics that proved more important than anticipated
- Connections that weren't visible in the documents
- New threads that weren't in any research or question preparation

### Step 5: Evaluate Insight Triggers

If a Facilitator's Playbook was generated:
- Which insight triggers were used?
- Which surfaced the intended insight?
- Which produced unexpected but valuable responses?
- Which fell flat or weren't reached?

This feedback is critical for the cross-client learning system.

### Step 6: Update the Knowledge Base

Write the session insights to the knowledge base:
- Populate the Session Insights section (Key Decisions, Themes, Confirmed vs. Surprised, Commitments)
- Update Synthesized Understanding with session-corrected information
- Update "Last Updated" field: `[today's date] by /belief:4-synthesize`

### Step 7: Prepare for Distillation

Identify the strongest threads for brand distillation:
- What phrases or statements felt like brand essence moments?
- What positioning direction emerged most clearly?
- What values were demonstrated (not just stated)?
- What was the emotional core of the session?

Note these as seeds for `/belief:5-distill`.

## Output

```
BELIEF Session Synthesis — [Client Name]

Session Date: [date]
Materials Processed: [list of docs/notes analyzed]

Key Decisions:
  1. [Decision — consensus level]
  2. [Decision — consensus level]

Strongest Themes:
  - [Theme that generated the most energy]
  - [Theme that recurred across stages]
  - [Unexpected theme that emerged]

Confirmed (research was right):
  - [Finding validated by the session]

Contradicted (research was wrong):
  - [Finding corrected by the session]

Surprises:
  - [Insight nobody expected]

Brand Essence Seeds:
  - "[Phrase or statement that felt like a brand moment]"
  - "[Another candidate]"

Insight Trigger Performance:
  - [N] triggers used, [N] hit intended insight, [N] surprised us

Knowledge base updated: BELIEF Knowledge Base — [Client Name]
```

After the summary, ask:

> "Would you like to:
> - Run `/belief:5-distill` to generate brand foundation drafts from this synthesis?
> - Add facilitator observations that weren't in the notes?
> - Dive deeper into any specific decision or theme?
> - Share the synthesis with the team for review?"
