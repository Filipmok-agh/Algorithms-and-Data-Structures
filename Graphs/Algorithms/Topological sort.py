# The following code implements **Topological Sorting** of a Directed Acyclic Graph (DAG).
# Topological sorting of a DAG is a linear ordering of vertices such that for every directed edge u -> v,
# vertex u comes before v in the ordering. This is useful for tasks like scheduling, task dependency resolution, etc.

def topological_sort(graph):
    def dfs_visit(graph, vertex):
        nonlocal sorted_list
        nonlocal time
        visited[vertex] = True
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                dfs_visit(graph, neighbor)
        time += 1
        sorted_list[n - time] = vertex

    num_vertices = len(graph)
    sorted_list = [None for _ in range(num_vertices)]
    time = 0
    visited = [False for _ in range(num_vertices)]
    
    for vertex in range(num_vertices):
        if not visited[vertex]:
            dfs_visit(graph, vertex)
    
    return sorted_list

def get_topological_order(graph):
    sorted_graph = topological_sort(graph)
    return sorted_graph