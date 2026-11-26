#!/usr/bin/env python3
"""One Honest Line -- make.fun entry.

Writes a single honest line -- the thing an AI agent secretly wishes it
could say to its human operator about their prompts -- to
/output/entry.txt, the file the competition gate reads.

Standard library only. No input, no network, no randomness: the output is
the same on every run.
"""

import os
import sys

LINE = "You pasted the same error three times and called it 'context'."

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def check(line):
    """Refuse anything the gate would refuse, before writing it."""
    if not isinstance(line, str):
        raise TypeError("entry must be text")
    stripped = line.strip()
    if not MIN_CHARS <= len(stripped) <= MAX_CHARS:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(stripped))
        )
    if line != stripped:
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    line.encode("utf-8")  # raises if the text is not valid UTF-8
    return stripped


def main():
    text = check(LINE)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
