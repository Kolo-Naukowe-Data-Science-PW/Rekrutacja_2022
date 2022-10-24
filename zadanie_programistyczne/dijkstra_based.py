"""It's a code solution based dijkstra algorithm to find shortest paths between two given points in graph.
Graph in form of a specific dictionary. Example presented lower as 'example_input'. """

example_input = {
    ("B", "D"): 2,
    ("D", "A"): 1,
    ("B", "A"): 4,
    ("A", "C"): 2,
    ("B", "E"): 3,
    ("C", "D"): 7,
    ("E", "C"): 3,
}

# returns set of points/places from given dictionary
def points(dictionary):
    set_points = []
    for key in dictionary.keys():
        set_points.append(key[0])
        set_points.append(key[1])
    return set(set_points)

""" returns a letter (place) that is unvisited and has the shortest path. 
If two paths have the same distance, it returns the first letter that occurs."""
def next_letter(table, unvisited):
    copy_table = table.copy()
    for element in table:           #checks if the letter is unvisited
        if element not in unvisited:
            del copy_table[element]

    for x in table:        #cheks which letter from unvisited has the shortest path.
        if x in unvisited:
            if table[x][0] == copy_table[min(copy_table, key=lambda x: table[x][0])][0]:
                return x

#makes a table that can provide the shortest path from chosen letter to all the letters in given graph
def table_of_paths(start_letter, allpaths): #start_letter -string of place where the path starts. allpaths - dictionary with all paths
    unvisited = points(allpaths)
    visited = []
    table = {}

    # for loop creates first state of table where chosen letter has path = 0 and others path = infinity.
    for x in unvisited:
        if x != start_letter:
            table[f"{x}"] = [float("inf"), "none"]
        else:
            table[f"{x}"] = [0, f"{x}"]

    prev_node = start_letter

    """finds a path that between previous node and other points. Then cheks if it is the shortest way 
    according to dijkstra algorythm and adds to table"""
    while any(unvisited):
        for key in allpaths:
            if prev_node == key[0] and table[key[1]][0] > (allpaths[key] + table[prev_node][0]):
                table[key[1]] = [allpaths[key] + table[prev_node][0], prev_node]
            elif prev_node == key[1] and table[key[0]][0] > (allpaths[key] + table[prev_node][0]):
                table[key[0]] = [allpaths[key] + table[prev_node][0], prev_node]

        unvisited.remove(prev_node) #after looking for shortest path, removes letter from unvisited.
        visited.append(prev_node)
        prev_node = next_letter(table, unvisited) #finds next letter to visit
    return table

# creates a string describing shortest path between two chosen letters.
def shortes_path_str(start, destination, paths):
    table = table_of_paths(start, paths)
    end_str = " -> " + destination + f" || distance: {table[destination][0]}"
    while_dest = destination
    while start != table[while_dest][1]:
        end_str = f" -> {table[while_dest][1]}" + end_str
        while_dest = table[while_dest][1]
    return start + end_str

if __name__ == '__main__':
    print(table_of_paths("B", example_input))
    print(shortes_path_str("B", "C", example_input))