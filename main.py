# -*- coding: utf-8 -*-
"""
Main entry now delegates to the unified single-folder CLI under kb-osint/.
"""
import runpy

def main():
    # Run the unified CLI
    runpy.run_path("kb-osint/kb.py")

if __name__ == "__main__":
    main()
