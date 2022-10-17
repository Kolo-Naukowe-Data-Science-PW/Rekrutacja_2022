import json
import ast


def read_graph_from_file(filename):
    with open(filename) as json_file:
        raw_data = json.load(json_file)
    return {ast.literal_eval(key): value for key, value in raw_data.items()}


if __name__ == '__main__':
    graph = read_graph_from_file(filename="graph.json")
    print(graph)
