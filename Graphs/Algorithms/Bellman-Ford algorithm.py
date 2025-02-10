# Bellman-Ford algorithm for finding the shortest paths from a source vertex to all other vertices
# The algorithm works by iteratively relaxing all edges n-1 times, where n is the number of vertices.
# After the n-1 iterations, it checks for negative-weight cycles by trying to relax the edges once more.
# If any edge can still be relaxed, a negative-weight cycle is detected.
# Time complexity: O(V * E), where V is the number of vertices and E is the number of edges.

from math import inf

def bellman_ford(graph, source):
    n = len(graph)
    dist = [inf] * n
    dist[source] = 0
    parent = [None] * n

    def relax(u, v, weight):
        if dist[v] > dist[u] + weight:
            dist[v] = dist[u] + weight
            parent[v] = u

    for _ in range(n - 1):
        for u in range(n):
            for v, weight in graph[u]:
                relax(u, v, weight)

    for u in range(n):
        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                return False
    return dist
