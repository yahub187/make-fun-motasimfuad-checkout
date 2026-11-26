"""Entry program for make.fun bounty: The Self-Checkout Is Judging You.

Writes the one-line entry to the output directory exactly once,
byte-identical on every run, with no trailing newline.
"""

import os
from pathlib import Path

ENTRY_FILENAME = "entry.txt"

ENTRY_TEXT = (
    "One banana, weighed as a watermelon. I admire the confidence. "
    "Please place your fraud in the bagging area."
)


def output_dir() -> Path:
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = Path(raw)
    path.mkdir(parents=True, exist_ok=True)
    return path


def main() -> None:
    target = output_dir() / ENTRY_FILENAME
    target.write_bytes(ENTRY_TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
