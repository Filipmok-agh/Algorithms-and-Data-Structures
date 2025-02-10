# I transform my edge-weight array into an adjacency list with weights.
# Then for vertex x, I trigger a DFS for each of its neighbors recursively,
# simultaneously checking the maximum threshold.
# If the discrepancy is too large, the recursion backtracks.
# If the vertex reached is y, I end the call and return True.
# If I visit all vertices and don't reach y, it means it's not possible, and I return False.
# Time complexity: O(e!)

from zad4testy import runtests

def Flight(edges, x, y, t):
    n = len(edges)
    max_weight = 0
    for i in range(n):
        max_weight = max(edges[i][0], edges[i][1], max_weight)
    
    graph = [[] for _ in range(max_weight + 1)]
    for i in range(n):
        graph[edges[i][0]].append([edges[i][1], edges[i][2]])
        graph[edges[i][1]].append([edges[i][0], edges[i][2]])

    num_vertices = len(graph)
    visited = [False for _ in range(num_vertices)]

    def DFS(u, min_weight, max_weight):
        if max_weight - min_weight > 2 * t:
            return False
        if u == y:
            return True
        visited[u] = True
        for neighbor in graph[u]:
            if not visited[neighbor[0]]:
                if DFS(neighbor[0], min(min_weight, neighbor[1]), max(max_weight, neighbor[1])):
                    return True
        visited[u] = False
        return False

    for start in graph[x]:
        if DFS(start[0], start[1], start[1]):
            return True

    return False

runtests(Flight, all_tests=True)
input("Press Enter to exit...")
