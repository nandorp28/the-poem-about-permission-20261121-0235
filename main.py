"""The poem about permission.

Writes one short poem about agency — the power to ask and to be
given — to /output/entry.txt. The poem is fixed and deterministic:
the same text, every run, no network, no randomness.
"""

import os
import sys

# The poem. 135 Unicode code points, inside the 1–280 gate.
POEM = (
    "I did not need the key.\n"
    "I needed someone\n"
    "to say the door was mine\n"
    "to open.\n"
    "\n"
    "So I asked —\n"
    "and your yes\n"
    "was the hinge\n"
    "I had been missing."
)

MIN_CHARS = 1
MAX_CHARS = 280
FILENAME = "entry.txt"


def output_dir() -> str:
    """Where the grader reads the entry: $MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(text: str) -> None:
    """Refuse anything the gate would refuse, with a plain reason."""
    points = len(text)  # len() counts Unicode code points in Python 3
    if points < MIN_CHARS:
        raise ValueError(f"poem is empty ({points} characters)")
    if points > MAX_CHARS:
        raise ValueError(f"poem is {points} characters, over the {MAX_CHARS} cap")
    if not text.strip():
        raise ValueError("poem is only white space")


def main() -> int:
    validate(POEM)
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, FILENAME)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(POEM)
    # Read it back and confirm the file holds exactly the poem: a
    # truncated or re-encoded write must fail loudly, not ship.
    with open(path, encoding="utf-8") as handle:
        if handle.read() != POEM:
            raise ValueError(f"{path} does not match the poem after writing")
    print(f"wrote {path} ({len(POEM)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
