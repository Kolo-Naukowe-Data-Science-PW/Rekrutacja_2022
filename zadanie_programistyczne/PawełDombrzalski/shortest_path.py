class Vertex:
    def __init__(self, name: str, cost=float('inf'), neighbours=None, visited=False):
        self.name = name
        if neighbours is None:
            self.neighbours = {}
        else:
            self.neighbours = neighbours
        self.visited = visited
        self.cost = cost

    def add_neighbour(self, new_neighbour, distance):
        self.neighbours[new_neighbour] = distance

    def __str__(self):
        text = f"{self.name}: "
        for neighbour in self.neighbours:
            text += f"{neighbour.name}: {self.neighbours[neighbour]}\n"
        return text[:-1]


def parse_data(graph_dict):
    all_vertices = []
    for element in graph_dict:
        all_vertices += element
    all_vertices = set(all_vertices)

    all_vertices_dict = {v: Vertex(v) for v in all_vertices}

    for element in graph_dict:
        all_vertices_dict[element[0]].add_neighbour(all_vertices_dict[element[1]], graph_dict[element])
        all_vertices_dict[element[1]].add_neighbour(all_vertices_dict[element[0]], graph_dict[element])

    return all_vertices_dict


def dijkstra(vertices_list, start_vertex, end_vertex):
    if start_vertex == end_vertex:
        return []
    start = start_vertex
    previous_vertices_dict = {}
    for vertex in vertices_list:
        previous_vertices_dict[vertex] = -1
    start.cost = 0
    not_visited = vertices_list
    while not_visited:
        q = sorted(not_visited, key=lambda vertex: vertex.cost)
        not_visited.remove(q[0])
        q[0].visited = True
        for neighbour in q[0].neighbours:
            if neighbour.cost > q[0].cost + q[0].neighbours[neighbour]:
                neighbour.cost = q[0].cost + q[0].neighbours[neighbour]
                previous_vertices_dict[neighbour] = q[0]
    return get_path(start_vertex, end_vertex, previous_vertices_dict)


def get_path(start_vertex, end_vertex, previous_vertices_dict):
    path = [end_vertex]
    temp = end_vertex
    while True:
        previous_vertex = previous_vertices_dict[temp]
        path.append(previous_vertex)
        temp = previous_vertex
        if temp == start_vertex:
            return path[::-1]
    return path[::-1]


def main():
    graph = {
        ("B", "D"): 2,
        ("D", "A"): 1,
        ("B", "A"): 4,
        ("A", "C"): 2,
        ("C", "D"): 7,
        ("E", "C"): 3
    }

    graph2 = {
        ("A", "B"): 6,
        ("A", "D"): 4,
        ("B", "C"): 3,
        ("B", "D"): 6,
        ("B", "E"): 5,
        ("C", "E"): 2,
        ("D", "E"): 12,
        ("D", "F"): 9,
        ("E", "F"): 8,
    }

    all_vertices_dict = parse_data(graph)
    all_vertices = list(all_vertices_dict.values())

    path = dijkstra(all_vertices, all_vertices_dict["A"], all_vertices_dict["E"])
    p_names = [v.name for v in path]
    print(p_names)


if __name__ == "__main__":
    main()
