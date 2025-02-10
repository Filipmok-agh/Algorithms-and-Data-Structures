# Mokrzycki Filip
# I create an adjacency list and then use Dijkstra's algorithm to find the shortest path from a to the singularity
# and from b to the singularity. At the same time, I also find the shortest path from a to b without considering the singularity.
# The shortest path from a to b is the minimum value between (a to singularity + b to singularity) or a to b without considering the singularity.
# Time complexity: O(2*len(E)*log(n))

from zad5testy import runtests
from queue import PriorityQueue
from math import inf

def spacetravel(n, edges, singularities, a, b):
    graph = [[] for _ in range(n)]
    for start, end, weight in edges:
        graph[start].append([end, weight])
        graph[end].append([start, weight])

    def dijkstra(graph, source):
        distances = [inf for _ in range(n)]
        visited = [False for _ in range(n)]
        distances[source] = 0

        def relax(u, v, weight):
            if distances[v] > distances[u] + weight:
                distances[v] = distances[u] + weight
                priority_queue.put((distances[v], v))

        priority_queue = PriorityQueue()
        priority_queue.put((distances[source], source))

        while not priority_queue.empty():
            dist, u = priority_queue.get()
            if not visited[u]:
                visited[u] = True
                for neighbor, weight in graph[u]:
                    relax(u, neighbor, weight)

        return distances

    dist_a = dijkstra(graph, a)
    dist_b = dijkstra(graph, b)

    min_distance_ab = dist_a[b]

    min_dist_a_to_singularity = inf
    min_dist_b_to_singularity = inf

    for i in range(n):
        if i in singularities:
            min_dist_a_to_singularity = min(min_dist_a_to_singularity, dist_a[i])
            min_dist_b_to_singularity = min(min_dist_b_to_singularity, dist_b[i])

    min_distance_ab = min(min_distance_ab, min_dist_a_to_singularity + min_dist_b_to_singularity)

    if min_distance_ab == inf:
        min_distance_ab = None

    return min_distance_ab

runtests(spacetravel, all_tests=True)
input("Press Enter to exit...")
