
import os
import sys
import time
import random
import platform
import hashlib
import shutil
from datetime import datetime

# ============================================================
# AI VIBE CODER 3000: ULTIMATE DEVELOPER EDITION
# Copyright nobody. Licensed under pure vibes.
# ============================================================

VERSION = "9.9.9-BETA-ULTRA-LEGENDARY"
PROJECT_NAME = "AI VIBE CODER 3000"

# ANSI COLORS
RESET = "\033[0m"
GREEN = "\033[92m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
YELLOW = "\033[93m"
RED = "\033[91m"
WHITE = "\033[97m"
GRAY = "\033[90m"
BOLD = "\033[1m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def color(text, colour=GREEN):
    return f"{colour}{text}{RESET}"


def type_text(text, delay=0.015):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def random_hex(length=32):
    return "".join(random.choices("0123456789ABCDEF", k=length))


def divider():
    print(color("═" * 62, CYAN))


def banner():
    print(color(r"""
     █████╗ ██╗    ██╗██╗   ██╗
    ██╔══██╗██║    ██║██║   ██║
    ███████║██║ █╗ ██║██║   ██║
    ██╔══██║██║███╗██║╚██╗ ██╔╝
    ██║  ██║╚███╔███╔╝ ╚████╔╝
    ╚═╝  ╚═╝ ╚══╝╚══╝   ╚═══╝
    """, GREEN))

    print(color("       V I B E   C O D E R   3 0 0 0", MAGENTA))
    print(color("       ULTIMATE DEVELOPER EDITION", CYAN))
    print(color(f"       Version {VERSION}", GRAY))
    divider()


def loading(message, duration=None):
    if duration is None:
        duration = random.uniform(0.5, 1.4)

    width = 32
    steps = 32

    print(f"{CYAN}[SYSTEM]{RESET} {message}")

    for i in range(steps + 1):
        progress = i / steps
        filled = int(width * progress)
        bar = "█" * filled + "░" * (width - filled)
        percent = int(progress * 100)

        print(
            f"\r  {MAGENTA}[{bar}]{RESET} "
            f"{percent:3d}%",
            end="",
            flush=True,
        )
        time.sleep(duration / steps)

    print(color("  COMPLETE", GREEN))


def matrix_rain():
    clear()
    print(color("INITIALIZING MATRIX PROTOCOL...", GREEN))
    print()

    chars = "01ABCDEF#$%&@"
    width = min(shutil.get_terminal_size((80, 24)).columns, 100)

    for _ in range(12):
        line = "".join(random.choice(chars) for _ in range(width))
        print(color(line, random.choice([GREEN, CYAN, MAGENTA])))
        time.sleep(0.08)

    print()
    type_text(color("MATRIX ACCESS GRANTED.", GREEN), 0.04)
    time.sleep(0.6)


def system_diagnostics():
    divider()
    print(color("        EXTREMELY UNNECESSARY SYSTEM DIAGNOSTICS", YELLOW))
    divider()

    diagnostics = [
        ("CPU VIBE FREQUENCY", f"{random.randint(9000, 99999)} MHz"),
        ("GPU AURA", f"{random.randint(80, 999)}%"),
        ("QUANTUM COFFEE LEVEL", f"{random.randint(1, 100)}%"),
        ("AI CONFIDENCE", f"{random.randint(101, 999)}%"),
        ("KEYBOARD RGB", "MAXIMUM"),
        ("BUG REPELLENT", "EXPIRED"),
        ("STACK OVERFLOW ENERGY", "CRITICAL"),
        ("DEVELOPER AURA", f"{random.randint(1, 100)} / 100"),
        ("PYTHON SNAKE MODE", "ACTIVATED"),
        ("GRAVITY ENGINE", "UNNECESSARY"),
    ]

    for name, value in diagnostics:
        print(
            f" {color(name, CYAN):<30} "
            f"{color(value, GREEN)}"
        )
        time.sleep(0.12)

    print()
    print(color("WARNING: Your computer has become too powerful.", RED))
    divider()


def hacking_sequence():
    print()
    print(color(">>> ESTABLISHING SECURE VIBE CONNECTION <<<", MAGENTA))

    for _ in range(8):
        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        port = random.choice([443, 8080, 1337, 9001, 65535])

        print(
            f"{GREEN}[ACCESS]{RESET} "
            f"{ip}:{port} "
            f"| KEY={random_hex(12)}"
        )
        time.sleep(0.13)

    print()
    print(color("ENCRYPTION: UNNECESSARILY STRONG", CYAN))
    print(color("HACKING: COMPLETELY SIMULATED", YELLOW))


def generate_code():
    code = [
        "import everything",
        "from ai import magic",
        "from vibes import immaculate",
        "",
        "class RevolutionaryApplication:",
        "    def __init__(self):",
        "        self.bugs = float('inf')",
        "        self.confidence = 1000",
        "",
        "    def fix_everything(self):",
        "        try:",
        "            return self.add_ai()",
        "        except Exception:",
        "            return self.ask_ai_again()",
        "",
        "app = RevolutionaryApplication()",
        "app.fix_everything()",
        "print('It works on my machine')",
    ]

    print(color(">>> AI-GENERATED SOURCE CODE", CYAN))
    print()

    for line in code:
        print(color(line, GREEN))
        time.sleep(0.10)

    return code


