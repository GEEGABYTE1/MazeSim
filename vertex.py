class Vertex:
    def __init__(self, value, x, y):
        self.value = value 
        self.edges = {}
        self.position = (x, y)

    def add_edge(self, vertex, weight=0):
        self.edges[vertex] = weight

    def get_edges(self):
        return list(self.edges.keys())