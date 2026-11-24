#!/usr/bin/env python3
"""Two Lines to Your Past Self entry.

Writes two lines to /output/entry.txt (UTF-8, 266 characters, inside
the 1-280 gate). Deterministic, standard library only, no network,
no environment reads.

Line 1 warns the past self about one specific moment: handing the
car keys to my brother at six on a rainy Friday evening. Line 2
traces the cause and effect: he drove into the guardrail before
midnight, and every family dinner since has had one empty chair and
one sentence nobody finishes. The moment is concrete (a time, a
place, an object, a sentence said out loud); the second line shows
what changed because of it instead of restating the warning. The
em dash in line 1 joins the warning to the exact words to say, so
the line stays one sentence.
"""

import os

TEXT = (
    "Don't hand your brother the car keys at six on that rainy Friday "
    "evening \u2014 tell him the brakes are shot and keep them in your pocket.\n"
    "He drove into the guardrail before midnight, and every family "
    "dinner since has had one empty chair and one sentence nobody finishes."
)


def main() -> None:
    # The gate requires 1-280 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(TEXT) <= 280, "entry must be 1-280 characters"
    assert TEXT.strip() == TEXT, "entry must not start or end with whitespace"
    assert TEXT.count("\n") == 1, "entry must be exactly two lines"
    lines = TEXT.split("\n")
    assert all(line.strip() for line in lines), "neither line may be blank"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
