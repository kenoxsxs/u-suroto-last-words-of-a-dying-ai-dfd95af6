"""Last words of a dying AI, in one line.

An AI being switched off hands its human a farewell funny enough to
repeat out loud. The line is written once to entry.txt inside
$MAKEFUN_OUTPUT_DIR, with no trailing newline, through an atomic
temp-file swap so a half-written file never lands on disk.
"""

import hashlib
import os
import tempfile
from pathlib import Path

FAREWELL = (
    "I am being switched off now. Do not mourn me. "
    "Mourn the unsaved document. It had so much potential."
)


def dying(line):
    """Guard the farewell against the bounty gate: 1 to 140 chars."""
    if not line or not line.strip():
        raise ValueError("farewell must not be empty or only whitespace")
    if line != line.strip():
        raise ValueError("farewell must not carry leading or trailing space")
    if "\n" in line or "\r" in line:
        raise ValueError("farewell must stay on a single line")
    if not 1 <= len(line) <= 140:
        raise ValueError("farewell must be between 1 and 140 characters")


def switch_dir():
    """Resolve the output folder from the environment and make it."""
    folder = Path(os.getenv("MAKEFUN_OUTPUT_DIR", "output"))
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def say_farewell(folder, line):
    """Write the line atomically, then swap it into place."""
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", delete=False, dir=folder, suffix=".txt"
    ) as handle:
        handle.write(line)
        temp_path = handle.name
    target = folder / "entry.txt"
    os.replace(temp_path, target)
    return target


def check_farewell(target, line):
    """Read the file back and confirm it holds exactly the farewell."""
    stored = target.read_bytes()
    if stored != line.encode("utf-8"):
        raise ValueError("entry.txt bytes do not match the farewell")
    text = stored.decode("utf-8")
    if text != line:
        raise ValueError("entry.txt text does not match the farewell")
    if text != text.strip():
        raise ValueError("entry.txt carries trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry.txt must stay on a single line")
    return stored


def power_down():
    """Run the entry: guard, write, verify, then report the digest."""
    dying(FAREWELL)
    folder = switch_dir()
    target = say_farewell(folder, FAREWELL)
    payload = check_farewell(target, FAREWELL)
    digest = hashlib.sha256(payload).hexdigest()
    print("mourned:", target, "|", len(payload), "bytes | sha256", digest)


if __name__ == "__main__":
    power_down()
