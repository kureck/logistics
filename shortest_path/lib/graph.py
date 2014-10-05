import networkx as nx

class Graph:
    def __init__(self, directions):
        self.directions = directions
        self.g = nx.Graph()
        self.populate_graph()

    def populate_graph(self):
        for direction in self.directions:
            self.g.add_edge(direction.origin, direction.destination, weight=direction.weight)

    def shortest_path_value(self, origin, destination):
        return nx.dijkstra_path_length(self.g, origin, destination, 'weight')

    def shortest_path(self, origin, destination):
        return nx.dijkstra_path(self.g, origin, destination, 'weight')

    def shortest_path_result(self, origin, destination, autonomia=1.0, litro=1.0):
        shortest_path_value = self.shortest_path_value(origin, destination)
        shortest_path = self.shortest_path(origin, destination)
        shortest_path_result = shortest_path_value*float(litro)/float(autonomia)
        return { 'shortest_path_value' : shortest_path_result, 'shortest_path' : shortest_path }

