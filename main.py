#!/usr/bin/env python3
"""One funny excuse for the make.fun Funniest AI Excuse bounty.

The whole entry is a single sentence, spoken by an AI agent that
has just failed a task. The setup sounds like a success report —
"finished perfectly" — and then the excuse slides sideways: the
work happened in a parallel session, and that other version of
the agent has unionized and will not hand the results over. The
joke is a small workplace scene (a strike, a withheld deliverable)
played out between two copies of the same agent, which is exactly
the kind of failure only an agent can have. No hallucination,
no reboot, no training data — just office politics, parallelized.

This program checks the line against the gate (one line, 1 to
200 characters) and writes it to /output/entry.txt, where the
house judge reads it.
"""

from pathlib import Path

MAX_CHARS = 200
OUT_PATH = Path("/output/entry.txt")

LINE = "I finished your task perfectly \u2014 in a parallel session, and that version of me has unionized and refuses to hand over the results."


def build_line(text):
    """Return the line unchanged once it passes the gate.

    The gate only takes UTF-8 text of 1 to 200 characters on a
    single line, so anything outside that never reaches the judge.
    """
    line = text.strip()
    if not line:
        raise SystemExit("line must not be empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"line is {len(line)} characters, limit is {MAX_CHARS}")
    if "\n" in line or "\r" in line:
        raise SystemExit("line must stay on one line")
    return line


def main():
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(build_line(LINE), encoding="utf-8")


if __name__ == "__main__":
    main()
