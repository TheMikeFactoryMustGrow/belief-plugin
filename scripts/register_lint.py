"""Structural lint for the REQUIREMENTS.md hard-rule register (R-REG-01)."""
import re
import sys
from pathlib import Path


def check(cond: bool, msg: str) -> None:
    if not cond:
        sys.exit(f"register lint: {msg}")


def main() -> None:
    text = Path("REQUIREMENTS.md").read_text(encoding="utf-8")
    check("**Fitness metric:**" in text or "## Fitness metric" in text,
          "register missing fitness metric")
    body = []
    for ln in (ln.strip() for ln in text.splitlines()):
        # GFM renders rows without a leading pipe too — normalize those
        if re.match(r"^R-[A-Z]+-\d+\s*\|", ln):
            ln = "|" + ln
        if ln.startswith("|"):
            body.append(ln if ln.endswith("|") else ln + "|")
    rows = [s for s in body
            if not re.match(r"^\|\s*ID\s*\|", s)
            and not re.match(r"^\|(\s*:?-{3,}:?\s*\|)+$", s)]
    check(bool(rows), "register has no rule rows (| R-XXX-NN | ...)")
    ids = []
    for row in rows:
        check(row.endswith("|"), f"row must end with |: {row}")
        cells = [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", row[1:-1])]
        check(len(cells) == 5 and all(cells), f"row needs 5 non-empty cells: {row}")
        check(bool(re.fullmatch(r"R-[A-Z]+-\d+", cells[0])),
              f"malformed rule ID {cells[0]!r}: {row}")
        ids.append(cells[0])
    check(len(ids) == len(set(ids)), "duplicate rule IDs")
    print(f"register OK: {len(ids)} rules")


if __name__ == "__main__":
    main()
