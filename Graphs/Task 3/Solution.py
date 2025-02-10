from zad6testy import runtests
from math import inf
from queue import PriorityQueue

# Solution where we don't create new nodes, but "pretend" they exist
# We distinguish between them in the queue using a Flag - F.
# Depending on which vertex is delivered to the queue, we perform the corresponding relaxation.
# The shortest path is the min(path to "real", path to "fake").
# Time complexity: O(V^3)

def jumper(G, s, w):
    n = len(G)
    graph = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                graph[i].append([j, G[i][j]])

    def dikstra(T, p, k):
        dist = [[inf, inf] for _ in range(n)]

        def relax_real(u, v, weight):
            previous = dist[v][0]
            dist[v][0] = min(dist[v][0], dist[u][0] + weight, dist[u][1] + weight)
            if dist[v][0] != previous:
                Q.put((dist[v][0], v, True))

        def relax_fake(u, v, weight):
            previous = dist[v][1]
            for neighbor, w in T[u]:
                dist[v][1] = min(dist[v][1], max(weight, w) + dist[neighbor][0])
            if dist[v][1] != previous:
                Q.put((dist[v][1], v, False))

        dist[p][0] = 0
        dist[p][1] = 0
        
        Q = PriorityQueue()
        Q.put((0, p, True))

        while not Q.empty():
            d, u, F = Q.get()
            for idx, weight in T[u]:
                if F:
                    relax_fake(u, idx, weight)
                relax_real(u, idx, weight)

        return min(dist[k][0], dist[k][1])

    return dikstra(graph, s, w)


runtests(jumper, all_tests=True)
input("Press Enter to exit...")
