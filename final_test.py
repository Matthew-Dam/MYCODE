#!/usr/bin/env python
# Test menu navigation and basic functionality
import subprocess
import sys

# Simple test: navigate menu and exit
input_sequence = "2\n3\n2\n4\n"

result = subprocess.run(
    [sys.executable, "My_app.py"],
    input=input_sequence,
    capture_output=True,
    text=True,
    cwd="c:\\Users\\hp\\Desktop\\MYCODE",
    timeout=5
)

print("=== Menu Test Results ===")
print(result.stdout)
print("\nReturn code:", result.returncode)
if result.returncode == 0:
    print("✓ Application works correctly!")
else:
    print("Error:", result.stderr[-500:])
