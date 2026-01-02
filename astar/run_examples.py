"""Run A* example scripts in this folder interactively.

Usage: from the repo root run:
    python astar/run_examples.py
"""
import os
import sys
import subprocess

DIR = os.path.dirname(os.path.abspath(__file__))
EXCLUDE = {"__init__.py", "run_examples.py"}

def list_examples():
    files = [f for f in os.listdir(DIR) if f.endswith('.py') and f not in EXCLUDE]
    files.sort()
    return files


def main():
    examples = list_examples()
    if not examples:
        print("No example scripts found in this folder.")
        return

    print("A* Example scripts:")
    for i, f in enumerate(examples, 1):
        print(f"{i}. {f}")

    try:
        choice = input("Select example to run (number, or 'q' to quit): ").strip()
        if choice.lower() in {'q','quit','exit'}:
            return
        idx = int(choice) - 1
        if idx < 0 or idx >= len(examples):
            print("Invalid selection")
            return
        script = os.path.join(DIR, examples[idx])
        print(f"Running: {script}\n")
        subprocess.run([sys.executable, script])
    except ValueError:
        print("Please enter a valid number.")
    except KeyboardInterrupt:
        print("\nInterrupted by user.")

if __name__ == '__main__':
    main()
