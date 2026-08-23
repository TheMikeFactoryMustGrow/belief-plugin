"""Structural lint for the REQUIREMENTS.md hard-rule register (R-REG-01)."""
import re
from pathlib import Path


def main() -> None:
    t = Path("REQUIREMENTS.md").read_text(encoding="utf-8")
    assert "**Fitness metric:**" in t, "register missing fitness metric line"
    body = [s for s in (l.strip() for l in t.splitlines()) if s.startswith("|")]
    rows = [s for s in body
            if not re.match(r"^\|\s*ID\s*\|", s) and not re.match(r"^\|[\s|:-]+\|?$", s)]
    assert rows, "register has no rule rows (| R-XXX-NN | ...)"
    ids = []
    for l in rows:
        assert l.endswith("|"), f"row must end with |: {l}"
        cells = [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", l[1:-1])]
        assert len(cells) == 5 and all(cells), f"row needs 5 non-empty cells: {l}"
        assert re.fullmatch(r"R-[A-Z]+-\d+", cells[0]), f"malformed rule ID {cells[0]!r}: {l}"
        ids.append(cells[0])
    assert len(ids) == len(set(ids)), "duplicate rule IDs"
    print(f"register OK: {len(ids)} rules")


if __name__ == "__main__":
    main()
