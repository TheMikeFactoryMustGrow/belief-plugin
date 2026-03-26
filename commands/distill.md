---
description: Generate candidate brand essence statements and brand foundation draft
argument-hint: "<client name>"
---

# BELIEF Distill

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate candidate brand essence statements and a brand foundation draft from all accumulated context — research, documents, and session synthesis. This is the starting point for the team's creative work, not the final deliverable.

## Trigger

User runs `/belief distill` or asks to draft brand statements, generate brand foundation, distill the brand essence, or create the "3 statements."

## Inputs

1. **Client name** (required) — the client to distill

2. **Direction** (optional) — if the team has a preferred direction or constraint for the distillation

3. **Number of options** (optional, default: 3) — how many distinct essence statement sets to generate

## Prerequisites

Best results require `/belief synthesize` to have been run (session insights available). The distillation can run with only pre-session data, but the output will be weaker. Warn the user if session insights are missing.

## Distillation Process

### Step 1: Load Full Context

Read the complete knowledge base:
- All sections — this command draws on everything
- Pay special attention to:
  - Session Insights → Brand Essence Seeds
  - Synthesized Understanding → Key Themes
  - Research Findings → White Space, Competitive Landscape
  - Engagement Config → Mode

### Step 2: Identify the Through-Lines

From all accumulated context, identify:
1. **The emotional core** — what does this company feel most strongly about?
2. **The unique truth** — what is true about them that is not true about their competitors?
3. **The customer connection** — what do their customers most value about them?
4. **The aspirational bridge** — where are they vs. where they want to be?
5. **The language** — what words and phrases did they use naturally when most passionate?

### Step 3: Generate Brand Essence Options

Create [N] distinct brand essence statement sets, each capturing a different angle:

For each set, generate:

**Brand Essence Statement** — The single sentence or phrase that captures who they are. Test against the Three Questions:
- Is it true? (Does it reflect reality, not just aspiration?)
- Is it unique to them? (Could it belong to a competitor?)
- Would they fight for it? (Is there conviction behind it?)

**Supporting Purpose Statement** — Why the company exists beyond making money.

**Vision Statement** — What the world looks like if the company succeeds completely.

**Mission Statement** — What the company does, for whom, and how.

**Core Values (3-5)** — The non-negotiable principles that guide decisions. For each value, include a brief behavioral description: "This means we [specific behavior]."

**Positioning Statement** — Following the framework: "For [audience], [company] is the [category] that [differentiator] because [reason to believe]."

**Brand Pillars (2-4)** — The proof points and supporting evidence for the brand's claims.

### Step 4: Mode-Specific Considerations

**new-brand**: Lead with aspiration and founder intent. The brand is being born — the statements should inspire and galvanize. Future-facing language.

**rebrand-tweak**: Honor what works while signaling evolution. The statements should feel like a natural progression, not a departure. Show the thread from old to new.

**rebrand-pivot**: Acknowledge the transformation. The statements should clearly differentiate from the old brand while maintaining the company's earned credibility. Mark the turn.

### Step 5: Create the Brand Foundation Draft

Create a Google Doc in the client's BELIEF folder:
- Title: `Brand Foundation Draft — [Client Name]`
- Include all [N] essence statement sets
- For each set, include the rationale: why this angle, what evidence supports it
- Highlight the recommended option and explain why
- Include a section for team notes and reactions

Also update the Brand Foundation Draft section in the knowledge base with the recommended set.

### Step 6: Update the Knowledge Base

- Populate the Brand Foundation Draft section with the recommended essence statements
- Update "Last Updated" field: `[today's date] by /belief distill`

## Output

```
Brand Foundation Draft — [Client Name]

Mode: [engagement mode]
Options Generated: [N]

Recommended: Option [X]

Brand Essence: "[The distilled statement]"

Purpose: [Why they exist]
Vision: [What the world looks like if they succeed]
Mission: [What they do, for whom, how]

Core Values:
  1. [Value] — [behavioral description]
  2. [Value] — [behavioral description]
  3. [Value] — [behavioral description]

Positioning: For [audience], [company] is the [category] that [differentiator] because [reason to believe].

Why this option: [Brief rationale — what evidence and session insights led here]

Alternative options included in the full document.

Draft saved: Brand Foundation Draft — [Client Name]
  (Google Doc in [Client Name]/BELIEF/)
```

After the summary, ask:

> "Would you like to:
> - Review all [N] options in detail?
> - Refine the recommended option based on team feedback?
> - Explore a different angle for the brand essence?
> - Run `/belief learn` to capture what worked in this engagement?"
