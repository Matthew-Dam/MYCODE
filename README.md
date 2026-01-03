# All-In-One Algorithm Collection

A comprehensive Python implementation of various graph algorithms including DFS, BFS, Dijkstra's Algorithm, and A* Search.

## Project Structure

- **ALL IN ONE/** - Main unified algorithm implementation
  - `ALL_IN_ONE.py` - Combined Graph class with multiple algorithms
  
- **astar/** - A* search algorithm implementations
  - `ASTAR.py` - Basic A* implementation
  - `Astar Algorithm 2.py` - Enhanced A* with coordinates
  - `ASTAR WITH COODINATES.PY` - A* with coordinate-based heuristics
  - `run_examples.py` - Example demonstrations

- **Root Level Implementations**
  - `Dijkstra's Algorithm.py` - Dijkstra's shortest path implementation
  - `DFS and BFS.py` - Depth-First and Breadth-First Search implementations

## Features

- **Graph Data Structure** - Flexible directed/undirected graph implementation
- **Dijkstra's Algorithm** - Efficient shortest path algorithm
- **A* Search** - Heuristic-based pathfinding with coordinate support
- **DFS & BFS** - Fundamental graph traversal algorithms
- **Distance Table** - Supporting data structure for shortest path calculations

## Getting Started

### Prerequisites
- Python 3.6+

### Usage

```python
from ALL_IN_ONE.ALL_IN_ONE import Graph, DistanceTable

# Create a graph
g = Graph(directed=False)

# Add edges
g.add_edges([(1, 2, 5)])
g.add_edges([(2, 3, 3)])

# Use algorithms
# (See individual files for detailed usage examples)
```

## Testing

Various test files are provided:
- `test_menu.py` - Interactive menu for testing
- `test_search_full.py` - Full search algorithm tests
- `final_test.py` - Comprehensive test suite

## License

MIT License - See LICENSE file for details

## Author

Created as a learning project for graph algorithms and pathfinding.
