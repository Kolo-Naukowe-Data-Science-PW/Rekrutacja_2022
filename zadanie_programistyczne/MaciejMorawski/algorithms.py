import networkx as nx


class SolutionUsingNetworkX:
    def __init__(self, graph):
        self._graph = nx.Graph()
        self._graph.add_weighted_edges_from(
            [(key[0], key[1], value) for key, value in graph.items()])

    def shortest_path(self, source, target):
        return nx.shortest_path(self._graph, source, target, weight='weight')


class CustomSolution:
    def __init__(self, graph):
        self._graph = graph

    def shortest_path(self, source, target):
        return f"{source}->...->{target}"
