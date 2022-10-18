import networkx as nx
from pqdict import pqdict


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
        self._distances = {}
        self._path_backwards = {}

    def shortest_path(self, source, target):
        self._dijkstra(source=source)
        return self._get_path(source=source, target=target)

    def _dijkstra(self, source):
        queue = pqdict()

        # cost to source is 0
        queue[source] = 0
        self._distances = {
            source: 0
        }

        while len(queue) > 0:
            node, _ = queue.popitem()

            for neighbour, cost in self._get_node_neighbours_with_path_weights(node):
                if neighbour not in self._distances or\
                   self._distances[neighbour] > self._distances[node] + cost:
                    self._distances[neighbour] = self._distances[node] + cost
                    # remember best previous position
                    self._path_backwards[neighbour] = node
                    # push neighbour to queue
                    queue[neighbour] = self._distances[neighbour]

    def _get_node_neighbours_with_path_weights(self, node):
        full_graph = self._graph_with_reverse_edges(self._graph)
        neighbours = []
        for key, value in full_graph.items():
            if key[0] == node:
                neighbours.append((key[1], value))
        return neighbours

    def _get_path(self, source, target):
        node = target
        path = [target]
        while node != source:
            node = self._path_backwards[node]
            path.insert(0,node)
        return path

    def _graph_with_reverse_edges(self, graph):
        full_graph = graph.copy()
        for key, value in graph.items():
            full_graph[(key[1], key[0])] = value
        return full_graph
