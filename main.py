"""Fortune in a Pot — make.fun bounty.

One line telling a houseplant's fortune: kind, funny, unmistakably about
the plant on the windowsill.
"""

LINE = (
    "Your fortune: repotted soon, loved loudly, sunny spot by spring — "
    "but beware the cat, who has plans for your leaves."
)

LIMIT = 120
TARGET = "/output/entry.txt"


def check_entry(line):
    """Validate the entry: one non-blank line within the char limit."""
    if not isinstance(line, str) or not line.strip():
        raise ValueError("entry must be a non-blank string")
    if "\n" in line.strip():
        raise ValueError("entry must be a single line")
    if len(line) > LIMIT:
        raise ValueError(f"entry is {len(line)} chars, over the {LIMIT} limit")
    if "fortune" not in line.lower() or "cat" not in line.lower():
        raise ValueError("fortune must mention the fortune and the cat")
    if line.strip() != line:
        raise ValueError("entry must not have leading or trailing whitespace")
    return line


def write_entry(line):
    """Print the line and write it to /output/entry.txt."""
    import os

    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    check_entry(LINE)
    write_entry(LINE)
