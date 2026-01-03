#!/usr/bin/env python
# Test the search app output with pause
import subprocess
import sys

# Create input: move to search app (4 moves), run it with a test search, exit
input_sequence = "2\n2\n2\n1\npython\nexit\n4\n"

# Run the app with the input
result = subprocess.run(
    [sys.executable, "My_app.py"],
    input=input_sequence,
    capture_output=True,
    text=True,
    cwd="c:\\Users\\hp\\Desktop\\MYCODE",
    timeout=10
)

print("=== OUTPUT ===")
print(result.stdout[-1500:])  # Last 1500 chars
print("\n=== Return Code ===")
print(result.returncode)
