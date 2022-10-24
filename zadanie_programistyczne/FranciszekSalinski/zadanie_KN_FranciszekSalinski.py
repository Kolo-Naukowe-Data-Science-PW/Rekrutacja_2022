from queue import PriorityQueue
import csv 

def find_shortest_path(graph, x, y):
    # Funkcja znajdzie najkrótszą ścieżkę z węzła x do y w grafie za pomocą algorytmu Dijkstry
    queue = PriorityQueue() # kolejka priorytetowa

    distances = {node : float('inf') for node in graph} # słownik przechowujący odległości węzłów od punktu x
    distances[x] = 0

    previous = {node : '' for node in graph} # słownik przechowujący informacje o poprzednikach węzłów w najkrótszych ścieżkach

    queue.put((0, x))
    
    while not queue.empty():
        current_node = queue.get()[1] # wyciągamy z kolejki priorytetowej węzeł, do którego prowadzi najkrótsza ścieżka

        for connected_node in graph[current_node]:
            if distances[current_node] + graph[current_node][connected_node] < distances[connected_node]: # sprawdzamy czy do któregoś z sąsiednich węzłów możemy dojść krótszą ścieżką niż dotychczas
                distances[connected_node] = distances[current_node] + graph[current_node][connected_node] # jeśli tak, odpowiednio podmieniamy odległość oraz poprzednika
                previous[connected_node] = current_node
                queue.put((distances[connected_node], connected_node)) # dodajemy do kolejki węzęł który mógł jeszcze nie być przetwarzany
        
    path = []
    
    path_node = y
    while path_node != x: # tworzymy tablicę z kolejnymi węzłami najkrótszej cieżki z x do y
        path.append(path_node)
        path_node = previous[path_node]
    path.append(x)
    path.reverse()
    
    return f'Najkrótsz ścieżka to: {" -> ".join(path)}. Ma długość {distances[y]}.' # zwracamy uzyskany rezultat

def convert_graph(graph):
    """
    Funkcja zamienia postać grafu
    Zamienia słownik, gdzie kluczem jest krotka (para połączonych węzłów) a wartością odległość między nimi, 
    na słownik, w którym kluczem jest węzeł, a wartością słownik sąsiednich węzłów i odległości od nich
    """
    new_graph = {}
    for edge in graph:
        if not edge[0] in new_graph:
            new_graph[edge[0]] = {}
        if not edge[1] in new_graph:
            new_graph[edge[1]] = {}
        new_graph[edge[0]][edge[1]] = graph[edge]
        new_graph[edge[1]][edge[0]] = graph[edge]
    return new_graph

def main():

    graph = {}

    with open('graph2.csv') as file: # wczytujemy graf z pliku csv
        reader = csv.reader(file)
        for row in reader:
            graph[(row[0], row[1])] = int(row[2])

    graph = convert_graph(graph)

    print(find_shortest_path(graph, "A", "Z")) # przykładowe wywołanie funkcji


if __name__ == '__main__':
    main()