# Contributing

- Hard rules live in `REQUIREMENTS.md` (id / requirement / author / why /
  enforcement). Docs cite IDs; they do not restate the register.
- PRs use the why-first template (`.github/PULL_REQUEST_TEMPLATE.md`).
- **Submit discipline (R-PR-01): draft = still working; ready-for-review is
  the done-signal, flipped by the authoring session itself the moment the
  Accept-if checks pass (CI green where CI applies) — never left to a human.**
- Any `plugins/belief/` change bumps the plugin version in the same PR
  (R-VER-01); client material never enters this repo (R-DATA-01).
