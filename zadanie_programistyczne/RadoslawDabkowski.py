def dijkstra(graph, start, end):

    # for every node store every node it is connected to and the cost
    available_paths = {}
    for connection in graph:
        if available_paths.get(connection[0]) is None:
            available_paths[connection[0]] = []
        available_paths[connection[0]].append((graph[connection], connection[1]))

    # if the start node is not in the graph, return an empty list
    if start not in available_paths:
        return []
    
    visited = []
    shortest_path = {}
    for node, node2 in graph:
        shortest_path[node] = (None, float('inf'))
        shortest_path[node2] = (None, float('inf'))
    shortest_path[start] = (None, 0)
    current_node = start
    
    while end not in visited:

        # loop through all the nodes connected to the current node
        for value, node in available_paths[current_node]:
            if node not in visited:

                # if the node is not in the shortest_path dictionary
                # or the distance to the node is shorter than the current distance
                # update the distance and previous node
                    if shortest_path.get(node)[0] is None or value > shortest_path[current_node][1] + graph[(current_node, node)]:
                        shortest_path[node] = (current_node, shortest_path[current_node][1] + graph[(current_node, node)])

        # find the next node to visit
        visited.append(current_node)
        next_node = None
        for node in shortest_path:
            if node not in visited and node in available_paths:
                if next_node is None:
                    next_node = node
                elif shortest_path[node][1] < shortest_path[next_node][1]:
                    next_node = node
        current_node = next_node
        if current_node is None:
            break
        

    # build the path from the end to the start using the shortest_path dictionary
    path = []
    current_node = end
    while current_node != start:
        path.append(current_node)
        current_node = shortest_path[current_node][0]

        # if there is no path
        if current_node is None:
            return []
            
    path.append(start)
    return path[::-1]

# test
def main():
    graph = {
    ("B", "D"): 2,
    ("D", "A"): 1,
    ("B", "A"): 4,
    ("A", "C"): 2,
    ("B", "E"): 3,
    ("C", "D"): 7,
    ("E", "C"): 3
    } 
    print(" => ".join(dijkstra(graph, "E", "A")))

if __name__ == "__main__":
    main()
