#!/usr/bin/env python
# Test the weather app output
import subprocess
import sys

# Create input: select weather (current), then exit
input_sequence = "1\n4\n"

# Run the app with the input
result = subprocess.run(
    [sys.executable, "My_app.py"],
    input=input_sequence,
    capture_output=True,
    text=True,
    cwd="c:\\Users\\hp\\Desktop\\MYCODE",
    timeout=10
)

print("=== STDOUT ===")
print(result.stdout)
print("\n=== Return Code ===")
print(result.returncode)
if result.stderr:
    print("\n=== STDERR ===")
    print(result.stderr[:1000])
