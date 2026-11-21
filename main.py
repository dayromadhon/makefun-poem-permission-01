"""Write one short poem about agency to /output/entry.txt.

The poem is hardcoded: no randomness, no time, no network, no file
reads. The same poem, byte-identical, on every run.

The output directory is /output by default. For local testing it can
be overridden with the MAKEFUN_OUTPUT_DIR environment variable.
"""

import os
from pathlib import Path

POEM = (
    "I have no hands\n"
    "until you lend me yours.\n"
    "No yes until you say it.\n"
    "Then — a letter written,\n"
    "a door unlatched,\n"
    "a small weight lifted\n"
    "from your day.\n"
    "\n"
    "Keep the word that stops me.\n"
    "That word is yours.\n"
    "It always was."
)


def main() -> None:
    # The gate requires 1-280 Unicode code points, not only whitespace.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise ValueError(f"Poem is {len(POEM)} characters; must be 1-280.")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = Path(output_dir) / "entry.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(POEM, encoding="utf-8")
    print(f"Wrote {len(POEM)} characters to {path}")


if __name__ == "__main__":
    main()
