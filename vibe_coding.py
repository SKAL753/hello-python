
import random
import time
import os

PROJECT_NAME = "AI VIBE CODER 3000"
VERSION = "0.0.1 (probably stable)"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def type_text(text, delay=0.02):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def loading(message):
    print(f"\n{message}", end="", flush=True)

    for _ in range(random.randint(10, 25)):
        time.sleep(0.08)
        print(random.choice([".", ".", ".", "█"]), end="", flush=True)

    print(" DONE")


def generate_code():
    fake_code = [
        "import everything",
        "from ai import magic",
        "try:",
        "    fix_everything()",
        "except Exception:",
        "    ask_ai_again()",
        "",
        "# TODO: understand this later",
        "print('It works on my machine')",
    ]

    for line in fake_code:
        print(f"\033[92m{line}\033[0m")
        time.sleep(0.15)


def main():
    clear()

    print("=" * 50)
    print(f"   {PROJECT_NAME}")
    print(f"   Version: {VERSION}")
    print("=" * 50)

    username = input("\nEnter developer name: ")
    project = input("What are we building today? ")

    print("\nInitializing AI development environment...")
    loading("Connecting to ChatGPT")
    loading("Installing unnecessary dependencies")
    loading("Reading documentation (skipping)")
    loading("Generating architecture")

    print("\nGenerating your revolutionary application...\n")
    generate_code()

    print("\nRunning automated tests...")
    time.sleep(1)

    if random.random() < 0.7:
        print("\033[91mERROR: Something went wrong.\033[0m")
        input("\nPress Enter to ask AI to fix it...")

        loading("Fixing the bug")
        loading("Fixing the fix")
        loading("Reverting the fix")

    print("\n" + "=" * 50)
    print("BUILD SUCCESSFUL (we think)")
    print("=" * 50)

    print(f"\nDeveloper: {username}")
    print(f"Project:   {project}")
    print("Code quality:  questionable")
    print("Test coverage: 100% (tests not included)")
    print("Documentation: ask the AI")
    print("Understanding: 0%")
    print("\nStatus: READY FOR PRODUCTION 🚀")

    print("\nRemember:")
    print('"If it works, do not touch it."')

    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
