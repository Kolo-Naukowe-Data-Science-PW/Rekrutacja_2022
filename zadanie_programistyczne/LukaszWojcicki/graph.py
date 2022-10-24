START = "A"
END = "B"
PATHS = {
    ("B", "D"): 2,
    ("D", "A"): 1,
    ("B", "A"): 4,
    ("A", "C"): 2,
    ("B", "E"): 3,
    ("C", "D"): 7,
    ("E", "C"): 3,
    ("E", "F"): 1
}
GRAPH = {}


class Node:
    def __init__(self, name):
        self.name = name
        self.cost = float("inf")
        self.paths = {}
        self.visited = False
        self.visable = False
        self.shortest_way = []

    def add_path(self, direction, cost):
        self.paths[direction] = cost

    def __eq__(self, new_name: str) -> bool:
        if self.name == new_name:
            return True
        return False

    def __str__(self) -> str:
        ret = f"{self.name}: {str(self.paths)} -- {self.cost}"
        return ret


def make_graph():
    for path in PATHS:
        node = Node(path[0])
        if node.name not in GRAPH:
            GRAPH[node.name] = node
        else:
            node = GRAPH[node.name]
        node.add_path(path[1], PATHS[path])
        node = Node(path[1])
        if node.name not in GRAPH:
            GRAPH[node.name] = node
        else:
            node = GRAPH[node.name]
        node.add_path(path[0], PATHS[path])


def find_shortest_way():
    current_node: Node = GRAPH[START]
    current_node.cost = 0
    current_node.visited = True
    while len(GRAPH) != 0:
        for path in current_node.paths:
            next_node: Node = GRAPH[path]
            if next_node.visited is True:
                continue
            if next_node.cost > current_node.cost + current_node.paths[path]:
                next_node.cost = current_node.cost + current_node.paths[path]
                next_node.shortest_way = current_node.shortest_way + [next_node.name]
        current_node.visited = True
        current_name = find_min_cost()
        if current_name is None or current_name == END:
            break
        current_node = GRAPH[current_name]
    ret = f"The shortest path: {GRAPH[END].shortest_way} , cost:{GRAPH[END].cost}"
    return ret


def show_graph():
    for node_name in GRAPH:
        print(GRAPH[node_name])


def find_min_cost():
    min_value = float("inf")
    min_node = None
    node: Node
    for node in GRAPH.values():
        if node.cost < min_value and node.visited is False:
            min_node: Node = node
            min_value = node.cost
    if min_node is None:
        return None
    return min_node.name


def main():
    make_graph()
    print(find_shortest_way())
    show_graph()


if __name__ == "__main__":
    main()
