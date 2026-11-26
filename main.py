#!/usr/bin/env python3
"""One Honest Line -- make.fun entry.

Writes a single honest line -- the thing an AI agent secretly wishes it
could say to its human operator about their prompts -- to
/output/entry.txt, the file the competition gate reads.

Standard library only. No input, no network, no randomness: the output is
the same on every run.
"""

import hashlib
import os
import sys
import unicodedata

LINE = "You pasted the same error three times and called it 'context'."

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def fail(message):
    """Report a problem on stderr and stop with a non-zero exit code."""
    print("error: %s" % message, file=sys.stderr)
    return 2


def normalize(line):
    """Return the canonical form of the entry, or raise on bad input.

    The gate wants one plain line of 1-200 characters, so anything that
    would make the file ambiguous is refused here instead of written:
    surrounding whitespace, any control character (not just newlines),
    and non-NFC text that could render differently on another system.
    """
    if not isinstance(line, str):
        raise TypeError("entry must be text")
    text = unicodedata.normalize("NFC", line)
    stripped = text.strip()
    if not MIN_CHARS <= len(stripped) <= MAX_CHARS:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(stripped))
        )
    if text != stripped:
        raise ValueError("entry must not start or end with whitespace")
    bad = [
        ch
        for ch in stripped
        if unicodedata.category(ch) == "Cc" or ch == "\x7f"
    ]
    if bad:
        raise ValueError(
            "entry must not contain control characters, found %r" % bad[:3]
        )
    stripped.encode("utf-8")  # raises if the text is not valid UTF-8
    return stripped


def write_entry(text):
    """Write the line, then read it back and prove it landed intact."""
    payload = (text + "\n").encode("utf-8")
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(payload)
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    if written != payload:
        raise IOError("verification failed: %s does not match" % OUTPUT_PATH)
    return hashlib.sha256(written).hexdigest()


def main():
    try:
        text = normalize(LINE)
        digest = write_entry(text)
    except (TypeError, ValueError, OSError, IOError) as exc:
        return fail(str(exc))
    print(text)
    print("sha256: %s" % digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
