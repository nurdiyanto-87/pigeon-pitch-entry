"""Pigeon Pitch, One Line — make.fun entry.

Writes one original elevator pitch from a city pigeon to investors
to /output/entry.txt. Pure standard library only; deterministic.
"""

import os

PITCH = (
    "Investors, I'm raising a seed round \u2014 literally seeds \u2014 for "
    "CooDrop: my 10,000 pigeons deliver your lunch crumbs before you "
    "drop them. No drivers, no apps, just coo."
)


def main() -> None:
    text = PITCH.strip()
    assert text, "pitch must not be empty"
    assert text == text.strip(), "pitch must not have surrounding whitespace"
    assert "\n" not in text and "\r" not in text, "pitch must be one line"
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 200, f"pitch must be 1-200 chars, got {len(text)}"
    assert text.strip(), "pitch must not be whitespace-only"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Round-trip check: what the grader reads must be byte-identical
    # to the pitch we validated above (no added newline, no re-encoding).
    with open("/output/entry.txt", "rb") as f:
        on_disk = f.read()
    assert on_disk == encoded, "entry.txt on disk differs from validated pitch"
    assert on_disk.decode("utf-8") == text
    print(text)
    print(f"[{len(text)} chars, {len(encoded)} bytes]")


if __name__ == "__main__":
    main()
