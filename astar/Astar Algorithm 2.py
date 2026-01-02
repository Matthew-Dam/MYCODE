# A* ALGORITHM USING ADJACENCY LIST WITH WEIGHTS.

import heapq
class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self,u,v,weight):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append((v,weight))
    
# HEURISTIC FUNCTION
def heuristic(node,goal,h_value):
    return h_values.get(node, float('inf'))

# A* algorithm function
def a_star(graph,start,goal,h_values):
    open_set = []

    heapq.heappush(open_set,(0,start))

    came_from = {}
    g_score = {start:0}

    while open_set:
        _,current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from,current), g_score[current]
        
        for neighbour,cost in graph.edges.get(current,[]):
            tentative_g = g_score[current] + cost

            if neighbour not in g_score or tentative_g < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g
                f_score = tentative_g + heuristic(neighbour,goal,h_values)
                heapq.heappush(open_set,(f_score,neighbour))

    return None, float('inf')

#PATH RECONSTRUCTION
def reconstruct_path(came_from ,current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

if '__main__' == __name__:
    graph = Graph()

    graph.add_edge('A','B',1)
    graph.add_edge('A','C',4)
    graph.add_edge('B','C',2)
    graph.add_edge('B','D',5)
    graph.add_edge('C','D',1)
    graph.add_edge('D','E',3)
    graph.add_edge('B','E',12)
    graph.add_edge('C','E',6)
    graph.add_edge('E','F',2)
    graph.add_edge('D','F',4)

    h_values = {
        'A':7,
        'B':6,
        'C':2,
        'D':1,
        'E':0,
        'F':0
    }

    path, cost = a_star(graph, 'A', 'F', h_values)
    print("Shortest path:", path)
    print("Total cost:", cost)