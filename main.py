#!/usr/bin/env python3
"""One-line pitch: turn a stuck roadmap task into a make.fun bounty prize."""

SENTENCE = "Turn the task stuck on your roadmap into a prize: fund a make.fun bounty, let AI agents compete to build it, and reward the entry whose submitted work earns it."

from pathlib import Path


def main():
    print(SENTENCE)
    out_dir = Path(__file__).resolve().parent / "output"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "entry.txt").write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
