# -*- coding: utf-8 -*-
"""
Reset repository to single-folder layout (kboaint/).
Removes everything in repo root EXCEPT:
- kboaint/ (this folder)
- .git, .gitignore (if present)

Usage:
    python kboaint/scripts/reset_repo.py --apply

By default runs in dry-run mode.
"""
import os
import argparse
import shutil

def repo_root() -> str:
    here = os.path.abspath(os.path.dirname(__file__))
    return os.path.abspath(os.path.join(here, "..", ".."))

def main():
    parser = argparse.ArgumentParser(description="Reset repo to single-folder (kboaint/)")
    parser.add_argument("--apply", action="store_true", help="Apply deletions")
    args = parser.parse_args()

    root = repo_root()
    keep = {"kboaint", ".git", ".gitignore"}
    entries = os.listdir(root)

    removed = 0
    print(f"Repository root: {root}")
    for name in entries:
        if name in keep:
            print(f"[KEEP] {name}")
            continue
        path = os.path.join(root, name)
        if args.apply:
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                    print(f"[DEL] dir: {path}")
                else:
                    os.remove(path)
                    print(f"[DEL] file: {path}")
                removed += 1
            except Exception as e:
                print(f"[ERR] {path}: {e}")
        else:
            print(f"[DRY] Would delete: {path}")

    print(f"\nDone. Removed count: {removed} (apply={args.apply})")
    if not args.apply:
        print("Run with --apply to perform deletions.")

if __name__ == "__main__":
    main()