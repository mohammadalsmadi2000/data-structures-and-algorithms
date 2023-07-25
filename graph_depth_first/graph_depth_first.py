class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, adjacent):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(adjacent)

    def depth_first(self, start):
        if not self.graph:  
            return [start]
        if start not in self.graph:
            return []
        S1 = [start]
        result = []
        visite = set()

        while S1:
            node = S1.pop()
            if node not in visite:
                visite.add(node)
                result.append(node)
                for neighbor in self.graph.get(node, []):
                    S1.append(neighbor)

        return result