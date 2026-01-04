# DFS and BFS implementations with path reconstruction

from collections import deque

# Depth-First Search (DFS) Stack-based implementation
def DFS(graph, start, destination=None):
    """Iterative DFS using a stack. Marks nodes as seen when pushed to avoid
    multiple discoveries and to preserve the first-discovery parent.
    """
    seen = {start}
    stack = [start]
    dfs_parent_map = {start: None}

    while stack:
        node = stack.pop()

        if destination is not None and node == destination:
            break

        # reverse the neighbors so that the visitation order matches
        # the order in the adjacency list (optional)
        for neighbour in reversed(graph.get(node, [])):
            if neighbour not in seen:
                seen.add(neighbour)
                dfs_parent_map[neighbour] = node
                stack.append(neighbour)
    return dfs_parent_map

# Depth-First Search (DFS) Recursive implementation
def recursive_dfs(graph, start, destination=None):
    """Recursive DFS that propagates an early-stop when destination is found."""
    seen = {start}
    recursive_parent_map = {start: None}
    found = False

    def explore(node):
        nonlocal found
        if found:
            return True
        if destination is not None and node == destination:
            found = True
            return True

        for neighbour in graph.get(node, []):
            if neighbour not in seen:
                seen.add(neighbour)
                recursive_parent_map[neighbour] = node
                if explore(neighbour):
                    return True
        return False

    explore(start)
    return recursive_parent_map

# Breadth-First Search (BFS) implementation
def BFS(graph, start, destination=None):
    """BFS using deque and marking nodes as seen when enqueued to avoid
    duplicates and to ensure parents reflect first-discovery."""
    seen = {start}
    queue = deque([start])
    bfs_parent_map = {start: None}

    while queue:
        current = queue.popleft()

        if destination is not None and current == destination:
            break

        for neighbor in graph.get(current, []):
            if neighbor not in seen:
                seen.add(neighbor)
                bfs_parent_map[neighbor] = current
                queue.append(neighbor)

    return bfs_parent_map

# Path reconstruction from parent map
def reconstruct_path(parent_map, destination):
    """Reconstruct the path from start to destination using parent_map.

    Returns a list of nodes from start to destination, or None if destination
    was not reached (not present in parent_map).
    """
    if destination not in parent_map:
        return None

    path = []
    cur = destination
    while cur is not None:
        path.append(cur)
        cur = parent_map.get(cur)

    path.reverse()
    return path
