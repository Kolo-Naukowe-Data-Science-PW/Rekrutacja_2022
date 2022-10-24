from typing import Dict, Tuple
import numpy as np

class Graph:
    """
    Class representing whole graph with vertices and edges.
    Graph has attribute vertices, which is dictionary with keys as
    vertices' ids and Vertex objects as values.
    """

    def __init__(self):
        self.vertices: Dict[str, Vertex] = {}

    def __iter__(self):
        return iter(self.vertices.values())

    def __str__(self):
        result = ''
        for vertex in self:
            for vertex_2, weight in vertex.get_connections():
                result += f'({vertex.key}, {vertex_2.key}, {weight})\n'
        return result

    def add_vertex(self, key: str):
        """
        Add vertex to a graph
        """
        if key not in self.vertices:
            self.vertices[key] = Vertex(key=key)

    def add_edge(self, key_from: str, key_to: str, weight: float):
        """
        Add edge to graph. If vertices do not exist, functions creates them.
        """
        self.add_vertex(key_from)
        self.add_vertex(key_to)
        self.vertices[key_from].add_neighbour(self.vertices[key_to], weight)

    def load_from_dict(self, dictionary: Dict[Tuple[str, str], float]):
        """
        Create graph structure from dictionary, where key: <key_from, key_to>, value: edge weight
        """
        for key, value in dictionary.items():
            try:
                self.add_edge(key_from=key[0],
                              key_to=key[1],
                              weight=value)
            except:
                print('Item provided in invalid format')


class Vertex:
    """
    Class representing single vertex in a graph.
    Each object has the following attributes:
    key: identity of a vertex
    connected_to: dictionary with adjacent vertices and corresponding weights
    parent: vertex predecessor (used in search algorithm)
    distance: distance from the starting vertex (used in search algorithm)
    """
    def __init__(self, key: str) -> None:
        self.key = key
        self._connected_to = {}
        self._parent = None
        self._distance = np.inf

    def __gt__(self, other):
        "Defining > relation for search algorithm"
        return self.get_distance() > other.get_distance()

    def __lt__(self, other):
        "Defining < relation for search algorithm"
        return self.get_distance() < other.get_distance()

    def __str__(self):
        return str(self.key) + ' connected to: ' + str([x.key for x in self._connected_to])

    def add_neighbour(self, nbr, weight: float) -> None:
        """
        Add neighbouring vertex with a particular weight
        """
        self._connected_to[nbr] = weight

    def get_connections(self):
        """
        Get all adjacent vertices and corresponding weights
        """
        return ((vertex, weight) for vertex, weight in self._connected_to.items())

    def set_parent(self, parent):
        self._parent = parent

    def get_parent(self):
        return self._parent

    def set_distance(self, distance):
        self._distance = distance

    def get_distance(self):
        return self._distance

if __name__ == '__main__':
    pass
