# This function attempts to find a C4 (4-cycle) in an undirected graph.
# The graph is represented by an adjacency list, where G[u] contains the list of neighbors of vertex u.
# The algorithm uses a matrix 'Sasiedzi' to store the vertices that have been previously visited and their corresponding neighbors.
# It checks for a cycle of length 4 by traversing all pairs of neighbors for each vertex u.
# If it finds a C4 (a cycle of length 4), it returns the four vertices that form the cycle. If no such cycle is found, it returns an empty tuple.

def find_C4(G):
    n = len(G)
    neighbors = [[-1] * n for _ in range(n)]
    for u in range(n):
        for i in range(1, len(G[u])):
            for j in range(i):
                v = G[u][i]
                w = G[u][j]
                if neighbors[v][w] < 0:
                    neighbors[v][w] = neighbors[w][v] = u
                else:
                    return (v, neighbors[v][w], w, u)
    return ()  
