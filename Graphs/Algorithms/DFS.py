# This function implements Depth-First Search (DFS) on a directed graph represented by an adjacency list.
# The DFS function traverses the graph, marking the time of entry (previsit) and exit (postvisit) for each vertex.
# It also tracks the parent of each vertex and stores the discovery and finishing times for all vertices.
# The function is recursive, and a helper function DFSvisit is used to explore the graph recursively.
# The DFS traversal is performed for every unvisited vertex in the graph.

def DFS(G):
    def DFSvisit(G, v):
        nonlocal time
        time += 1
        visited[v] = True
        przejscie[v] = time
        for i in G[v]:
            if visited[i] == False:
                parent[i] = v
                DFSvisit(G, i)
        time += 1
        przetworzenie[v] = time

    n = len(G)
    time = 0
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    przejscie = [-1 for _ in range(n)]
    przetworzenie = [-1 for _ in range(n)]
    for v in range(n):
        if visited[v] == False:
            DFSvisit(G, v)
