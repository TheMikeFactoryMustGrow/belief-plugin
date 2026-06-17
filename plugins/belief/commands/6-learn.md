---
description: Capture cross-client learnings after engagement completion
argument-hint: "<client name>"
---

# BELIEF Learn

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Capture learnings from a completed BELIEF engagement — facilitation patterns, industry intelligence, and process improvements — and feed them into the cross-client knowledge base so future engagements benefit.

## Trigger

User runs `/belief:6-learn` or asks to capture learnings, debrief after an engagement, record what worked, or close out a BELIEF project.

## Inputs

1. **Client name** (required) — the completed engagement to learn from

2. **Facilitator reflections** (encouraged) — the facilitator's perspective on what worked and what didn't. This is the most valuable input — the knowledge base captures facts, but the facilitator experienced the dynamics.

## Learning Capture Process

### Step 1: Load the Full Knowledge Base

Read the complete per-client knowledge base to understand the engagement from start to finish:
- Mode, industry, session date
- What was analyzed and researched
- What the playbook prepared
- What the session revealed
- What the distillation produced

### Step 2: Ask Structured Debrief Questions

Guide the user through a structured reflection. Ask these one at a time:

**Facilitation Quality:**
- "Which questions or insight triggers from the playbook worked best? What made them effective?"
- "Were there any questions that fell flat or produced generic answers?"
- "What questions did you improvise during the session that weren't in the playbook but worked well?"

**Session Dynamics:**
- "Was there a breakthrough moment in the session? What triggered it?"
- "Were there any tensions or disagreements that were particularly productive or unproductive?"
- "Did anything surprise you about how the leadership team responded?"

**Process Reflection:**
- "Was the pre-session preparation adequate? What was missing?"
- "How well did the research match reality? Where was it most and least accurate?"
- "If you ran this engagement again, what would you do differently?"

**Industry Insights:**
- "Did you learn anything about this industry that would help with future clients in the same space?"
- "Were there positioning patterns or audience dynamics specific to this industry?"

### Step 3: Extract Learnings

From the knowledge base content and facilitator reflections, extract:

**Facilitation Patterns:**
- Questions that consistently surface good insights (generalizable across clients)
- Facilitation techniques that worked well (manage dynamics, draw out quiet voices)
- Pitfalls to avoid (question types that don't work, timing issues)
- Improvised approaches worth repeating

**Industry Intelligence:**
- Positioning patterns for this industry
- Typical white space opportunities
- Audience expectations and decision factors
- Competitive landscape dynamics

**Process Improvements:**
- Timeline adjustments that improved outcomes
- Research approaches that produced the best inputs
- Delivery improvements for post-session work
- Tool or template improvements

### Step 4: Update Cross-Client Knowledge Base

Read the cross-client knowledge base (`BELIEF Cross-Client Learnings`) from the WE Marketing shared drive.

Update it with new learnings:
- Add to Facilitation Patterns section (merge with existing patterns)
- Add or update the Industry Intelligence section for this client's industry
- Add to Process Improvements section
- Add a row to the Engagement Log table

Use `mcp__google_work__modify_doc_text` for targeted updates.

### Step 5: Close the Engagement

Update the per-client knowledge base:
- Note that learnings have been captured
- Update "Last Updated" field: `[today's date] by /belief:6-learn`

## Output

```
BELIEF Learnings Captured — [Client Name]

Engagement: [mode] | [industry] | Session [date]

Key Learnings:

Facilitation Patterns:
  - [Pattern that worked well — generalizable to future sessions]
  - [Pattern that didn't work — avoid in future]

Industry Intelligence:
  - [Insight specific to this industry]

Process Improvements:
  - [Improvement to adopt going forward]

Cross-client knowledge base updated.
Engagement logged and closed.

Total engagements in cross-client KB: [N]
Industries covered: [list]
```

After the summary, ask:

> "Would you like to:
> - Review the full cross-client knowledge base?
> - Run `/belief:status` to see the updated engagement dashboard?
> - Set up a new engagement with `/belief:1-intake`?"
