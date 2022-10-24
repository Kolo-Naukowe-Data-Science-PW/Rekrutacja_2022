import ast
import json

from algorithms import CustomSolution, SolutionUsingNetworkX


def read_graph_from_file(filename):
    with open(filename, encoding='utf-8') as json_file:
        raw_data = json.load(json_file)
    return {ast.literal_eval(key): value for key, value in raw_data.items()}


if __name__ == '__main__':
    graph = read_graph_from_file(filename="graph.json")

    networkx_algorithm = SolutionUsingNetworkX(graph)
    print(f"NetworkX solution path: "\
        f"{networkx_algorithm.shortest_path(source = 'A', target = 'B')}")

    custom_algorithm = CustomSolution(graph)
    print(f"Custom implementation of Dijkstra\'s algorithm solution path: " \
        f"{custom_algorithm.shortest_path(source = 'A', target = 'B')}")
