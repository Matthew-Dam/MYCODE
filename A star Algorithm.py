# A* Algorithm Implementation
import heapq
# A node ono a grid
class Node:
    def __init__(self,position,parent=None):
        self.position = position
        self.parent = parent
        self.g = 0 # cost from start
        self.h = 0 # heuristic cost to goal
        self.f = 0 # total cost

    def __it__(self,other):
        return self.f < other.f # for heapq priority
    
# Heuristic: Straight-line distance (Euclidean)
def heuristic(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

# A* ALGORITHM IMPLEMENTATION
def astar(grid,start,goal):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    goal_node = Node(goal)

    heapq.heappush(open_list,start_node)

    while open_list:
        current = heapq.heappop(open_list)
        closed_set.add(current.position)

        if current.position == goal_node.position:
            #reconstruct path
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]
        
        # explore neighbours (4 directional)
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            neighbour_pos = (current.position[0]+dx,current.position[1]+dy)

            if (0 <= neighbour_pos[0] < len(grid) and
                0 <= neighbour_pos[1] < len(grid[0]) and
                grid[neighbour_pos[0]][neighbour_pos[1]] == 0 and
                neighbour_pos not in closed_set):

                neighbour = Node(neighbour_pos,current)
                neighbour.g = current.g + 1
                neighbour.h = heuristic(neighbour_pos,goal)
                neighbour.f = neighbour.g + neighbour.h

                # if neighbour already in open with lower f, skip
                if any(n.position == neighbour.position and n.f <= neighbour.f for n in open_list):
                    continue

                heapq.heappush(open_list,neighbour)

    return None


grid = [
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,1,0],
    [0,1,0,0,0],
    [0,0,0,1,0]
]
start = (0,0)
goal = (4,4)

path = astar(grid,start,goal)
print(f"Path found: {path}")