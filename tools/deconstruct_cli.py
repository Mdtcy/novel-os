#!/usr/bin/env python3
"""Minimal scaffolding tool for the deconstruct workflow.

This does NOT run model inference. It prepares a folder layout and templates
so you can deconstruct a book consistently.

Usage:
  python tools/deconstruct_cli.py init --out deconstruct --chapters 120

It will create:
  deconstruct/
    blueprint.md
    style-profile.md
    hook-catalog.md
    promise-payoff.md
    characters.md
    chapter-rhythm.csv
    chapter-cards/CH0001.md ...
"""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "templates" / "deconstruct"


def _read_template(name: str) -> str:
    return (TEMPLATES / name).read_text(encoding="utf-8")


def init(out_dir: Path, chapters: int) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "chapter-cards").mkdir(parents=True, exist_ok=True)

    # Copy core templates
    (out_dir / "blueprint.md").write_text(_read_template("blueprint.md"), encoding="utf-8")
    (out_dir / "chapter-rhythm.csv").write_text(_read_template("chapter-rhythm.csv"), encoding="utf-8")

    # Create empty docs users fill manually
    for name in [
        "style-profile.md",
        "hook-catalog.md",
        "promise-payoff.md",
        "characters.md",
    ]:
        p = out_dir / name
        if not p.exists():
            p.write_text(f"# {name.rsplit('.', 1)[0].replace('-', ' ').title()}\n\n", encoding="utf-8")

    # Create chapter cards
    card_tmpl = _read_template("chapter-card.md")
    for i in range(1, chapters + 1):
        cid = f"CH{i:04d}"
        path = out_dir / "chapter-cards" / f"{cid}.md"
        if path.exists():
            continue
        path.write_text(card_tmpl.replace("CH0001", cid), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    init_p = sub.add_parser("init", help="Create a deconstruct workspace")
    init_p.add_argument("--out", default="deconstruct", help="Output directory")
    init_p.add_argument("--chapters", type=int, default=120, help="Number of chapter cards to generate")

    args = ap.parse_args()

    if args.cmd == "init":
        init(Path(args.out), args.chapters)


if __name__ == "__main__":
    main()
