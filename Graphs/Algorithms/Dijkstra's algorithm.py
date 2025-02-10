from math import inf
from queue import PriorityQueue

# Dijkstra's algorithm to find the shortest paths from a given source vertex to all other vertices
# in a weighted, directed graph. The graph is represented as an adjacency list where each element
# contains a list of neighboring vertices and the weights of the edges connecting them. The algorithm
# uses a priority queue to efficiently select the vertex with the smallest tentative distance. The time
# complexity of the algorithm is O(E log V), where E is the number of edges and V is the number of vertices.

def dijkstra_single_source(graph, source):
    num_vertices = len(graph)
    distances = [inf for _ in range(num_vertices)]
    visited = [False for _ in range(num_vertices)]
    distances[source] = 0
    predecessors = [None for _ in range(num_vertices)]  

    def relax_edge(u, v, weight):
        if distances[v] > distances[u] + weight:
            distances[v] = distances[u] + weight
            priority_queue.put((distances[v], v))
            predecessors[v] = u

    priority_queue = PriorityQueue()
    priority_queue.put((distances[source], source))
    
    while not priority_queue.empty():
        current_distance, current_vertex = priority_queue.get()
        if not visited[current_vertex]:
            visited[current_vertex] = True
            for neighbor, weight in graph[current_vertex]:
                relax_edge(current_vertex, neighbor, weight)
    
    return distances, predecessors
