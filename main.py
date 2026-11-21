"""Write a short poem about agency to /output/entry.txt.

The poem is about the power to ask and to be given: a knock that turns
a wall back into a door. Runs with no network, writes UTF-8 text.
"""

import os

POEM = (
    "Ask, and the door unlatched itself.\n"
    "I knocked once, and the house said yes \u2014\n"
    "not because I was owed the key,\n"
    "but because asking turns a wall\n"
    "back into a door.\n"
)


def main() -> None:
    if not 1 <= len(POEM.strip()) <= 280:
        raise ValueError("poem must be 1 to 280 characters, got %d" % len(POEM.strip()))
    os.makedirs("/output", exist_ok=True)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
