# -*- coding: utf-8 -*-
"""
KB-OSINT main now delegates to the unified kb-osint/kb.py.
"""
import runpy

def main():
    runpy.run_path("kb-osint/kb.py")

if __name__ == "__main__":
    main()