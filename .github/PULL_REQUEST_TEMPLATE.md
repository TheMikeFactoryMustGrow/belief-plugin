<!--
  Agents and humans: fill every section that applies.
  Reviewers evaluate the *reasoning*, not only the diff.
  Hard rules: REQUIREMENTS.md (cite IDs).
-->

## Summary

<!-- 1–3 bullets: what changed in concrete terms. Name the version bump when plugins/belief/ content changed (R-VER-01). -->

-

**Supersedes / relates to:** <!-- PR #s, RCAs, rulings that led here — "none" if standalone -->

## Problem / opportunity



## First principles

<!--
  - Fitness: engagements move through the lifecycle; clients see the shipped version
  - Client material stays in the client's Drive, never this public repo (R-DATA-01)
  - Hard rules live in REQUIREMENTS.md with author + why — docs cite IDs
-->

| Principle | How this PR honors it |
| --- | --- |
| | |

### Alternatives considered

-

### Non-goals

-

## Requirements touched

<!-- REQUIREMENTS.md IDs — "none" if none. Hard-rule changes update the register in the same PR. -->

-

## How to evaluate this update

**Accept if:**

- [ ] version-guard green (bump present iff `plugins/belief/` changed)
- [ ] No client material or credentials in the diff
- [ ] REQUIREMENTS.md updated if any hard rule changed

**Reject / send back if:**

- [ ]

**Manual / scripted checks run:**

```text
# commands run + results
```

## Impact surface

- [ ] Plugin content (`plugins/belief/` — version bump required)
- [ ] Repo docs (README, MIRROR, docs/)
- [ ] Hard-rule register (`REQUIREMENTS.md`)
- [ ] CI / repo hygiene only

**Blast radius (one line):**

## Version

<!-- Single version home: plugins/belief/.claude-plugin/plugin.json (R-VER-01). -->

- [ ] No `plugins/belief/` content changed → **no bump**

## Risk & rollback

**Risk level:** Low / Medium / High

**If this is wrong, rollback is:**

## Test plan

- [ ]

---

### Agent notes (optional)
