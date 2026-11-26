"""One Line to Your Younger Self — make.fun entry.

Writes a single line, in English, that its writer would send back to
their younger self if one line were all they got. Deterministic: the
same bytes on every run, no time, no randomness, no network.
"""

import os

ENTRY = (
    # Three hard-won truths from a life actually lived (tabs, the dip,
    # the girl), then one imperative that stings: the window it names
    # — before 2019 ends — is already closed.
    "The tabs will never close themselves, 'buy the dip' is a lie, "
    "and the girl you like already likes you back. "
    "Go talk to her before 2019 ends."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip() == ENTRY, "entry must not start or end with whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