def compile_project(code):
    print()
    divider()
    print(color("INITIATING QUANTUM COMPILATION ENGINE", MAGENTA))
    divider()

    loading("Compiling Python into pure vibes")
    loading("Optimizing unnecessary abstractions")
    loading("Installing 47 imaginary dependencies")
    loading("Converting coffee into machine code")
    loading("Calibrating developer aura")

    print()
    print(color("RUNNING UNIT TESTS...", CYAN))

    tests = [
        "Does it run?",
        "Does it look cool?",
        "Does anyone understand it?",
        "Did AI invent new syntax?",
        "Can we blame the compiler?",
    ]

    for test in tests:
        passed = random.choice([True, True, True, False])
        status = color("PASS", GREEN) if passed else color("SKIPPED", YELLOW)

        print(f"  [{status}] {test}")
        time.sleep(0.25)

    print()
    print(color("BUILD RESULT: PROBABLY SUCCESSFUL", GREEN))


def generate_report(project, username, code):
    divider()
    print(color("          FINAL DEVELOPER REPORT", CYAN))
    divider()

    project_hash = hashlib.sha256(
        project.encode("utf-8")
    ).hexdigest()[:16].upper()

    metrics = [
        ("Developer", username),
        ("Project", project),
        ("Runtime", platform.python_version()),
        ("Operating system", platform.system()),
        ("Lines of code", len(code)),
        ("Project hash", project_hash),
        ("Code quality", "CLASSIFIED"),
        ("Architecture", "UNNECESSARILY COMPLEX"),
        ("Documentation", "VIBES-BASED"),
        ("Actual AI usage", "0%"),
        ("Confidence", "1000%"),
    ]

    for name, value in metrics:
        print(f"{color(name + ':', CYAN):<32} {value}")

    divider()
    print(color("ACHIEVEMENT UNLOCKED: PROFESSIONAL COPY-PASTER", YELLOW))
    print(color("RANK: SENIOR VIBE ENGINEER", MAGENTA))
    print(color("PRODUCTION READINESS: ASK AGAIN LATER", RED))
    divider()


def easter_egg():
    clear()
    print(color(r"""
       .-----------------------.
       |  TOP SECRET TERMINAL  |
       |  ACCESS LEVEL: ???    |
       '-----------------------'
    """, MAGENTA))

    secrets = [
        "The real bug was the developer all along.",
        "There are 47 dependencies. None are necessary.",
        "The code works. Nobody knows why.",
        "Git commit message: final_final_REAL.py",
        "AI has replaced your TODO comments with more TODOs.",
        "Congratulations. You have achieved peak laziness.",
    ]

    print()
    type_text(random.choice(secrets), 0.035)
    print()
    input("Press Enter to return to the terminal...")


def secret_menu():
    while True:
        print()
        divider()
        print(color("SECRET DEVELOPER MENU", MAGENTA))
        print("1. Matrix rain")
        print("2. Generate classified access codes")
        print("3. Reveal developer wisdom")
        print("4. Return to main menu")

        choice = input(color("\nSelect protocol: ", CYAN)).strip()

        if choice == "1":
            matrix_rain()

        elif choice == "2":
            hacking_sequence()

        elif choice == "3":
            easter_egg()

        elif choice == "4":
            break

        else:
            print(color("INVALID INPUT. YOUR AURA HAS DECREASED.", RED))


def main():
    clear()
    banner()

    print(color("WELCOME, FUTURE LEGEND.", GREEN))
    username = input("\nDeveloper codename: ").strip() or "Anonymous Legend"
    project = input("Project name: ").strip() or "Untitled AI Disaster"

    print()
    type_text(f"Initializing project: {project}", 0.025)

    loading("Booting vibe reactor")
    loading("Negotiating with artificial intelligence")
    loading("Disabling unnecessary common sense")

    system_diagnostics()

    print()
    choice = input(
        color("Activate Matrix protocol? (y/n): ", CYAN)
    ).strip().lower()

    if choice == "y":
        matrix_rain()

    hacking_sequence()

    print()
    code = generate_code()
    compile_project(code)

    print()
    choice = input(
        color("Open secret developer menu? (y/n): ", MAGENTA)
    ).strip().lower()

    if choice == "y":
        secret_menu()

    generate_report(project, username, code)

    print()
    print(color("SYSTEM SHUTDOWN INITIATED...", RED))
    loading("Saving absolutely nothing")

    print()
    type_text(
        color("THANK YOU FOR VIBE CODING. STAY UNEMPLOYABLE.", GREEN),
        0.035,
    )

    input("\nPress Enter to terminate the universe...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(color("\n\nVIBE INTERRUPTED. REALITY RESTORED.", RED))
