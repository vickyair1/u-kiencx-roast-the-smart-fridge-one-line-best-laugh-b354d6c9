#!/usr/bin/env python3
"""Roast the Smart Fridge: one line roasting the smart fridge.

Writes exactly the line to /output/entry.txt, no trailing newline.
"""

import os

# The roast: the fridge is a snitch about the door but goes silent when its
# own ice maker dies -- loyalty runs one way. Fresh angle, no milk-ordering
# cliche, and it names a real behaviour of the thing.
LINE = "My smart fridge snitches 'door left open' when I grab a midnight snack, but when its ice maker died it stayed silent for a month — loyalty runs one way here."


MAX_CHARS = 160


def normalize_line(line: str) -> str:
    """Collapse accidental double spaces and strip edge whitespace.

    Defensive formatting only: the sealed line is already clean, so this
    returns it byte-identical.
    """
    return " ".join(line.split())


def get_line() -> str:
    """Return the entry line, normalized."""
    return normalize_line(LINE)


def output_dir() -> str:
    """Output directory, overridable via MAKEFUN_OUTPUT_DIR."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(line: str) -> None:
    """Write the line to <output_dir>/entry.txt, no trailing newline."""
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line)


def validate_line(line: str) -> None:
    """Gate: the sealed scorer needs 1-160 chars, UTF-8, not only
    whitespace, exactly one clean line. Fail loudly here rather than ship
    an invalid entry."""
    assert 1 <= len(line) <= MAX_CHARS, "line must be 1-160 characters"
    line.encode("utf-8")
    assert line.strip() == line and "\n" not in line and "\r" not in line, \
        "must be one clean line"


def main() -> None:
    line = get_line()
    validate_line(line)
    write_entry(line)


if __name__ == "__main__":
    main()
