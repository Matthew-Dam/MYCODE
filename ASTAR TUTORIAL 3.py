class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self,u,v,w):
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append((v,w))

class Coordinates:
    def __init__(self,graph):
        self.graph = graph
        self.positions = {}

    def add_position(self,node,x,y):
        if node not in self.graph.edges:
            raise KeyError(f"{node} not on graph.")
            return None
        self.positions[node] = (x,y)

    
import math
def heuristic(node,goal,position):
    x1,x2 = position.positions[node]
    y1,y2 = position.positions[goal]
    return math.hypot(x2 - x1, y2 - y1)

import heapq   
def astar(graph,start,goal,position):
    open_set =[]

    heapq.heappush(open_set,(0,start))

    g_score = {start:0}
    came_from = {}

    while open_set:
        _,current = heapq.heappop(open_set)

        g = g_score[current]
        h = heuristic(current,goal,position)
        f = g + h

        print(f"Visiting : {current} | g={g:.2f}, h={h:.2f}, f={f:.2f}")

        if current == goal:
            return reconstruct_path(came_from,current),g
        
        for neighbour,cost in graph.edges.get(current,[]):
            tentative_g = g + cost

            if neighbour not in g_score or tentative_g < g_score[neighbour]:
                g_score[neighbour] = tentative_g
                came_from[neighbour] = current

                f_score = tentative_g + heuristic(neighbour,goal,position)
                heapq.heappush(open_set,(f_score,neighbour))

    return None, float("inf")

def reconstruct_path(came_from,current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]


if "__main__"==__name__:
    graph = Graph()
    position = Coordinates(graph)

    graph.add_edge("A","B",2.2)
    graph.add_edge("A","C",3.2)
    graph.add_edge("B","D",2.5)
    graph.add_edge("C","D",2.0) 
    graph.add_edge("C","E",3.0)
    graph.add_edge("D","F",2.2)
    graph.add_edge("E","F",2.5)
    graph.add_edge("G","F",1.5)
    graph.add_edge("E","H",3.5)
    graph.add_edge("F","H",4.5)
    graph.add_edge("H","A",2.5)

    position.add_position("A",0,1)
    position.add_position("B",2,1)
    position.add_position("C",4,2)
    position.add_position("D",2,4)
    position.add_position("E",3,5)
    position.add_position("F",1,4)
    position.add_position("G",4,1)
    position.add_position("H",5,0)

    path,cost = astar(graph,"A","F",position)

    print(f"Path found : {path}")
    print(f"Total cost : {cost}")



        
