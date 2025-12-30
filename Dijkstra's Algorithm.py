#MY FIRST DIJKSTRA'S ALGORITHM CODE ON COMPUTER

# I  imported (HEAPQ) for minheap priority queue
import heapq

# I created a graph class for my vertices and edges
class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = {}

# i created a method to add edges to the graph which takes edges (u,v,weight) as an arguments
    def add_edges(self, edges):
        for u, v, weight in edges:
            if u not in self.adj_list:
                self.adj_list[u] = []
            self.adj_list[u].append((v, weight))
            if not self.directed:
                if v not in self.adj_list:
                    self.adj_list[v] = []
                self.adj_list[v].append((u, weight))

# I created a method to check if an edge exists between two vertices
    def check_edge(self, u, v):
        if u in self.adj_list:
            for neighbor, weight in self.adj_list[u]:
                if neighbor == v:
                    return True
        return False
    
# I created a method to remove an edge between two vertices
    def remove_edge(self, u, v):
        if u in self.adj_list:
            self.adj_list[u] = [(neighbor, weight) for neighbor, weight in self.adj_list[u] if neighbor != v]
        if not self.directed and v in self.adj_list:
            self.adj_list[v] = [(neighbor, weight) for neighbor, weight in self.adj_list[v] if neighbor != u]

# I created DistanceTable class to keep track of distances, visited nodes, and previous nodes
class DistanceTable:
    def __init__(self,graph):
        self.graph = graph
        self.distances = {node:float('inf') for node in graph.adj_list}
        self.visited = {node:False for node in graph.adj_list}
        self.previous_nodes = {node:None for node in graph.adj_list}

# I created methods to update and retrieve distances, neighbors, visited status, and previous nodes
    def update_distance(self, node, distance):
        self.distances[node] = distance

    def get_distance(self, node):
        return self.distances.get(node, float('inf'))
    
    def get_neighbors(self, node):
        return self.graph.adj_list.get(node, [])
    
    def mark_visited(self, node):
        self.visited[node] = True

    def is_visited(self, node):
        return self.visited.get(node, False)
    
    def set_previous(self, node, previous):
        self.previous_nodes[node] = previous

    def get_previous(self, node):
        return self.previous_nodes.get(node, None)

# I implemented Dijkstra's algorithm using a priority queue (min-heap)
def dijkstra(graph,start,destination):
    table = DistanceTable(graph)
    heap = [(0,start)]
    table.distances[start] = 0

    while heap:
        current_dist,current_node = heapq.heappop(heap)
        if table.visited[current_node]:
            continue

        table.mark_visited(current_node)
        if destination is not None and current_node == destination:
            break

        for neighbour,weight in table.get_neighbors(current_node):
            if weight < 0:
                raise ValueError("Error occured weight must be positive")
            
            new_distance = current_dist + weight
            if new_distance < table.distances[neighbour]:
                table.distances[neighbour] = new_distance
                table.set_previous(neighbour, current_node)
                heapq.heappush(heap,(new_distance,neighbour))


# I return the distances and previous nodes from the distance table
    return table.distances,table.previous_nodes

def get_path(previous_nodes,start,destination):
    path = []
    current_node = destination
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path.reverse()
    if path[0] == start:
        return path
    else:
        return []
if __name__ == "__main__":
    graph = Graph(directed=True)
    graph.add_edges([ ('A','B',1),
                        ('B','C',2),
                        ('A','C',4),
                        ('C','D',1),
                        ('B','D',5),
                        ('D','E',3),
                        ('C','E',2),
                        ('E','F',1),
                        ('D','F',2),
                        ('B','F',10),
                        ('A','F',15),
                        ('E','A',7),
                        ('F','A',12),
                        ('F','B',6),
                        ('E','C',4),
                        ('D','B',8),
                        ('C','B',9),
                        ('D','C',3),
                        ('E','D',5),
                        ('F','E',2),
                        ('B','A',11),
                        ('C','A',13),
                        ('D','A',14),
                        ('F','D',4),
                        ('E','B',1),
                        ('A','E',9),
                        ('B','E',2),
                        ('C','F',3),
                        ('D','F',7),
                        ('E','F',8),
                        ('F','C',5),
                        ('A','D',10)])
    start = 'A'
    destination = 'F'
    distances, previous_nodes = dijkstra(graph, start, destination)
     
    path = get_path(previous_nodes, start, destination)
    print(f"Shortest path from {start} to {destination}: {path}")

  
