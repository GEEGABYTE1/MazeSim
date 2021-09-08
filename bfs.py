from nodes import graph

def bfs(graph, start_vertex, target):
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    bfs_queue = [vertex_and_path]
    visited = set()

    while bfs_queue:
        current_vertex,  path = bfs_queue.pop()
        visited.add(current_vertex)
        try:
            for neighbour in graph[current_vertex]:
                if not neighbour in visited:
                    if neighbour == target:
                        path.append(neighbour)
                        return path 
                    else:
                        path.append(neighbour)
                        bfs_queue.append([neighbour, path])
        except KeyError:
            break
        
    return None

bfs_graph = {}

for vertex, edge in graph.graph_dict.items():
    lst = []
    edge = edge.edges 
    for neighbour in edge.keys():
        lst.append(neighbour)
    
    bfs_graph[vertex] = lst 




