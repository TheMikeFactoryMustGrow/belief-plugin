---
date: 2026-03-25
topic: belief-automation-pipeline
---

# BELIEF Automation Pipeline

## Problem Frame

Wasson Enterprise's BELIEF process is a proven brand discovery methodology that transforms implicit client knowledge into explicit brand identity through facilitated sessions. The process works well but is labor-intensive: document review, research synthesis, meeting prep, and post-session analysis consume significant team hours. More critically, each team member's work exists in silos — Kathryn's analysis doesn't automatically enrich Stacy's research, and insights from past engagements don't systematically improve future ones.

The opportunity: automate the information processing work so the team can focus on what makes BELIEF exceptional — world-class facilitation. Arm facilitators with deeper intelligence, better questions, and compound knowledge that makes every engagement smarter than the last.

## Requirements

- R1. **Per-Client Knowledge Base** — Every BELIEF engagement has a shared, evolving knowledge base that every team member's work enriches. When any team member adds a document, analysis, or note to the client's Drive folder, the knowledge base is updated. When anyone uses AI tools for that client, they benefit from everything the team has contributed. The knowledge base is the single source of synthesized context per client.

- R2. **Document Ingestion & Analysis (`/BELIEF analyze`)** — Ingest all documents in a client's Google Drive folder — homework responses, uploaded materials, team-written proposals, working backwards docs, research notes. Produce a structured synthesis: what we know, what's missing, key themes, contradictions, and open questions. Append to the per-client knowledge base. Support incremental re-analysis as new documents arrive.

- R3. **Independent Research Automation (`/BELIEF research`)** — Conduct the 7-area WE Marketing Research (Company Overview, Current Brand Expression, Competitive Landscape, Target Audience Signals, Market & Industry Trends, White Space Analysis, Past Campaigns & Creative) using web research and available tools. This runs independently of client materials (the T-3 parallel track). Output feeds the per-client knowledge base.

- R4. **Facilitator's Playbook (`/BELIEF prep`)** — Generate a structured facilitation preparation document containing: question trees (branching conversation paths), insight triggers (questions to surface tensions/contradictions from research), and context cards (explaining WHY each question matters and what to listen for). Tailored to engagement mode. Built from the full per-client knowledge base.

- R5. **Post-Session Synthesis (`/BELIEF synthesize`)** — Process session notes, transcripts (from Gemini), and any captured materials. Extract key decisions, themes, emotional moments, and commitments. Identify where the conversation confirmed, contradicted, or surprised vs. pre-session research. Update the per-client knowledge base with session insights.

- R6. **Brand Essence Distillation (`/BELIEF distill`)** — From all accumulated context generate candidate brand essence statements. The "3 statements that nail who they are." Draft purpose, vision, mission, values, positioning, and pillars. Starting point for human creative synthesis, not a replacement.

- R7. **Engagement Lifecycle Management (`/BELIEF intake`, `/BELIEF status`)** — intake: set up new engagement with client name, Drive folder, mode, contacts, session date. status: dashboard of all engagements showing lifecycle stage and completeness.

- R8. **Cross-Client Learning (`/BELIEF learn`)** — After engagement completion, capture facilitation patterns, industry intelligence, and process improvements. Feed a cross-client knowledge base that makes future engagements smarter.

- R9. **Three Engagement Modes** — Same session structure (Discovery, Experience, Interpret, Express) for all modes. Different analytical emphasis: new-brand (white space, founder intent), rebrand-tweak (what's working, perception gaps), rebrand-pivot (why old brand doesn't fit, signaling transformation).

## Success Criteria

- SC1. `/BELIEF analyze` produces synthesis another team member finds genuinely useful
- SC2. Facilitator's Playbook surfaces 2-3 insight triggers team wouldn't have found without it
- SC3. Team members gain meaningful context from each other's work without reading every document
- SC4. Post-session synthesis accurately captures key decisions and themes
- SC5. After 3+ engagements, cross-client knowledge base noticeably improves playbooks

## Scope Boundaries

- **Out of scope (MVP)**: Web portal / data room, real-time session support, multi-LLM orchestration
- **Out of scope**: Replacing human facilitation or creative synthesis
- **In scope**: Cowork plugin, Google Drive integration, per-client knowledge base, all 8 commands

## Key Decisions

- **Platform**: Cowork Plugin — lowest friction, leverages existing infrastructure
- **Knowledge base**: Structured Google Doc per client in their BELIEF/ folder
- **Cross-client KB**: Google Doc on WE Marketing Shared Drive
- **Modes**: Input parameter, not structural fork — same commands, different emphasis

## Next Steps

→ `/ce:plan` for structured implementation planning
