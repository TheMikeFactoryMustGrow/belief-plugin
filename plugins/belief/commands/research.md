---
description: Conduct independent 7-area market research for a BELIEF client
argument-hint: "<client name>"
---

# BELIEF Research

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Conduct independent market research across the seven WE Marketing Research areas for a BELIEF engagement. This research runs in parallel with client homework and material collection — it does not depend on client-provided inputs.

## Trigger

User runs `/BELIEF research` or asks to research a client's market, competitors, industry, or audience for a BELIEF engagement.

## Inputs

1. **Client name** (required) — the client to research

2. **Focus areas** (optional) — specific research areas to prioritize or limit to. If not specified, conduct all seven areas.

3. **Additional context** (optional) — any specific competitors, industries, or angles the user wants explored

## Research Process

### Step 1: Load Existing Context

- Read the client's knowledge base doc (`BELIEF Knowledge Base — [Client Name]`)
- Extract the Engagement Config (especially mode and client contacts)
- Check if any Research Findings already exist from a previous run
- Read the Synthesized Understanding section for context from document analysis (if `/BELIEF analyze` has been run)
- This context helps focus research on what matters and avoid duplicating what's already known

### Step 2: Conduct Research

Using the research-methodology skill as a guide, conduct web research across all seven areas. Adjust emphasis based on the engagement mode:

**new-brand**: Extra emphasis on Competitive Landscape, White Space, and Target Audience. Skip Current Brand Expression and Past Campaigns if the company is pre-launch.

**rebrand-tweak**: Extra emphasis on Current Brand Expression and perception gaps. Research how the market has evolved since the brand was last updated.

**rebrand-pivot**: Extra emphasis on Company Overview (what changed), Current Brand Expression (what they're leaving behind), and White Space (where they're going).

For each area, use web search to find:
- Company and competitor websites
- Industry publications and news
- Review sites and community discussions
- Market reports and trend analyses
- Social media presence and positioning

### Step 3: Synthesize Findings

For each research area, produce:
- **Key Findings** (3-5 bullets)
- **Supporting Evidence** (sources, quotes, data)
- **Implications for Brand Discovery** (what this means for the session)
- **Questions This Raises** (new threads to explore)

### Step 4: Identify Cross-Area Insights

After completing individual area research, look across all seven areas for:
- **Positioning opportunities** that emerge from the intersection of competitive gaps and audience needs
- **Contradictions** between how the company presents itself and what the market sees
- **Tensions** that should be explored in the BELIEF session
- **Surprising discoveries** that the client may not be aware of

### Step 5: Update the Knowledge Base

- Write research findings to the Research Findings section of the knowledge base doc
- If research reveals new gaps or contradictions, update the Synthesized Understanding section
- Add any new open questions to the Open Questions section
- Update "Last Updated" field: `[today's date] by /BELIEF research`

If research findings already exist from a previous run, merge new findings with existing ones rather than replacing.

### Step 6: Check Cross-Client Intelligence

- Read the cross-client knowledge base (`BELIEF Cross-Client Learnings`) if it exists
- Check if any past engagements were in a similar industry
- Note relevant cross-client insights that could inform this engagement
- Include relevant cross-client intelligence in the output

## Output

Present a research summary to the user:

```
BELIEF Research Complete — [Client Name]

Mode: [engagement mode]
Research date: [today]

Key Discoveries:
  1. [Most important finding across all areas]
  2. [Second most important finding]
  3. [Third most important finding]

Competitive Positioning Map:
  [Brief description of where the client sits vs. competitors]

White Space Opportunities:
  - [Opportunity 1]
  - [Opportunity 2]

Contradictions & Tensions:
  - [Finding that contradicts client's self-description]
  - [Market reality vs. stated positioning]

Questions for the BELIEF Session:
  - [Research-generated question 1]
  - [Research-generated question 2]

Cross-Client Intelligence:
  [Any relevant patterns from similar past engagements, or "No similar engagements found"]

Knowledge base updated: BELIEF Knowledge Base — [Client Name]
```

After the summary, ask:

> "Would you like to:
> - Dive deeper into any specific research area?
> - Run `/BELIEF prep` to generate the Facilitator's Playbook?
> - Run `/BELIEF analyze` to cross-reference research with client materials?
> - Explore a specific competitor or market angle in more detail?"
