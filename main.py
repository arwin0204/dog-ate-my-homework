#!/usr/bin/env python3
"""Writes one funny dog excuse to /output/entry.txt.

Deterministic: the same line is written on every run.
"""

import os
import sys

ENTRY = (
    "The homework whispered 'eat me' in pencil. "
    "I don't argue with talking food — and it was the smartest thing "
    "I ate all week."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
