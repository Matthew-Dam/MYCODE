#!/usr/bin/env python
# Quick test to verify the menu is working
import sys
sys.path.insert(0, 'c:\\Users\\hp\\Desktop\\MYCODE')

from My_app import run

print("Testing if application loads and menu responds...")
print("(Press Ctrl+C to test if the menu is responsive)")
try:
    run()
except KeyboardInterrupt:
    print("\nTest complete - menu is responsive!")
