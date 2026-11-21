#!/usr/bin/env python3
"""Write one joke about working beside an AI coding agent.

Deterministic, stdlib only, no network. Writes a single line to
/output/entry.txt (creating /output if needed).
"""

import hashlib
import os
from pathlib import Path

JOKE = (
    "My AI coding agent writes code just like me \u2014 "
    "it leaves TODOs and blames the previous developer, who is me."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    text = JOKE + "\n"
    out_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
