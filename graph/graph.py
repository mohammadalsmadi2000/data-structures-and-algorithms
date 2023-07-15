from edge import Edge
from vertices import Vertices


class Graph:
    def __init__(self):
        self.edj_list = {}

    def add_vertex(self, V):
        tempVertices = Vertices(V)
        self.edj_list[tempVertices] = []
        return tempVertices

    def add_edge(self, V1, V2, W):
        if (not V1 in self.edj_list.keys()) or (not V2 in self.edj_list.keys()):
            raise ValueError("This vertex does not exist")

        edge1 = Edge(V2, W)
        edge2 = Edge(V1, W)

        self.edj_list[V1].append(edge1)
        self.edj_list[V2].append(edge2)

    def get_vertices(self):
        return list(self.edj_list.keys())

    def get_neighbors(self, V):
        return self.edj_list[V]

    def size(self):
        return len(self.edj_list)
