"""Entry program for the make.fun news-image-20261117 bounty.

The repository ships one image, entry.png, which sums up the world news
of Tuesday 17 November 2026. This program copies that image, byte for
byte, to the output directory the grader provides.

It is deterministic: every run writes exactly the same bytes, because it
only copies a fixed file. It uses the standard library only, needs no
network, and reads nothing outside this repository.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print("entry.png not found beside main.py", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
