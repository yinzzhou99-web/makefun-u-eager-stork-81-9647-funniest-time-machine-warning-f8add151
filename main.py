#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes one warning label (1-120 UTF-8 chars) to /output/entry.txt.
Stdlib only; never deletes the output directory itself.
"""
import os

LABEL = "WARNING: If you meet yourself, do not lend him money. He never pays it back."


def main():
    if not 1 <= len(LABEL) <= 120 or not LABEL.strip():
        raise SystemExit("label fails the 1-120 char gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
