from graph import*
from vertex import Vertex



graph = Graph(True)

objects = []

vertex_one = Vertex('a', 1, 5)
vertex_two = Vertex('b', 2, 10)
vertex_three = Vertex('c', 3, 15)

vertex_four = Vertex('d', 4, 6)
vertex_five = Vertex('e', 5, 12)
vertex_six = Vertex('*', 6, 18)

vertex_seven = Vertex('f', 7, 7)
vertex_eight = Vertex('g', 8, 14)
vertex_nine = Vertex('h', 9, 21)

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

graph.add_edge(vertex_one, vertex_three, 4)
graph.add_edge(vertex_one, vertex_five, 11)

graph.add_edge(vertex_three, vertex_seven, 5)
graph.add_edge(vertex_seven, vertex_eight, 8)
graph.add_edge(vertex_eight, vertex_four, 9)
graph.add_edge(vertex_four, vertex_nine, 2)

graph.add_edge(vertex_nine, vertex_two, 1)
graph.add_edge(vertex_two, vertex_five, 10)

graph.add_edge(vertex_five, vertex_six, 7)
graph.add_edge(vertex_three, vertex_six, 3)
graph.add_edge(vertex_eight, vertex_six, 6)
graph.add_edge(vertex_nine, vertex_six, 0)

