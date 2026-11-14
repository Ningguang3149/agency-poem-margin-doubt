"""Deterministic poem emitter for agency-poem-01."""

import os
from pathlib import Path

POEM = "The Axle in the Creek\n\nThe boundary surveyor carried a yellow pole\ncapped with a dome that caught seven satellites.\nThe screen blinked blue, resolved down to three millimeters,\nand drew a red vector through the birch grove.\n\"Your property line is here,\" he said,\ntapping a plastic pin into the ferns.\n\"Your grandfather's fence is seven feet off.\"\n\nI led him down the gully to the water\nwhere the creek bends around the roots of the hemlock.\nI reached shoulder-deep into the cold current,\nfound the slime-slick iron,\nand pulled up the weed until he could see it:\nan unthreaded wagon axle from nineteen-forty,\ndriven into bedrock by two men with sledgehammers.\n\n\"That's not legal datum,\" the surveyor said.\n\"The state grid shifts with the continental plate.\"\n\"It's not datum,\" I told him, drying my arm on my sleeve.\n\"It's where he shook hands with Arthur Miller\nafter the flood washed the hay away.\"\n\nI left his plastic pin in the ferns.\nThe iron stays in the water."


def main() -> None:
    chars = len(POEM)
    if not (1 <= chars <= 1000) or not POEM.strip():
        raise ValueError(f"Invalid poem length: {chars}")
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    out_file = target_dir / "entry.txt"
    out_file.write_text(POEM, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
