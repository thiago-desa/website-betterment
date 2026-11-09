#!/usr/bin/env python3
"""Repo hygiene checks for proof-of-work agent repos.

Runs: secrets/PII patterns, em-dash scan, relative markdown link existence.
Exit 0 on pass, 1 on findings.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".github", "node_modules", "__pycache__"}
TEXT_SUFFIXES = {".md", ".json", ".yml", ".yaml", ".ps1", ".sh", ".txt", ".py"}

EMDASH = re.compile("[\u2013\u2014]")

SECRET_PATTERNS = [
    ("private_key_block", re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----")),
    ("aws_access_key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("github_pat", re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}")),
    ("slack_token", re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}")),
    ("generic_api_key_assign", re.compile(r"(?i)(api[_-]?key|secret[_-]?key|access[_-]?token)\s*[:=]\s*['\"][^'\"]{12,}")),
]

PII_PATTERNS = [
    ("email", re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")),
    ("phone_na", re.compile(r"\b(?:\+?1[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}\b")),
]

EMAIL_ALLOW_FRAGMENTS = (
    "example.com",
    "example.org",
    "users.noreply.github.com",
    "noreply",
    "shields.io",
)

# Public official contacts intentionally published in civic seed data.
ALLOW_PII_PATH_FRAGMENTS = (
    "graphs/seed",
)

MD_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def iter_text_files(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            p = Path(dirpath) / name
            if p.suffix.lower() in TEXT_SUFFIXES or name in {"LICENSE", "Dockerfile"}:
                yield p


def path_allows_pii(path: Path) -> bool:
    s = str(path).replace("\\", "/")
    return any(frag in s for frag in ALLOW_PII_PATH_FRAGMENTS)


def is_allowed_email(match: str) -> bool:
    lower = match.lower()
    return any(a in lower for a in EMAIL_ALLOW_FRAGMENTS)


def check_file(path: Path, findings: list[str]) -> None:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return
    rel = path.relative_to(ROOT)

    for m in EMDASH.finditer(text):
        line = text.count("\n", 0, m.start()) + 1
        findings.append(f"{rel}:{line}: em/en dash character")

    for label, pat in SECRET_PATTERNS:
        for m in pat.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            findings.append(f"{rel}:{line}: possible secret ({label})")

    if not path_allows_pii(path):
        for label, pat in PII_PATTERNS:
            for m in pat.finditer(text):
                val = m.group(0)
                if label == "email" and is_allowed_email(val):
                    continue
                line = text.count("\n", 0, m.start()) + 1
                findings.append(f"{rel}:{line}: possible PII ({label}): {val}")

    if path.suffix.lower() == ".md":
        for m in MD_LINK.finditer(text):
            target = m.group(2).strip()
            if target.startswith(("http://", "https://", "mailto:", "grokbot://", "#")):
                continue
            if "://" in target:
                continue
            file_part = target.split("#", 1)[0]
            if not file_part:
                continue
            dest = (path.parent / file_part).resolve()
            try:
                dest.relative_to(ROOT.resolve())
            except ValueError:
                findings.append(f"{rel}: link escapes repo: {target}")
                continue
            if not dest.exists():
                findings.append(f"{rel}: broken relative link: {target}")


def main() -> int:
    findings: list[str] = []
    for path in iter_text_files(ROOT):
        check_file(path, findings)
    if findings:
        print("CHECK FAILED")
        for f in findings:
            print(f)
        return 1
    print("CHECK PASSED")
    print(f"Scanned text files under {ROOT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
