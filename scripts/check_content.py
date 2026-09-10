"""Content checks for the MkDocs blog."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CONFIG = ROOT / "mkdocs.yml"
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+['\"][^'\"]*['\"])?\)")
FENCED_BLOCK = re.compile(r"^```.*?^```\s*$", re.MULTILINE | re.DOTALL)
H1_PATTERN = re.compile(r"^#\s+\S", re.MULTILINE)
IGNORED_SCHEMES = {"http", "https", "mailto", "tel", "data"}


def nav_paths(node: object) -> list[str]:
    """Return every local path declared in the nested MkDocs navigation."""
    if isinstance(node, list):
        return [path for item in node for path in nav_paths(item)]
    if isinstance(node, dict):
        return [path for value in node.values() for path in nav_paths(value)]
    if isinstance(node, str):
        return [node]
    return []


def check_navigation(errors: list[str]) -> None:
    config = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    for entry in nav_paths(config.get("nav", [])):
        parsed = urlsplit(entry)
        if parsed.scheme in IGNORED_SCHEMES:
            continue
        target = DOCS / unquote(parsed.path)
        if not target.is_file():
            errors.append(f"Navigation verweist auf fehlende Datei: {entry}")


def check_markdown(errors: list[str]) -> None:
    for page in sorted(DOCS.rglob("*.md")):
        text = page.read_text(encoding="utf-8")
        visible_text = FENCED_BLOCK.sub("", text)

        h1_count = len(H1_PATTERN.findall(visible_text))
        if h1_count != 1:
            errors.append(
                f"{page.relative_to(ROOT)} enthält {h1_count} H1-Überschriften (erwartet: 1)"
            )

        for raw_target in LINK_PATTERN.findall(visible_text):
            target_text = raw_target.strip("<>")
            parsed = urlsplit(target_text)
            if parsed.scheme in IGNORED_SCHEMES or target_text.startswith("#"):
                continue
            local_path = unquote(parsed.path)
            if not local_path:
                continue
            target = (page.parent / local_path).resolve()
            if target.is_dir():
                target = target / "index.md"
            if not target.is_file():
                errors.append(
                    f"Defekter lokaler Link in {page.relative_to(ROOT)}: {target_text}"
                )


def main() -> int:
    errors: list[str] = []
    check_navigation(errors)
    check_markdown(errors)

    if errors:
        print("Inhaltsprüfung fehlgeschlagen:")
        for error in errors:
            print(f"- {error}")
        return 1

    pages = sum(1 for _ in DOCS.rglob("*.md"))
    print(f"Inhaltsprüfung erfolgreich: {pages} Markdown-Seiten geprüft.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
