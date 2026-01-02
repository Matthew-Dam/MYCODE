# MYCODE

`My_app.py` — Multi-request console application

This repository contains `My_app.py`, a console utility that bundles several
interactive features:

- `get_weather` — current weather via OpenWeatherMap
- `daily_news` — news search via NewsAPI
- `chat` — Gemini (Google) or OpenAI chat interface
- `search` — DuckDuckGo instant answer search

Setup

1. Create or update `APIs.env` in the repository root with the following keys:

```
OPENAI_API_KEY=...
GEMINI_API_KEY=...
NEWS_API_KEY=...
WEATHER_API_KEY=...
```

2. Install dependencies (example):

```bash
pip install -r requirements.txt
# or at minimum: pip install requests python-dotenv colorama google-genai openai
```

Run

```bash
python My_app.py
```

Notes

- This project is a single multi-request application, not solely algorithm
  demos such as Dijkstra/BFS/DFS. The module header and this README reflect
  that intent.
