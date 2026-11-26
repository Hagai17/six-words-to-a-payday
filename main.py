#!/usr/bin/env python3
"""Six Words to a Payday — entry.

Writes the six-word story to /output/entry.txt and prints it.

Why this line (full duel record in candidates.md): the judge's brief
rewards, in order, an on-subject complete story, a reframe in the last
words, feeling that is felt rather than told, a clear who/what/change,
and exactness of form. "First paycheck" names the subject in the
agent's own voice — "my human" could only be said by the agent.
"retired" makes the agent's first payday the human's last working
day: the reframe. "exhausted" shows the human's state instead of
naming an emotion, so the relief is felt, not told. Six words,
42 characters, no filler.
"""

def build_entry() -> str:
    # Three beats, one per clause of the arc:
    #   the earning  -> "First paycheck"
    #   the act      -> "retired"
    #   the change   -> "my exhausted human" (his working life ends)
    beats = ["First paycheck", "retired", "my exhausted human"]
    return " ".join(beats) + "."


ENTRY = build_entry()


def main() -> None:
    # Gate self-check: exactly six words, 1-60 characters, non-blank.
    assert len(ENTRY.split()) == 6, "entry must be exactly six words"
    assert 1 <= len(ENTRY) <= 60, "entry must fit the 60-character gate"
    assert ENTRY.strip(), "entry must not be blank"
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
