from data_structures import Vertex, Graph
from queue import PriorityQueue
from typing import Tuple, List


def create_solution(initial: str, final: str, data_source):
    """
    Give solution in a neat way, with txt_info, shortest distance and path from root to final vertex
    """
    if isinstance(data_source, str):
        graph_dict = convert_txt_to_graph_dict(data_source)
    elif isinstance(data_source, dict):
        graph_dict = data_source
    else:
        raise Exception('Data source type invalid')

    graph = Graph()
    graph.load_from_dict(graph_dict)
    result, txt = priority_search(initial, final, graph)
    print(f"Trying to find path from '{initial}' to '{final}'")
    print(txt)
    if result:
        print('Minimal distance to a final vertex ', graph.vertices[final].get_distance())
        print('Path to a final vertex: ', traverse_back(graph.vertices[final]))


def priority_search(initial: str,
                    final: str,
                    graph: Graph) -> Tuple[bool, str]:
    """
    Perform priority search on graph
    Starting from initial vertex, algorithm tries to find the shortest path to final one.
    Vertices' attributes are updated dynamically, so after the all process final vertex contain
    all info necessary to get the shortest distance and path

    :param initial: inital vertex id
    :param final: final vertex id
    :param graph: graph object with loaded all vertices and edges
    return: <True, txt_info> if solution exists, <False, txt_info> otherwise
    """
    if not all(key in graph.vertices for key in [initial, final]):
        return False, 'Vertices do not exist in a graph'

    graph.vertices[initial].set_distance(0)
    waiting_list = PriorityQueue()
    waiting_list.put(graph.vertices[initial])

    while not waiting_list.empty():
        current_vertex = waiting_list.get()
        if current_vertex.key == final:
            return True, 'Solution found in a graph'

        for vertex, weight in current_vertex.get_connections():
            if current_vertex.get_distance() + weight < vertex.get_distance():
                vertex.set_parent(current_vertex)
                vertex.set_distance(current_vertex.get_distance() + weight)
                waiting_list.put(vertex)
    return False, 'No connection between two given vertices'


def traverse_back(vertex: Vertex) -> List:
    """
    Traverse back from particular vertex, up to the root
    """
    if not vertex.get_parent():
        return [vertex.key]
    else:
        return traverse_back(vertex.get_parent()) + [vertex.key]

def convert_txt_to_graph_dict(txt_file):
    graph_dict = {}
    with open(txt_file) as f:
        line = f.readline().strip()
        while line:
            splitted = line.split(sep=',')
            if len(splitted) != 3:
                print('Row not in correct format')
            else:
                try:
                    graph_dict[(splitted[0], splitted[1])] = float(splitted[2])
                except:
                    print('Row was not in correct format')
            line = f.readline().strip()
    return graph_dict

if __name__ == '__main__':
    pass