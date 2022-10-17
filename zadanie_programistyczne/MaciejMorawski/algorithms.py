import networkx


class SolutionUsingNetworkX:
    def __init__(self, graph):
        self._graph = graph

    def shortest_path(self, source, target):
        return f"{source}->...->{target}"


class CustomSolution:
    def __init__(self, graph):
        self._graph = graph

    def shortest_path(self, source, target):
        return f"{source}->...->{target}"
