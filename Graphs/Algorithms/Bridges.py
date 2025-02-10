# The function find_bridges uses DFS to find the bridges in an undirected graph.
# Bridges are edges whose removal increases the number of connected components in the graph.
# The algorithm runs in O(V + E) time, where V is the number of vertices and E is the number of edges.
# It returns a list of bridges, which are pairs of vertices that form the bridge edge.

def find_bridges(graph):
    n = len(graph)
    time = 0
    discovery_time = [0 for _ in range(n)]
    low = [0 for _ in range(n)]
    bridges = []

    def dfs(vertex, parent):
        nonlocal time
        time += 1
        discovery_time[vertex] = time
        low[vertex] = time

        for neighbor in graph[vertex]:
            if discovery_time[neighbor] == 0:
                dfs(neighbor, vertex)
                if low[neighbor] < low[vertex]:
                    low[vertex] = low[neighbor]
            elif neighbor != parent:
                if discovery_time[neighbor] < low[vertex]:
                    low[vertex] = discovery_time[neighbor]

        if discovery_time[vertex] == low[vertex] and parent >= 0:
            bridges.append((parent, vertex))

    dfs(0, -1)
    return bridges
