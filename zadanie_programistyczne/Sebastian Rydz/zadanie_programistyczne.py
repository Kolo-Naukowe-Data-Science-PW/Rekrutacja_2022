from math import isinf
from itertools import permutations

def main():

    def convert_to_matrix(points):
        all_points = sorted(set([point for tup in points.keys() for point in tup]))
        matrix = [[] for z in range(len(all_points))]
        for x in range(len(all_points)):
            for y in range(len(all_points)):
                try:
                    matrix[x].append(points[all_points[x],all_points[y]])
                except KeyError:
                    try:
                        matrix[x].append(points[all_points[y],all_points[x]])
                    except KeyError:
                        matrix[x].append(float("inf"))
        points_index = [ord(point)-65 for point in all_points]
        return matrix, points_index

    def check_distance_and_route(next_point, can_go_to, where_is_now, distance = 0):
        if isinf(matrix[where_is_now][next_point]): # for every possible next point, checks if there isn't a connection, if true: returns 'inf' as a distance for a whole route
            return float("inf")
        elif next_point == ending_point: # checks if we actually got into our endpoint while walking thru all possible ways
            return distance + matrix[where_is_now][next_point]
        else:
            return check_distance_and_route(can_go_to.pop(0), can_go_to, next_point, distance + matrix[where_is_now][next_point])
        
    distance_between_points = {
    ("B", "D"): 2,
    ("D", "A"): 1,
    ("B", "A"): 4,
    ("A", "C"): 2,
    ("B", "E"): 3,
    ("C", "D"): 7,
    ("E", "C"): 3
    } 

    matrix, points_index = convert_to_matrix(distance_between_points)

    starting_point = ord(input("Input starting point: ").upper())-65
    ending_point = ord(input("Input ending point: ").upper())-65

    can_go_to = points_index
    can_go_to.pop(starting_point) # points excluding starting_point

    ways_to_go = [list(way) for way in list(permutations(can_go_to))] # creating all possible ways to walk thru all points, starting point excluded

    min_cost = float("inf")
    min_route = ()

    for way in ways_to_go:
        distance = check_distance_and_route(way[0], way[1:], starting_point)
        if distance < min_cost:
            min_cost = distance 
            min_route = tuple(chr(starting_point+65)) + tuple(chr(z+65) for z in way[:-1])

    print(f'Cost: {min_cost}, route: {min_route}')

if __name__ == "__main__":
    main()
