from graph import*
from vertex import Vertex

graph = Graph()

objects = []

vertex_one = Vertex('/', 1, 5)
vertex_two = Vertex('/', 1, 10)
vertex_three = Vertex('/', 1, 15)

vertex_four = Vertex('/', 2, 6)
vertex_five = Vertex('/', 2, 12)
vertex_six = Vertex('*', 2, 18)

vertex_seven = Vertex('/', 3, 7)
vertex_eight = Vertex('/', 3, 14)
vertex_nine = Vertex('/', 3, 21)

objects.append(vertex_one)
objects.append(vertex_two)
objects.append(vertex_three)
objects.append(vertex_four)
objects.append(vertex_five)
objects.append(vertex_six)
objects.append(vertex_seven)
objects.append(vertex_eight)
objects.append(vertex_nine)

print(objects)