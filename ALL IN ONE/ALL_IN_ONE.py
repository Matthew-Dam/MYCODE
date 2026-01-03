# GRAPH CLASS FOR ALL THE ALGORITHMS

from collections import defaultdict,deque
import heapq
class Graph:
    def __init__(self,directed=False):
        self.directed = directed
        self.adjacency = defaultdict(list)

    def add_edges(self,edges): #edges = (u,v,w)
        u,v,w = [edge for edge in edges]
        self.adjacency[u].append((v,w))

        if not self.directed:
           self.adjacency[v].append((u,w))

    def confirm_edge(self,edge): # edge = (u-v)
        """ to confirm if edge exist, we only need u and v"""
        u,v = [node for node in edge]
        for neighbour,weight in self.adjacency[u]:
            if neighbour == v:
                return True
        return False

# DISTANCE TABLE FOR DIJKSTRA'S ALGORITHM

class DistanceTable:
    def __init__(self,graph,start,goal):
        self.graph = graph
        self.distances = {node:float("inf") for node in self.graph.adjacency}
        self.previous = {node:None for node in self.graph.adjacency}
        self.visited = {node:False for node in self.graph.adjacency}

    def update_distance(self,node,distance):
        self.distances[node] = distance

    def set_previous(self,child,parent):
        self.previous[child] = parent

    def mark_visited(self,node):
        self.visited[node] = True

    def get_distance(self,node):
        return self.distances.get(node,[])
    
    def is_visited(self,node):
        return self.visited.get(node,False)
    
    def get_neighbours(self,node):
        return self.graph.adjacency.get(node,[])
    
    def get_previous(self,node):
        return self.previous.get(node,[])

# COODINATES CLASS FOR A* ALGORITHM

class Coordinates:
    def __init__(self,graph):
        self.positions = {} # {node: (x,y)}
        self.graph = graph

    def add_position(self,node,x,y):
        if node not in self.graph.adjacency:
            raise KeyError('WARNING nod not on graph.')
            return None
        self.positions[node] = (x,y)


# HEURISTIC FUNCTION FOR A*
import math
def euclidean_heuristics(node,goal,position):
    x1,y1 = position.positions[node]
    x2,y2 = position.positions[goal]
    return math.hypot(x2-x1,y2-y1)

# ========BREATH FIRST SEARCH=========

def bfs(graph,start,goal):

    queue = deque([start])
    parent_map = {start:None}
    visited = set()

    while queue:
        node = queue.popleft()
        
        if node in visited:
            continue

        if node == goal:
            return reconstruct_path(parent_map,goal)

        for neighbour,_ in graph.adjacency.get(node,[]):
            if neighbour in visited:
                continue
            parent_map[neighbour] = node
            queue.append(neighbour)
        visited.add(node)
    
# =======DEPTH FIRST SEARCH=======
def dfs(graph,start,goal):

    parent_map = {start:None}
    visited = set()

    def explore(node):
        if node == goal:
            return reconstruct_path(parent_map,goal)
        visited.add(node)

        for neighbour,_ in graph.adjacency.get(node,[]):
            if neighbour not in visited:
                parent_map[neighbour] = node
                results = explore(neighbour)
                if results is not None:
                    return results
        return None
    return explore(start)

# =======DIJKSTRA'S ALGORITHM======
def dijkstra(graph,start,goal):
    heap = []
    table = DistanceTable(graph,start,goal)
    table.distances[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        cost,node = heapq.heappop(heap)

        if table.is_visited(node):
            continue
        
        table.mark_visited(node)

        if node == goal:
            return reconstruct_path(table.previous,goal)

        for neighbour,weight in table.get_neighbours(node):

            if weight < 0:
                raise ValueError("Warning: Negative weight detected.")
            
            new_cost = cost + weight

            if new_cost < table.distances[neighbour]:
                table.distances[neighbour] = new_cost
                table.set_previous(neighbour,node)
                heapq.heappush(heap,(new_cost,neighbour))

# ========A* ALGORITHM=========
def astar(graph,start,goal,position,heuristic):
    heap = []
    table = DistanceTable(graph,start,goal)
    table.distances[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        cost,node = heapq.heappop(heap)

        if table.is_visited(node):
            continue
        
        table.mark_visited(node)

        if node == goal:
            return reconstruct_path(table.previous,goal)

        for neighbour,weight in table.get_neighbours(node):

            if weight < 0:
                raise ValueError("Warning: Negative weight detected.")
            
            new_cost = cost + weight
            heuristic_cost = new_cost + heuristic(neighbour,goal,position)

            if new_cost < table.distances[neighbour]:
                table.distances[neighbour] = new_cost
                table.set_previous(neighbour,node)
                heapq.heappush(heap,(heuristic_cost,neighbour))

# RECONSTRUCT PATH FUNCTION
def reconstruct_path(previous_nodes,goal):
    path = []
    current_node = goal
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()
    return path
g = Graph(directed=False)

c = Coordinates(g)        
g.add_edges(('A','B',2))
g.add_edges(('A','C',4))
g.add_edges(('B','C',1))
g.add_edges(('B','D',7))
g.add_edges(('C','E',3))
g.add_edges(('D','F',1))
g.add_edges(('E','D',2))
g.add_edges(('E','F',5))


c.add_position('A',0,0)
c.add_position('B',1,2)
c.add_position('C',3,1)
c.add_position('D',4,3)
c.add_position('E',6,2)                                                                                                                                                                                                                                                                                                                             
c.add_position('F',7,4)


# Example usage:
path_bfs = bfs(g,'A','F')
path_dfs = dfs(g,'A','F')
path_dijkstra = dijkstra(g,'A','F')
path_astar = astar(g,'A','F',c,euclidean_heuristics)
print("BFS Path:",path_bfs)
print("DFS Path:",path_dfs)
print("Dijkstra's Path:",path_dijkstra)
print("A* Path:",path_astar)