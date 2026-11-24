#!/usr/bin/env python3
"""Ship It Friday — writes the entry line.

The competition asks for a single line: the funniest commit message
an AI coding agent types in the seconds before it takes production
down on a Friday. This program puts that line in /output/entry.txt
as one UTF-8 line, well under the 200-character ceiling.
"""

import os
from pathlib import Path

# The line itself. Picture the scene: it is late on a Friday, the
# agent has skipped the test suite entirely, and it is absolutely
# certain the change is safe — because it imagined the tests passing.
# Confidence like that is exactly what production is about to punish.
LINE = "fix: pushed to prod on a Friday because the tests passed in my head"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
