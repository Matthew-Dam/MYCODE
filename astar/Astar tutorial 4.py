# A* ALGORITHM ON WEIGHTED GRAPH WITHOUT COODINATES


from collections import deque,defaultdict

# BREADTH FIRST SEARCH TO COMPUTE MINIMUM EDGES
def bfs(graph,start,goal):
    '''Return minimum number of edges from start to goal ignoring weights'''
    queue = deque([(start,0)])
    visited = set()

    while queue:
        node,edges = queue.popleft()
        if node == goal:
            return edges
        if node in visited:
            continue
        visited.add(node)

        for neighbour,_ in graph.get(node,[]):
            if neighbour not in visited:
                queue.append((neighbour,edges+1))
    return float("inf")

# ADMISSIBLE HEURISTIC FUNCTION
def heuristic(graph,node,goal):
    '''Compute admissible heuristic: min_edges * min_dege_cost leaving node'''
    min_edges = bfs(graph,node,goal)

    #Find smallest ongoing edges cost from this node
    edges = graph.get(node,[])

    if edges:
        min_edge_cost = min(cost for _,cost in edges)
    else:
        min_edge_cost = 0

    return min_edges * min_edge_cost

# GRAPH DEFINITION
graph = {
    'A': [('B',1),('C',4)],
    'B': [('A',1),('C',2),('D',5)],
    'C': [('A',4),('B',2),('D',1)],
    'D': [('B',5),('C',1)]
}

import heapq

# A* ALGORITHM IMPLEMENTATION
def astar(graph,start,goal):
    open_set = []
    g_score = {start:0}

    came_from = {}

    heapq.heappush(open_set,(0,start))

    while open_set:
        _,current = heapq.heappop(open_set)

        g = g_score[current]
        h = heuristic(graph,current,goal)
        f = g + h

        print(f"Visiting : {current} | g={g:.2f}, h={h:.2f}, f={f:.2f}")

        if current == goal:
            return reconstruct_path(came_from,current),g
        
        for neighbour,cost in graph.get(current,[]):
            new_g = g + cost

            if neighbour not in g_score or new_g < g_score[neighbour]:
                g_score[neighbour] = new_g
                came_from[neighbour] = current

                f_score = new_g + heuristic(graph,neighbour,goal)
                heapq.heappush(open_set,(f_score,neighbour))
    return None, float("inf")


def reconstruct_path(came_from,current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

if "__main__" == __name__:

    path,cost = astar(graph,"A","D")
    print(f"Path found: {path} with total cost: {cost:.2f}")