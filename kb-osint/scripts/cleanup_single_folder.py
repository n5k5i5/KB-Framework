# -*- coding: utf-8 -*-
"""
Cleanup script to consolidate repository into a single-folder code layout (kb-osint/).

Dry-run by default. Use --apply to actually remove legacy top-level directories.
This script will NOT touch anything under kb-osint/.
"""

import os
import sys
import shutil
import argparse

LEGACY_DIRS = [
    "arayüz",
    "çekirdek",
    "modüller",
    "moduller",
    "eklentiler",
    "raporlar",
    "veri",
    "kb_osint",
    "external",
    "backups",
    "logs",
    "utils",
    "tests",
    "scripts",    # top-level scripts (keep kb-osint/scripts)
    "config",
    "docs",
]

LEGACY_FILES = [
    "requirements.txt",  # prefer kb-osint/requirements.txt
]


def repo_root() -> str:
    # kb-osint/scripts/ -> kb-osint/ -> repo root
    here = os.path.abspath(os.path.dirname(__file__))
    root = os.path.abspath(os.path.join(here, "..", ".."))
    return root


def is_safe_path(root: str, target: str) -> bool:
    """Ensure target is inside root and not kb-osint/ path."""
    try:
        target_abs = os.path.abspath(os.path.join(root, target))
        if not target_abs.startswith(root):
            return False
        # Don't remove kb-osint subtree
        kb_osint_abs = os.path.abspath(os.path.join(root, "kb-osint"))
        if target_abs.startswith(kb_osint_abs):
            return False
        return True
    except Exception:
        return False


def main():
    parser = argparse.ArgumentParser(description="Cleanup to single-folder layout (kb-osint/)")
    parser.add_argument("--apply", action="store_true", help="Apply deletions (default is dry-run)")
    args = parser.parse_args()

    root = repo_root()
    print(f"Repository root: {root}")

    removed = []
    skipped = []

    # Directories
    for d in LEGACY_DIRS:
        if not is_safe_path(root, d):
            skipped.append(d)
            continue
        path = os.path.join(root, d)
        if os.path.isdir(path):
            if args.apply:
                try:
                    shutil.rmtree(path)
                    removed.append(path)
                    print(f"Removed directory: {path}")
                except Exception as e:
                    print(f"Failed to remove {path}: {e}")
            else:
                print(f"[DRY-RUN] Would remove directory: {path}")
        else:
            # Not present
            pass

    # Files
    for f in LEGACY_FILES:
        if not is_safe_path(root, f):
            skipped.append(f)
            continue
        path = os.path.join(root, f