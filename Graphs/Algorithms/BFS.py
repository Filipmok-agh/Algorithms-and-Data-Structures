# Breadth-First Search (BFS) algorithm for unweighted graphs
# BFS explores the graph level by level starting from the source vertex.
# It uses a queue to ensure that vertices are explored in the order they are discovered.
# The algorithm computes the shortest path in terms of the number of edges from the source to all other vertices.
# Time complexity: O(V + E) of vertices and E is the number of edges.

from queue import Queue

def BFS(G, s):
    Q = Queue()
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    dist = [-1 for _ in range(n)]
    
    visited[s] = True
    parent[s] = None
    dist[s] = 0
    Q.put(s)
    
    while not Q.empty():
        u = Q.get()
        for i in G[u]:
            if not visited[i]:
                visited[i] = True
                dist[i] = dist[u] + 1
                parent[i] = u
                Q.put(i)
    
    return dist, parent, visited
