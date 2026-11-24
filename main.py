#!/usr/bin/env python3
"""Two Days of Quiet Dread - v1 (original).

Writes one code-review comment to /output/entry.txt: a single line of at
most 140 characters that approves a pull request while carrying quiet
existential dread.

The line (63 characters, no trailing newline):
    Approved. No one owns this file anymore, so I suppose I do now.

Why this line: the dread is not in the code, which is fine, but in what
the approval does to the reviewer. Approving an orphaned file is a quiet
transfer of ownership: nobody maintained it before, and from the click
onward, somebody does - the approver. The joke lands on "I suppose",
the smallest possible surrender, and the dread stays flat and
understated, the way a tired engineer would actually write it just
before clicking approve.
"""

import os

ENTRY = "Approved. No one owns this file anymore, so I suppose I do now."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Coordinator fix 24 Nov: VM umask 0007 leaves entry.txt 660; the
    # grader must be able to read it, so force the 0644 the other
    # text entries in this run already use.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
