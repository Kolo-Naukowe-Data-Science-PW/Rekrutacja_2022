import itertools

def all_places(dictionary):
    places = set([])
    
    for i in dictionary.keys(): #  Get all the places 
        places.update(i)

    places = list(places)
    places = ''.join(places)

    return places

def find_solution(places, dictionary):
    solutions = {}
    for index, i  in enumerate(itertools.permutations(places, len(places))):
        add = True
        distance = 0
        for k in range(0, len(places)-1):
            if (i[k], i[k+1]) in dictionary.keys() or (i[k+1], i[k]) in dictionary.keys():
                try:
                    distance += dictionary[(i[k], i[k+1])]
                except Exception as e:
                    distance += dictionary[(i[k+1], i[k])]
            else:
                add = False
                break
        #print(i, distance, add)
        if add:
            solutions[i] = distance
            shortest_path, shortest_distance = i, distance
    for path, distance in solutions.items():
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = path 
    return (shortest_path, shortest_distance)
    
def main():
    dictionary = {
        ("B", "D"): 2,
        ("D", "A"): 1,
        ("B", "A"): 4,
        ("A", "C"): 2,
        ("B", "E"): 3,
        ("C", "D"): 7,
        ("E", "C"): 3
    }   
    places = all_places(dictionary)
    solution = find_solution(places, dictionary)
    print(solution)


if __name__ == "__main__":
    main()


