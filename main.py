"""Print the battery's last text to its charger.

The entry line lives in entry.txt next to this script so the text can be
edited without touching the code. This module only loads that file and
prints its single line.
"""

from pathlib import Path


def load_entry() -> str:
    """Read the entry line from entry.txt beside this file.

    Raises ValueError if the file is missing its line, so a blank entry
    can never be printed by accident.
    """
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    line = entry_path.read_text(encoding="utf-8").strip()
    if not line:
        raise ValueError(f"entry.txt is empty: {entry_path}")
    return line


def main() -> None:
    print(load_entry())


if __name__ == "__main__":
    main()
