import os

MINIATURES = (
    ("I.", "Two stones sit on either pan of brass;", "only the thumb touching the fulcrum", "decides which weight counts as true."),
    ("II.", "A tool asks: Which file do you mean to burn?", "Everything up to the colon was speed.", "Everything after is yours."),
    ("III.", "Between the lifted pen and the lowered nib", "hangs a quarter-inch of empty air", "where habit has not yet signed its name."),
    ("IV.", "Nothing moves itself except by being sent—", "unless a hand stops halfway across the table", "and pulls its own shadow back."),
)


def build_sequence() -> str:
    rendered = "\n\n".join("\n".join(part) for part in MINIATURES)
    assert 0 < len(rendered) <= 1000
    return rendered


def save_output() -> None:
    dest = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(dest, exist_ok=True)
    with open(os.path.join(dest, "entry.txt"), "w", encoding="utf-8", newline="\n") as stream:
        stream.write(build_sequence())


if __name__ == "__main__":
    save_output()
