import ast


def nearest_unvisited_vertex(distance, unvisited):
    min_dist = 'i'
    ret_vertex = -1
    for v in unvisited:
        if distance[v] != 'i' and (min_dist == 'i' or distance[v] < min_dist):
            min_dist = distance[v]
            ret_vertex = v

    return ret_vertex


def create_dict_of_dist_from_start(connections_list):
    vertices_dictionary = {}
    for t in connections_list:
        if t[0] not in vertices_dictionary:
            vertices_dictionary.update({t[0]: 'i'})
        if t[1] not in vertices_dictionary:
            vertices_dictionary.update({t[1]: 'i'})

    return vertices_dictionary


def dijkstra(start_point, end_point, graph, previous):
    connections_list = list(graph.keys())
    distance = create_dict_of_dist_from_start(connections_list)
    unvisited = list(distance.keys())

    if start_point in distance and end_point in distance:
        distance[start_point] = 0
    else:
        return 'Co najmniej jeden z podanych wierzchołków nie znajduje się w grafie'

    current_point = start_point
    while end_point != current_point and len(unvisited) > 0 and current_point != -1:
        unvisited.remove(current_point)
        for v in connections_list:
            if current_point in v:
                u = v[0] if v[1] == current_point else v[1]
                if distance[u] == 'i' or distance[u] > distance[current_point] + graph[v]:
                    distance |= {u: distance[current_point] + graph[v]}
                    previous |= {u: current_point}

        current_point = nearest_unvisited_vertex(distance, unvisited)

    return distance[end_point]


def create_path(previous, end_vertex):
    path = []
    vertex = end_vertex
    path.append(end_vertex)
    while previous.get(vertex) is not None:
        vertex = previous[vertex]
        path.insert(0, vertex)

    return path


def main():
    previous = {}
    f = open("plik_graf.txt")
    d = f.readline()
    x = ast.literal_eval(d)
    start_vertex = f.readline()
    end_vertex = f.readline()
    ret = dijkstra(start_vertex[0], end_vertex[0], x, previous)
    if ret == 'i':
        print("Graf niespójny")
        return
    if type(ret) is str:
        print(ret)
        return
    print("Długość ścieżki:", ret)
    path = create_path(previous, end_vertex)
    print(path)
    f.close()


if __name__ == "__main__":
    main()
