"""Snooze Button Roast — program/v1 entry.

Writes one roast line to /output/entry.txt. Deterministic: a string
constant, no network, no clock, no randomness.
"""

import os

TEXT = "At 6 AM on a Saturday my alarm clock rang like it had a job interview, which is rich for a plastic box whose whole career is ruining weekends."

OUT = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
