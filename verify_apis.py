#!/usr/bin/env python
# Quick test to verify APIs load in My_app
import sys
sys.path.insert(0, 'c:\\Users\\hp\\Desktop\\MYCODE')

from My_app import Request

req = Request()
print("APIs loaded successfully!")
print(f"  OpenAI: {bool(req.openai_api)}")
print(f"  Gemini: {bool(req.gemini_api)}")
print(f"  News: {bool(req.news_api)}")
print(f"  Weather: {bool(req.weather_api)}")
