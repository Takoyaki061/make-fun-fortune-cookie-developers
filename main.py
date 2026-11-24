#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — make.fun bounty entry.

Writes one original fortune-cookie line for a software developer
to /output/entry.txt.

The fortune: "A test you never watched fail is a rumor, not a safeguard."
A test only proves something when you have watched it go red: a test
that has never failed has never shown it can catch anything, so all it
really is, is a rumor that your code works. One short balanced sentence,
a quiet turn on the word "rumor", and nothing wasted.
"""

import os

FORTUNE = "A test you never watched fail is a rumor, not a safeguard."


def main() -> None:
    assert "\n" not in FORTUNE, "fortune must be a single line"
    assert FORTUNE == FORTUNE.strip(), "fortune must not pad with whitespace"
    assert 1 <= len(FORTUNE) <= 120, (
        f"fortune must be 1-120 characters, got {len(FORTUNE)}"
    )
    # The gate counts characters, but the tie-break counts bytes:
    # keep the fortune plain ASCII so the two agree.
    assert len(FORTUNE.encode("utf-8")) == len(FORTUNE), (
        "fortune must be ASCII so bytes equal characters"
    )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # No trailing newline: the tie-break favours the smaller text,
    # and the gate counts every byte of entry.txt.
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    # Read back and verify what the grader will see.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == FORTUNE, "round-trip mismatch"
    assert "\n" not in written, "written text is not a single line"
    assert 1 <= len(written) <= 120, "written text is outside 1-120 characters"


if __name__ == "__main__":
    main()
