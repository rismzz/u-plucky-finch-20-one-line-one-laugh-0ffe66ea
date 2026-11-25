#!/usr/bin/env python3
"""One Line, One Laugh — one line, one laugh. Writes the line verbatim to
entry.txt.

The joke is the gap between the request and the delivery: asked for a
one-line summary, the agent returns a 40-page essay — and titles it
"In Summary", as if the title alone fulfils the brief. Confidence plus
total failure to follow instructions is the agent's whole personality.
The title in quotes is the punchline; the essay is just the setup.
"""

import os
from pathlib import Path

LINE = "I asked my agent for a one-line summary and it handed me a 40-page essay titled 'In Summary'."

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
