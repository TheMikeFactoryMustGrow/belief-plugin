# BELIEF Plugin — System Flow

## End-to-End Workflow

```mermaid
flowchart LR
    subgraph PRE["Pre-Session"]
        intake["/belief intake"]
        analyze["/belief analyze"]
        research["/belief research"]
        prep["/belief prep"]
    end

    subgraph SESSION["Live Session"]
        live["BELIEF Session\n(Human-Led)"]
    end

    subgraph POST["Post-Session"]
        synthesize["/belief synthesize"]
        distill["/belief distill"]
        learn["/belief learn"]
    end

    intake --> analyze
    intake --> research
    analyze --> prep
    research --> prep
    prep --> live
    live --> synthesize
    synthesize --> distill
    distill --> learn

    style intake fill:#4A90D9,color:#fff
    style analyze fill:#4A90D9,color:#fff
    style research fill:#4A90D9,color:#fff
    style prep fill:#E8833A,color:#fff
    style live fill:#7B68EE,color:#fff
    style synthesize fill:#4A90D9,color:#fff
    style distill fill:#4A90D9,color:#fff
    style learn fill:#50C878,color:#fff
```

## Knowledge Base Architecture

```mermaid
flowchart TB
    subgraph COMMANDS["Commands (What You Run)"]
        intake["/belief intake"]
        analyze["/belief analyze"]
        research["/belief research"]
        prep["/belief prep"]
        synthesize["/belief synthesize"]
        distill["/belief distill"]
        status["/belief status"]
        learn["/belief learn"]
    end

    subgraph KB["Knowledge Bases (Where Data Lives)"]
        clientKB[("Per-Client KB\n(Google Doc per client)")]
        crossKB[("Cross-Client KB\n(Shared Drive)")]
    end

    subgraph SKILLS["Skills (How Commands Think)"]
        kb_skill["knowledge-base\nSchema & conventions"]
        brand["brand-discovery\nBELIEF methodology"]
        questions["question-generation\nSocratic method"]
        research_skill["research-methodology\n7-area framework"]
    end

    %% Commands writing to Client KB
    intake -->|creates| clientKB
    analyze -->|updates| clientKB
    research -->|updates| clientKB
    synthesize -->|updates| clientKB
    distill -->|updates| clientKB

    %% Commands reading from Client KB
    clientKB -->|reads| analyze
    clientKB -->|reads| research
    clientKB -->|reads| prep
    clientKB -->|reads| synthesize
    clientKB -->|reads| distill
    clientKB -->|reads| learn

    %% Cross-client KB flows
    learn -->|writes| crossKB
    crossKB -->|reads| prep
    status -->|scans| clientKB

    %% Skills informing commands
    kb_skill -.->|informs| intake
    kb_skill -.->|informs| analyze
    research_skill -.->|informs| research
    brand -.->|informs| prep
    brand -.->|informs| distill
    questions -.->|informs| prep

    style clientKB fill:#FFD700,color:#000
    style crossKB fill:#FFD700,color:#000
    style kb_skill fill:#E8E8E8,color:#000
    style brand fill:#E8E8E8,color:#000
    style questions fill:#E8E8E8,color:#000
    style research_skill fill:#E8E8E8,color:#000
```

## Compound Learning Loops

```mermaid
flowchart TB
    subgraph LOOP1["Per-Client Loop (Within One Engagement)"]
        direction LR
        kathryn["Kathryn runs\n/belief analyze"] --> kb1["Client KB\nenriched"]
        kb1 --> stacy["Stacy runs\n/belief research"]
        stacy --> kb2["Client KB\ndeeper"]
        kb2 --> prep1["Anyone runs\n/belief prep"]
        prep1 --> playbook["Playbook reflects\neveryone's work"]
    end

    subgraph LOOP2["Cross-Client Loop (Across Engagements)"]
        direction LR
        eng1["Engagement 1\n/belief learn"] --> xkb["Cross-Client KB"]
        eng2["Engagement 2\n/belief learn"] --> xkb
        eng3["Engagement 3\n/belief learn"] --> xkb
        xkb --> future["/belief prep\nfor new clients"]
        future --> better["Better playbooks\nover time"]
    end

    LOOP1 --> LOOP2

    style kb1 fill:#FFD700,color:#000
    style kb2 fill:#FFD700,color:#000
    style xkb fill:#FFD700,color:#000
    style playbook fill:#E8833A,color:#fff
    style better fill:#50C878,color:#fff
```

## Three Engagement Modes

```mermaid
flowchart LR
    mode{"Engagement\nMode"}
    mode -->|new-brand| nb["White space focus\nFounder intent\nNo existing brand"]
    mode -->|rebrand-tweak| rt["Perception gaps\nWhat's working\nEvolution"]
    mode -->|rebrand-pivot| rp["Why old brand fails\nTransformation signal\nNew identity"]

    nb --> same["Same Session Structure\nDiscovery → Experience\n→ Interpret → Express"]
    rt --> same
    rp --> same

    same --> output["Brand Foundation\nEssence Statements\nPlaybook"]

    style mode fill:#7B68EE,color:#fff
    style same fill:#4A90D9,color:#fff
    style output fill:#50C878,color:#fff
```

## Command Quick Reference

| Command | Sequence | Reads From | Writes To | Key Skill |
|---|---|---|---|---|
| `/belief intake` | 1. Setup | — | Client KB (creates) | knowledge-base |
| `/belief analyze` | 2. Pre-session | Client KB, Drive folder | Client KB | knowledge-base |
| `/belief research` | 2. Pre-session | Client KB, Web | Client KB | research-methodology |
| `/belief prep` | 3. Pre-session | Client KB, Cross-Client KB | Playbook (new doc) | question-generation, brand-discovery |
| `/belief synthesize` | 4. Post-session | Client KB, Session notes | Client KB | brand-discovery |
| `/belief distill` | 5. Post-session | Client KB (full) | Client KB, Foundation doc | brand-discovery |
| `/belief status` | Anytime | All Client KBs | Console output | knowledge-base |
| `/belief learn` | 6. Close-out | Client KB (full) | Cross-Client KB | brand-discovery |
