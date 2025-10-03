# -*- coding: utf-8 -*-
"""
Interactive shell.
"""
from interface.command_parser import CommandParser
from interface.formatter import Formatter


class InteractiveShell:
    def __init__(self):
        self.prompt = "KB-OSINT> "
        self.commands = {}
        self.parser = CommandParser()

    def register_command(self, name, func, description=""):
        self.commands[name] = (func, description)

    def help(self):
        print(Formatter.title("Available Commands / Kullanılabilir Komutlar"))
        for name, (_, description) in sorted(self.commands.items()):
            print(f"{name:20} {description}")

    def run(self):
        self.help()
        while True:
            try:
                line = input(self.prompt).strip()
            except (EOFError, KeyboardInterrupt):
                print("\n" + Formatter.info("Exiting... / Çıkılıyor..."))
                break

            if not line:
                continue

            parts = self.parser.parse(line)
            cmd = parts[0]
            args = parts[1:]

            if cmd in {"cikis", "exit"}:
                print(Formatter.info("Exiting... / Çıkılıyor..."))
                break

            if cmd in {"yardim", "help"}:
                self.help()
                continue

            if cmd in self.commands:
                func, _ = self.commands[cmd]
                try:
                    func(args)
                except Exception as e:
                    print(Formatter.error(f"Command execution error: {e}"))
            else:
                print(Formatter.error(f"Unknown command: {cmd}. Use 'help' / 'yardim'."))