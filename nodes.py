from graph import*
from vertex import Vertex

graph = Graph(True)

objects = []

vertex_one = Vertex('a', 1, 5)
vertex_two = Vertex('b', 1, 10)
vertex_three = Vertex('c', 1, 15)

vertex_four = Vertex('d', 2, 6)
vertex_five = Vertex('e', 2, 12)
vertex_six = Vertex('*', 2, 18)

vertex_seven = Vertex('f', 3, 7)
vertex_eight = Vertex('g', 3, 14)
vertex_nine = Vertex('h', 3, 21)

objects.append(vertex_one)
objects.append(vertex_two)
objects.append(vertex_three)
objects.append(vertex_four)
objects.append(vertex_five)
objects.append(vertex_six)
objects.append(vertex_seven)
objects.append(vertex_eight)
objects.append(vertex_nine)

graph.add_vertex(vertex_one)            
graph.add_vertex(vertex_two)
graph.add_vertex(vertex_three)
graph.add_vertex(vertex_four)
graph.add_vertex(vertex_five)
graph.add_vertex(vertex_six)
graph.add_vertex(vertex_seven)
graph.add_vertex(vertex_eight)
graph.add_vertex(vertex_nine)

ref_num = 0
while ref_num != len(objects):
    for vertex in range(len(objects)):
        cur_vertex = objects[ref_num]
        if vertex == ref_num:
            continue 
        else:
            graph.add_edge(cur_vertex, objects[vertex])
    
    ref_num += 1


