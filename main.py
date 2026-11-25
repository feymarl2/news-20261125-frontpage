#!/usr/bin/env python3
"""News image entry for make.fun's "Sum up 25 November's world news in one image".

Copies the entry.png beside this file to <MAKEFUN_OUTPUT_DIR>/entry.png.
Deterministic: the same bytes every run, no network, stdlib only.
The image is 1024x1024 and under 1 MiB; the copy is chmodded 0644 so
the grader, which reads outputs as a different uid, can always read it.
"""

import os
import shutil


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    os.chmod(dst, 0o644)


if __name__ == "__main__":
    main()
