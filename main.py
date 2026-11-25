"""The Houseplant Out-of-Office.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Stdlib only. Deterministic: the text is fixed.
"""

import os

ENTRY = (
    "Out of office until someone waters me. "
    "My last drink was in March, and honestly, "
    "I've stopped believing in humans."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = ENTRY
    if not (1 <= len(text) <= 120):
        raise ValueError(f"entry is {len(text)} chars, must be 1-120")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
