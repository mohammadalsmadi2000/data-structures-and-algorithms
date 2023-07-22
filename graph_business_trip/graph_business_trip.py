class Graph:
    def __init__(self):
        self.graph = {}
        
    def add_edge(self, C1, C2, cost):
        if C1 not in self.graph:
            self.graph[C1] = {}
        self.graph[C1][C2] = cost

    def direct_flight(self, C1, C2):
        if  C1 in self.graph and C2 in self.graph[C1] :
         return True

    def flight_cost(self, C1, C2):
        return self.graph[C1][C2]


def business_trip(graph, path):
    total_cost = 0

    for i in range(len(path) - 1):
        current_city = path[i]
        next_city = path[i + 1]

        if not graph.direct_flight(current_city, next_city):
            return None

        total_cost += graph.flight_cost(current_city, next_city)

    return total_cost