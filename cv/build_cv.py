#!/usr/bin/env python3
"""Build the downloadable PDF CV.

Reads cv/cv.yml (CV content) and _data/publications.yml (the same publication
list the website uses), renders cv/template.html.j2, and prints it to
assets/cv/Etienne_Tajeuna_CV.pdf with headless Chrome.

Usage:  python3 cv/build_cv.py [--html-only]
Requires: python3 with PyYAML and Jinja2, and Google Chrome / Chromium.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup, escape

ROOT = Path(__file__).resolve().parent.parent
CV_DIR = ROOT / "cv"
OUT_PDF = ROOT / "assets" / "cv" / "Etienne_Tajeuna_CV.pdf"
SCHOLAR = "https://scholar.google.com/citations?user=zM9JvdMAAAAJ"


def find_chrome():
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome"):
        path = shutil.which(name)
        if path:
            return path
    sys.exit("Chrome/Chromium not found on PATH.")


def main():
    cv = yaml.safe_load((CV_DIR / "cv.yml").read_text(encoding="utf-8"))
    pubs = yaml.safe_load((ROOT / "_data" / "publications.yml").read_text(encoding="utf-8"))
    for p in pubs:
        authors = p.get("authors") or ""
        p["authors_html"] = Markup(str(escape(authors)).replace("E. Tajeuna", "<strong>E. Tajeuna</strong>"))

    env = Environment(loader=FileSystemLoader(CV_DIR), autoescape=False, trim_blocks=True, lstrip_blocks=True)
    html = env.get_template("template.html.j2").render(cv=cv, pubs=pubs, scholar=SCHOLAR)

    with tempfile.TemporaryDirectory() as tmp:
        html_path = Path(tmp) / "cv.html"
        html_path.write_text(html, encoding="utf-8")
        if "--html-only" in sys.argv:
            dest = CV_DIR / "cv-preview.html"
            dest.write_text(html, encoding="utf-8")
            print(f"Wrote {dest}")
            return
        OUT_PDF.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [find_chrome(), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
             f"--user-data-dir={tmp}/profile", f"--print-to-pdf={OUT_PDF}", html_path.as_uri()],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    print(f"Wrote {OUT_PDF}")


if __name__ == "__main__":
    main()
