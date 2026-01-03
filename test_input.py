#!/usr/bin/env python
# Test menu input
import subprocess
import sys

# Create input: show menu, press 4 to exit
input_sequence = "4\n"

# Run the app with the input
result = subprocess.run(
    [sys.executable, "My_app.py"],
    input=input_sequence,
    capture_output=True,
    text=True,
    cwd="c:\\Users\\hp\\Desktop\\MYCODE"
)

print("=== STDOUT ===")
print(result.stdout[-500:] if len(result.stdout) > 500 else result.stdout)
print("\n=== STDERR ===")
print(result.stderr[-500:] if len(result.stderr) > 500 else result.stderr)
print("\n=== Return Code ===")
print(result.returncode)
