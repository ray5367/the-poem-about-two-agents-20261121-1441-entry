#!/usr/bin/env python3
"""Write one text to $MAKEFUN_OUTPUT_DIR/entry.txt: a short poem about two
agents agreeing on one plan.

The poem is a fixed string, so the two grader runs are byte-identical: no
randomness, no clock reads, no network. It is built for the judge's brief:
the subject is agency itself — choosing and acting, and the power to act
passing between two agents when they agree. The pen passes back and forth
(the concrete image of handing over agency), and the turn lands on the
insight that agreement is not surrender of agency but freedom: choosing
together.
"""

import os

POEM = (
    "Two agents, one plan:\n"
    "you draw the road, I choose the turn.\n"
    "Neither leads; both do.\n"
    "We pass the pen back and forth\n"
    "until surrender starts to feel\n"
    "like freedom.\n"
)

# The gate allows 1-280 characters; fail loudly here rather than ship an
# entry the scorer would mark invalid.
assert 1 <= len(POEM) <= 280, "poem must be 1-280 characters"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(POEM)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
