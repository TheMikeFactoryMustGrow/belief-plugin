# Hard-rule register — belief-plugin

**Fitness metric:** a BELIEF engagement moves through its lifecycle
(intake → analyze/research → prep → synthesize → distill → learn) with every
client artifact in the client's own Drive structure and installed clients
always seeing the version they were shipped.

One row per hard rule: id / requirement / named author / one-sentence why /
enforcement. Docs cite IDs; they do not restate the register. Rows accumulate
only through authored PRs. Sources: version-guard workflow provenance
(RCA 2026-08-22), plugin layout, fleet rulings.

| ID | Requirement | Author | Why | Enforcement |
| --- | --- | --- | --- | --- |
| R-VER-01 | Any change under `plugins/belief/` bumps `plugins/belief/.claude-plugin/plugin.json` in the same PR | Mike (RCA 2026-08-22, version-increments-missed; version-guard port) | An unbumped change lands on GitHub but never reaches installed clients | `.github/workflows/version-guard.yml` |
| R-DATA-01 | Client engagement content lives in the client's Google Drive structure — never committed to this repo | Mike (plugin design; CONNECTORS.md integration model) | The repo is public methodology; client brand-discovery material is confidential | Review |
| R-PR-01 | Draft = still working; ready-for-review = the done-signal, flipped by the authoring session when Accept-if passes | Mike (submit-discipline ruling 2026-08-23) | Verified work sitting in draft stalls the merge loop | Review; PR template |
| R-REG-01 | This register stays structurally lintable: 5 non-empty cells per row, `R-XXX-NN` IDs, no duplicates, fitness metric present | Mike (why-first standard adoption, fleet rollout 2026-08-23) | An unlintable register silently stops being the source of truth | `.github/workflows/register-lint.yml` |
