#!/usr/bin/env python3
"""Run Blogkit's post-render hook from wherever the extension is installed.

`quarto add` and `quarto use template` put it in _extensions/statmania/blogkit/; a manual
copy (and the Blogkit repository itself) uses _extensions/blogkit/.
"""
import runpy
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
for folder in ("_extensions/statmania/blogkit", "_extensions/blogkit"):
    script = root / folder / "repair_index.py"
    if script.exists():
        runpy.run_path(str(script), run_name="__main__")
        break
else:
    sys.exit("blogkit: extension not found; run `quarto add statmania/quarto-blogkit`")
