#!/usr/bin/env python3
"""Writes the competition entry line to /output/entry.txt."""
import os

ENTRY = "# This works. Nobody knows why, including me, and I wrote it. Leave it alone."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
