import argparse
import os
from typing import Iterator


def line_stream() -> Iterator[str]:
    groups = [
    [
        "Room 6"
    ],
    [
        "All afternoon the clinic assistant handled the queue:",
        "clear bloodwork, refill approvals, routine follow-ups",
        "sent before my coffee cooled.",
        "Every message was warm, accurate, signed with my title."
    ],
    [
        "At 4:40 Mrs. Chen's scan arrived.",
        "Before I opened the second page,",
        "a draft waited in the outbox:",
        "\"We found something that needs closer attention.",
        "Please click below to schedule...\"",
        "Compassionate, compliant, ready in one click."
    ],
    [
        "I looked at the blue Send button for ten seconds.",
        "Routine news can travel through wires.",
        "Grief shouldn't arrive between a pharmacy alert",
        "and a grocery receipt."
    ],
    [
        "I closed the laptop, took the paper chart,",
        "and walked out to the chairs myself—",
        "to sit on the vinyl beside her",
        "and hold the bad news in my own mouth."
    ]
]
    for idx, block in enumerate(groups):
        if idx > 0:
            yield ""
        for line in block:
            yield line


def write_entry(output_dir: str) -> None:
    poem = "\n".join(line_stream())
    if not poem.strip() or len(poem) > 1000:
        raise ValueError("Invalid entry size")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "wb") as fp:
        fp.write(poem.encode("utf-8"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--out", default=os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    ns, _ = parser.parse_known_args()
    write_entry(ns.out)
