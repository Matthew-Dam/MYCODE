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
now organized under the `astar/` directory; run them individually or use the
interactive runner.

- `astar/ASTAR.py`: Core A* implementation (single-file reference implementation).
- `astar/A star Algorithm.py`: Alternate A* example with a different input format.
- `astar/Astar Algorithm 2.py`: A second variant, shows path reconstruction and
  heuristics tuning.
- `astar/ASTAR TUTORIAL 3.py`: A tutorial-style walkthrough with inline
  explanation and example grids.
- `astar/Astar tutorial 4.py`: Another tutorial example focusing on performance
  and optimizations.
- `astar/ASTAR WITH COODINATES.PY`: A variant that demonstrates coordinate-based
  inputs and visualization helpers.

Run examples

From the repository root you can run the interactive runner which lists the
examples and executes the selected one:

```bash
python astar/run_examples.py
```

If you prefer, run an example directly, for example:

```bash
python astar/ASTAR.py
```

