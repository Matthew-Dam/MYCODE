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

A* Algorithms

The repository includes several A* algorithm examples/tutorials. They are
kept as separate scripts (raw examples and tutorial variants). Brief notes
below — run them individually with `python <filename>`.

- `Astar.py`: Core A* implementation (single-file reference implementation).
- `A star Algorithm.py`: Alternate A* example with different input format.
- `Astar Algorithm 2.py`: A second variant, shows path reconstruction and
  heuristics tuning.
- `ASTAR TUTORIAL 3.py`: A tutorial-style walkthrough with inline
  explanation and example grids.
- `Astar tutorial 4.py`: Another tutorial example focusing on performance
  and optimizations.
- `ASTAR WITH COODINATES.PY`: A variant that demonstrates coordinate-based
  inputs and visualization helpers.

Recommended next steps

- If you want these examples organized, I can move them into an `astar/`
  folder and add a small `examples/` runner. Tell me if you'd like that.

