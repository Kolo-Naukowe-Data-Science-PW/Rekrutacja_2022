# Marta Szuwarska
# 23.10.2022
# Zadanie rekrutacyjne do Koła Naukowego Data Science
# Algorytm Dijkstry do znajdowania najkróßszej ścieżki w grafie
# Z wykorzystaniem kopca

import math
from heapq import heapify, heappop


class Vertex:

    # Tworzymy klasę Vertex (wierzchołek)

    def __init__(self, id):
        # Konstruktor
        self.id = id  # ID wierzchołka, czyli literka, np. "A"
        self.neighbours = {}  # zbiór sąsiadów wierzchołka w formie słownika, gdzie kluczem jest id wierzchołka,
        # a wartością obiekt
        self.predecessor = None  # poprzednik wierzchołka w najkrótszej ścieżce
        self.distance = math.inf  # odległość wierzchołka od wierzchołka startowego; początkowo wszystkie wierzchołki
        # mają odległość równą nieskończoność
        self.visited = False  # czy wierzchołek już został odwiedzony

    # def __str__(self):
    #     return str(self.id) + ": " + str([neighbour.id for neighbour in self.neighbours])

    def addNeighbour(self, v, dist = 0):
        # Funkcja dodająca sąsiada do zbioru sąsiadów
        self.neighbours[v] = dist


class Graph:

    # Tworzymy klasę Graph (graf)

    def __init__(self, dict):
        # Konstruktor
        self.vertices = {} # zbiór wierzchołków w formie słownika, gdzie kluczem jest id wierzchołka,
        # a wartością obiekt

        for edge in dict.items():
            # dodajemy krawędzie
            self.addEdge(edge[0][0], edge[0][1], edge[1])

    def addVertex(self, v):
        # dfunkcja dodająca wierzchołek do zbioru wierzchołków
        self.vertices[v] = Vertex(v)

    def addEdge(self, v1, v2, dist):
        # funkcja dodająca krawędź
        # jeżeli któryś z wierzchołków nie istnieje w zbiorze wierzchołków, to go dodajemy
        if v1 not in self.vertices:
            self.addVertex(v1)
        if v2 not in self.vertices:
            self.addVertex(v2)
        # dodajemy wierzchołkom siebie nawzajem jako sąsiadów z podaną odległością
        self.vertices[v1].addNeighbour(self.vertices[v2], dist)
        self.vertices[v2].addNeighbour(self.vertices[v1], dist)

    # def __str__(self):
    #     return str([str(v) for v in self.vertices.values()])


def findShortestPath(graph, start, end):
    # algorytm znajdowania najkrótszej ścieżki (Dijkstra)
    start.distance = 0  # ustawiamy odległość startowego wierzchołka (od samego siebie) jako 0

    # tworzymy kopiec, w którym węzłami są wierzchołki grafu uporządkowane według distance (odległości od wierzchołka startowego)
    # w ten sposób zawsze będziemy mieć na górze "najbliższy" wierzchołek
    unvisited = [(graph.vertices[v].distance, v) for v in graph.vertices]
    heapify(unvisited)

    # będziemy przechodzić po wierzchołkach, dopóki nie odwiedzimy wszystkich
    while len(unvisited) > 0:
        # ściągamy z kopca najbliższy wiechołek
        v = heappop(unvisited)
        currVert = graph.vertices[v[1]]
        currVert.visited = True # oznaczamy nasz aktualny wierzchołek jako odwiedzony
        # będziemy przechodzić po sąsiadach tego wierzchołka
        for neighbour in currVert.neighbours:
            if not neighbour.visited: # ale tylko tych nieodwiedzonych
                newDistance = currVert.distance + currVert.neighbours[neighbour] # liczymy nową odległość sąsiada od startu,
                # przechodząc przez obecny wierzchołek i porównujemy z jego aktulną odległością od startu
                if newDistance < neighbour.distance:
                    # jeżeli nowa odległość jest mniejsza, to aktualizujemy wartości atrybutów
                    neighbour.predecessor = currVert
                    neighbour.distance = newDistance
        # aktualizujemy nasz kopiec
        while len(unvisited) > 0:
            heappop(unvisited)
        unvisited = [(graph.vertices[v].distance, v) for v in graph.vertices if not graph.vertices[v].visited]
        heapify(unvisited)

    # zapisujemy do stosu ścieżkę od wierzchołka końcowego do startowego
    path = []
    v = end
    path.append(v.id)
    while v != start:
        path.append(v.predecessor.id)
        v = v.predecessor
    # wypisujemy długość ścieżki i kolejne wierzchołki
    print(end.distance)
    while len(path) > 0:
        print(path.pop())


def main():
    # wczytanie przykładowego grafu z polecenia
    graph = Graph({
        ("B", "D"): 2,
        ("D", "A"): 1,
        ("B", "A"): 4,
        ("A", "C"): 2,
        ("B", "E"): 3,
        ("C", "D"): 7,
        ("E", "C"): 3
    })
    # znalezienie najkrótszej ścieżki od wierzchołka A do E
    findShortestPath(graph, graph.vertices["A"], graph.vertices["E"])


if __name__ == '__main__':
    main()
