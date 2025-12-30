# DFS and BFS implementations with path reconstruction

# Depth-First Search (DFS) Stack-based implementation
def DFS(graph,start,destination=None):
    visited = set()
    stack = [start]
    dfs_parent_map = {start:None}

    while stack:
        node = stack.pop()

        if node in visited:
            continue
        
        visited.add(node)
        if destination is not None and node == destination:
            break

        for neighbour in graph.get(node,[]):
            if neighbour not in visited:
                dfs_parent_map[neighbour] = node
                stack.append(neighbour)
    return dfs_parent_map           

# Depth-First Search (DFS) Recursive implementation
def recursive_dfs(graph,start,destination =None):
    visited = set()
    recursive_parent_map = {start:None}

    def explore(node):
        if destination is not None and node == destination:
            return

        visited.add(node)
        for neighbour in graph.get(node,[]):
            if neighbour not in visited:
                recursive_parent_map[neighbour] = node
                explore(neighbour)
    explore(start)
    return recursive_parent_map
            
# Breadth-First Search (BFS) implementation        
def BFS(graph,start,destination=None):
    visited = set()
    queue = [start]
    bfs_parent_map = {start:None}

    while queue:
        current = queue.pop(0)
        visited.add(current)

        if destination is not None and current == destination:
            break

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                bfs_parent_map[neighbor] = current
                queue.append(neighbor)

    return bfs_parent_map

# Path reconstruction from parent map
def reconstruct_path(parent_map,destination):
    path = []
    cur = destination
    while cur:
        path.append(cur)
        cur = parent_map[cur]

    path.reverse()
    return path