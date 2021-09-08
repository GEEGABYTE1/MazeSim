from graph import*
from heapq import heappop, heappush
from math import inf, sqrt 

def man_heuristic(start, target):
    x_distance = abs(start.position[0] - target.position[0])
    y_distance = abs(start.position[1] - target.position[1])
    return x_distance + y_distance 

def eu_heuristic(start, target):
    x_distance = abs(start.position[0] - target.position[0])
    y_distance = abs(start.position[1] - target.position[1])

def a_star(graph, start, target):
    count = 0
    paths_and_distance = {}
    for vertex in graph.keys():
        paths_and_distance[vertex] = [inf, [start.value]]
    
    paths_and_distance[start][0] = 0 
    vertices_to_explore = [(0, start)]
    while vertices_to_explore and paths_and_distance[target][0] == inf:
        current_distance, current_vertex = heappop(vertices_to_explore)
        for neighbour, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight + man_heuristic(neighbour, target)
            new_path = paths_and_distance[current_vertex][1] + [neighbour.value]

            if new_distance < paths_and_distance[neighbour][0]:
                paths_and_distance[neighbour][0] = new_distance
                paths_and_distance[neighbour][1] = new_path 
                heappush(vertices_to_explore, (new_distance, neighbour))
                count += 1
    
    print('Path found in {num} steps'.format(num=count))
    return paths_and_distance[target][1]



dictionary = {}
for vertex, edge in graph.graph_dict.items():
    for vertex_obj in objects:
        if vertex == vertex_obj.value:
            new_lst = []
            edges = edge.edges
            for neighbour, weight in edges.items():
                for neighbour_obj in objects:
                    if neighbour_obj.value == neighbour:
                        new_lst.append((neighbour_obj, weight))
        
            dictionary[vertex_obj] = new_lst 


