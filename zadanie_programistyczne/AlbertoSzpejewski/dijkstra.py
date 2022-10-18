from typing import List, Dict, Tuple, Union


def create_graph(graph: Dict[Tuple[str, str], float]
                 ) -> Dict[str, Dict[str, float]]:
    """
    Function reshapes the given data into a more
    human and computer readable format. The data structure contains
    any nodes neighbor

    Args:
        graph Dict[Tuple[str, str], float]: Given data structure

    Returns:
        Dict[str, Dict[str, int]]
    """

    connection_graph = {}

    for connection, value in graph.items():
        if connection[0] in connection_graph:
            connection_graph[connection[0]][connection[1]] = value
        else:
            connection_graph[connection[0]] = {connection[1]: value}

        if connection[1] in connection_graph:
            connection_graph[connection[1]][connection[0]] = value
        else:
            connection_graph[connection[1]] = {connection[0]: value}

    return connection_graph


def create_table(graph: Dict[str, Dict[str, int]]
                 ) -> Dict[str, List[Union[float, str]]]:
    """
    Creates a table needed to perform Dijkstra algorithm

    Args:
        graph (Dict[str, Dict[str, int]]): Data returned by create_graph function

    Returns:
        Dict[str, List[Union[float, str]]]
    """
    table = {}

    for node in graph.keys():
        table[node] = [float("inf"), ""]

    return table


def dijkstra(start: str, end: str,
             graph: Dict[str, Dict[str, int]],
             table: Dict[str, List[Union[int, str]]]
             ) -> Dict[str, List[Union[int, str]]]:
    """
    Performs Dijkstra algorithm on the
    processed graph

    Args:
        start str: Start node
        end str: End node
        graph Dict[str, Dict[str, int]]: Graph from create graph function
        table Dict[str, List[Union[int, str]]]: Dijkstra table to save distances

    Returns:
        Dict[str, List[Union[int, str]]]: Final unprocessed Dijkstra's table
    """

    table[start][0] = 0
    current_node = start

    # Instead of adding every node,
    # a stack can be used to store discovered nodes
    non_visited = [node for node in graph.keys()]
    visited = []

    non_visited.remove(end)

    shortest_length = 0

    # The loop runs until there is no element in the list
    # The loop doesn't calculate the last element
    while non_visited:
        minimum_node = ""
        minimum_length = float("inf")

        for node, length in graph[current_node].items():
            if node in visited:
                continue

            if length + shortest_length < table[node][0]:
                table[node][0], table[node][1] = length + shortest_length, current_node

            if table[node][0] < minimum_length:
                minimum_length = table[node][0]
                minimum_node = node

        shortest_length = minimum_length

        if current_node == end:
            visited.append(non_visited[-1])
            current_node = non_visited.pop()
            shortest_length = table[current_node][0]
        elif current_node not in non_visited:
            current_node = minimum_node
        else:
            visited.append(current_node)
            non_visited.remove(current_node)
            current_node = minimum_node

    minimum_length = float("inf")

    # Perform the node search for the last node
    for node, length in graph[current_node].items():
        if node in visited:
            continue

        if length + shortest_length < table[node][0]:
            table[node][0], table[node][1] = length + shortest_length, current_node

        if table[node][0] < minimum_length:
            minimum_length = table[node][0]

    return table


def print_answer(start: str, end: str,
                 graph: Dict[Tuple[str, str], float]
                 ) -> None:
    """
    Groups every function return and processes
    it to get an easy to read shortest path

    Args:
        start str: Start node
        end str: End node
        graph Dict[Tuple[str, str], float]: Graph from create graph function

    Returns:
        None
    """

    graph = create_graph(graph)
    table = create_table(graph)

    answer = dijkstra(start, end, graph, table)

    node = end

    traversal = [end]

    print(f"From {start} to {end}: ")

    while answer[node][1] != start:
        node = answer[node][1]
        traversal.append(node)
    traversal.append(start)

    while traversal:
        print(traversal.pop(), end='')

    print()
