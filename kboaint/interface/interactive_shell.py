# -*- coding: utf-8 -*-
from typing import Callable, Dict, List

class InteractiveShell:
    def __init__(self):
        self.prompt = "KB-OSINT> "
        self.commands: Dict[str, Dict[str, Callable]] = {}
        self.history: List[str] = []

    def register_command(self, name: str, fn: Callable, desc: str) -> None:
        self.commands[name] = {"fn": fn, "desc": desc}

    def help(self) -> None:
        print("Available commands:")
        for k, v in sorted(self.commands.items()):
            print(f"  - {k:18} {v['desc']}")

    def run(self) -> None:
        print("Welcome to KB-OSINT interactive shell")
        print("Type 'help' or 'yardim' for commands. 'exit' or 'cikis' to quit.")
        while True:
            try:
                line = input(self.prompt).strip()
                if not line:
                    continue
                self.history.append(line)
                parts = line.split()
                cmd = parts[0]
                args = parts[1:]
                if cmd in {"exit", "cikis", "quit"}:
                    print("Goodbye.")
                    break
                elif cmd in {"help", "yardim"}:
                    self.help()
                elif cmd in self.commands:
                    self.commands[cmd]["fn"](args)
                else:
                    print(f"Unknown command: {cmd}")
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"Error: {e}")