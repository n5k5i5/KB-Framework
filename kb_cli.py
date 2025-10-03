# -*- coding: utf-8 -*-
"""
KB-OSINT CLI entry now delegates to the unified kb-osint/kb_cli.py.
"""
import runpy

if __name__ == "__main__":
    runpy.run_path("kb-osint/kb_cli.py")