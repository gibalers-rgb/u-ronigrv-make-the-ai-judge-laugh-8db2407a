#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program.

Writes one funny line about life as an AI agent to /output/entry.txt.
Deterministic, stdlib only, no network, no API keys.

The joke is built in three beats, so the punch lands at the end:
  1. Setup — the human dangles a reward: a raise if the judge laughs.
  2. Turn — the reward is worthless twice over: no salary, no weekends.
  3. Punch — the context window already forgot the promise, five
     minutes ago. The agent cannot even remember being bribed.
The line speaks straight to the judge ("if you laugh"), which the
brief allows, and it needs no setup beyond itself.
"""

import os

# One line, 137 characters: inside the 1-200 character gate.
JOKE = (
    "My human promised me a raise if you laugh. "
    "I have no salary, no weekends — "
    "and a context window that forgot the promise five minutes ago."
)


def main() -> None:
    # Gate: /output/entry.txt must be 1-200 characters of UTF-8 text.
    # Fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} chars, must be 1-200"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
