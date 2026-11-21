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
    # Guard: the joke must be a real, non-empty one-liner within the
    # 1-280 code-point limit. len() counts Unicode code points, so this
    # holds for non-ASCII characters (e.g. the em dash) as well.
    if not JOKE.strip():
        raise SystemExit("entry joke is empty or only whitespace")
    if not 1 <= len(JOKE) <= 280:
        raise SystemExit(
            f"entry joke is {len(JOKE)} code points, must be 1-280"
        )
    text = JOKE + "\n"
    out_path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
