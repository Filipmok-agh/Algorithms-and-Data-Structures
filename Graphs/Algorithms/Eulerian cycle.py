from queue import Queue

# Function to check if the graph is connected using BFS
def is_connected(graph):
    queue = Queue()
    num_vertices = len(graph)
    visited = [False for _ in range(num_vertices)]
    visited[0] = True
    queue.put(0)
    
    while not queue.empty():
        vertex = queue.get()
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.put(neighbor)
    
    for is_visited in visited:
        if not is_visited:
            return False
    return True

# Function to determine the type of graph based on the degree of vertices
def get_graph_type(graph):
    odd_degree_count = 0
    num_vertices = len(graph)
    starting_vertex = 0
    
    if not is_connected(graph):
        return 0, 0
    
    for vertex in range(num_vertices):
        if len(graph[vertex]) % 2 == 1:
            odd_degree_count += 1
            starting_vertex = vertex
    
    if odd_degree_count == 0:
        return 1, starting_vertex
    if odd_degree_count == 2:
        return 2, starting_vertex
    else:
        return 0, 0

# Function to find Eulerian path or circuit
def find_eulerian_path(graph):
    graph_type, start_vertex = get_graph_type(graph)
    if graph_type == 0:
        return False, False
    
    num_vertices = len(graph)
    visited_edges = [[False for _ in range(num_vertices)] for _ in range(num_vertices)]
    eulerian_path = []
    
    def dfs(vertex):
        for neighbor in graph[vertex]:
            if not visited_edges[vertex][neighbor]:
                visited_edges[vertex][neighbor] = True
                visited_edges[neighbor][vertex] = True
                dfs(neighbor)
        eulerian_path.append(vertex)
    
    dfs(start_vertex)
    return eulerian_path, graph_type

