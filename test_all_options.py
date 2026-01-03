#!/usr/bin/env python
# Test all menu options
import subprocess
import sys

# Create input: 2 (next), 3 (prev), 4 (exit)
input_sequence = "2\n3\n4\n"

# Run the app with the input
result = subprocess.run(
    [sys.executable, "My_app.py"],
    input=input_sequence,
    capture_output=True,
    text=True,
    cwd="c:\\Users\\hp\\Desktop\\MYCODE"
)

print("=== STDOUT ===")
print(result.stdout)
print("\n=== Return Code ===")
print(result.returncode)
if result.returncode != 0:
    print("\n=== STDERR ===")
    print(result.stderr[-1000:])
