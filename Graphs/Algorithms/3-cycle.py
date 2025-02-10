# This function checks whether there is a cycle in a graph represented by an adjacency matrix.
# It uses a Breadth-First Search (BFS) approach to traverse the graph.
# The graph is represented as an adjacency matrix, where M[i][j] == 1 indicates an edge between node i and node j.
# The algorithm checks for back edges during traversal, which are indicative of a cycle in an undirected graph.
# If a cycle is detected, the function returns True, otherwise, it returns False.

from queue import Queue

def has_cycle(adjacency_matrix):
    num_nodes = len(adjacency_matrix)
    visited = [False] * num_nodes
    parent = [-1] * num_nodes
    queue = Queue()

    queue.put(0)
    visited[0] = True

    while not queue.empty():
        current_node = queue.get()

        for neighbor in range(num_nodes):
            if adjacency_matrix[current_node][neighbor] == 1:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = current_node
                    queue.put(neighbor)
                elif parent[current_node] != neighbor:
                    return True
    return False
