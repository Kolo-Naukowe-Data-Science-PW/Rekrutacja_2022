import itertools



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

class Solution:
    def __init__(self, dictionary, start, end):
        self.dictionary = dictionary
        self.start = start
        self.end = end
        self.distance = [0]
        self.used = []

        self.solution = []

        self.all_places()
        self.sort_values()

    def all_places(self):
        places = set([])

        for i in self.dictionary.keys(): #  Get all the places 
            places.update(i)

        self.places = list(places)
        """
        add track of used verticies
        """

    def sort_values(self):
        self.sorted = {}
        for point in self.places:
            self.sorted[point] = []
            for path in self.dictionary.keys():
                if point in path:
                    if path[0] == point:
                        second = path[1]
                    else:
                        second = path[0]
                    self.sorted[point].append((second, self.dictionary[path]))

    def backtrack(self, curr_point):

        if self.expected_path(self.used):
            if self.solution:
                if self.solution[1] > sum(self.distance):
                    self.solution = (''.join(self.used), sum(self.distance))
            else:
                self.solution = (''.join(self.used), sum(self.distance))
            self.used.pop()
            self.distance.pop()
            return
        
        for next_point in self.sorted[curr_point]:
            if next_point[0] in self.used:
                continue
            self.distance.append(next_point[1])
            self.used.append(next_point[0])
            self.backtrack(next_point[0])

        self.used.pop()
        self.distance.pop()
        return

    def solve(self, curr_point):
        self.used.append(curr_point)
        self.backtrack(curr_point)

    def expected_path(self, path):
        if not path:
            return False
        if path[0] == self.start and path[-1] == self.end:
            return True
        return False

    def __repr__(self):
        return self.solution[0]


    
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
    start = 'A'
    end = 'C'
    solution = Solution(dictionary, start, end)
    solution.solve('A')
    print(solution)


if __name__ == "__main__":
    main()


