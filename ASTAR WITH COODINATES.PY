
# A* ALGORITHM WITH COORDINATES

# GRAPH DEFINITION
class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self,u,v,w):
        self.edges.setdefault(u,[]).append((v,w))

# NODE POSITIONS ON 2D PLANE
positions = {
            "A":(0,0),
            "B":(1,2),
            "C":(3,1),
            "D":(4,3),
            "E":(6,2),
            "F":(7,4)
}

# HEURISTIC FUNCTION
import math
# EUCLIDEAN HEURISTIC
def heuristic(node,goal,position):
    x1,y1 = positions[node]
    x2,y2 = positions[goal]
    return math.hypot(x2-x1,y2-y1)

# A* IMPLEMENTATION
import heapq

# A* ALGORITHM
def astar(graph,start,goal,positions):
    
    # PRIORITY QUEUE
    open_set= []
    heapq.heappush(open_set,(0,start))

    # COST FROM START TO NODE
    g_score = {start:0}

    # TRACKING PATH
    came_from = {}

    # MAIN LOOP
    while open_set:

        # GET NODE WITH LOWEST F SCORE
        _,current = heapq.heappop(open_set)

        # CALCULATE SCORES
        g = g_score[current]
        h = heuristic(current,goal,positions)
        f = g + h

        # DEBUGGING OUTPUT
        print(f"Visiting {current} | g={g:.2f}, h={h:.2f}, f={f:.2f}")

        # GOAL CHECK
        if current == goal:
            return reconstruct_path(came_from,current),g
        
        # EXPLORE NEIGHBOURS
        for neighbour, cost in graph.edges.get(current,[]):
            
            # CALCULATE TENTATIVE G SCORE
            tentative_g = g + cost

            # UPDATE SCORES IF BETTER PATH FOUND
            if neighbour not in g_score or tentative_g < g_score[neighbour]:
                g_score[neighbour] = tentative_g
                came_from[neighbour] = current

                f_score = tentative_g + heuristic(neighbour,goal, positions)
            
                # ADD TO PRIORITY QUEUE
                heapq.heappush(open_set,(f_score,neighbour))

    # NO PATH FOUND
    return None, float("inf")

# PATH RECONSTRUCTION
def reconstruct_path(came_from,current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path[::-1]  # reverse the path

# EXAMPLE USAGE
graph = Graph()
graph.add_edge("A","B",2.2)
graph.add_edge("A","C",3.2)
graph.add_edge("B","D",2.5)
graph.add_edge("C","D",2.0) 
graph.add_edge("C","E",3.0)
graph.add_edge("D","F",2.2)
graph.add_edge("E","F",2.5)
path,cost = astar(graph,"A","F",positions)
print("Path found:",path)
print("Total cost:",cost)