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
        if (V1 not in self.edj_list) or (V2 not in self.edj_list):
            raise ValueError("This vertex does not exist")

        edge1 = (V2, W)
        edge2 = (V1, W)

        self.edj_list[V1].append(edge1)
        self.edj_list[V2].append(edge2)

    def get_vertices(self):
        return list(self.edj_list.keys())

    def get_neighbors(self, V):
        return self.edj_list[V]

    def size(self):
        return len(self.edj_list)

# CC 36
    def breadth_first(self, start_vertex):
        visited = set()
        result = []
        to_visit = [start_vertex]
        index = 0

        visited.add(start_vertex)

        while index < len(to_visit):
            current_vertex = to_visit[index]
            result.append(str(current_vertex))  

            for neighbor, _ in self.edj_list[current_vertex]:
                if neighbor not in visited:
                    to_visit.append(neighbor)
                    visited.add(neighbor)

            index += 1

        return result