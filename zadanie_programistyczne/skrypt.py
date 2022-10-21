## tutaj bedziemy sobie implementowali algorytm dijkstry, no bo w sumie to jest chyba najlepszy algorytm do robienia tego
# zakladamy ze graf nie jest skierowany dla łatwosci

NONE_VAL = -1
MIN_DIST = 1e10


class Graph():
    def __init__(self, vertices):
        # tutaj bedziemy podawa
        self.V = {}
        self.n = 0
        self.E = []
        for key in vertices:
            if key[0] not in self.V:
                self.add_vertex(key[0])

            if key[1] not in self.V:
                self.add_vertex(key[1])
            
            key_indexes = (self.V[key[0]], self.V[key[1]])
            
            # if self.E[key[0]][key[1]] == -1:
            self.E[key_indexes[0]][key_indexes[1]] = vertices[key]
            self.E[key_indexes[1]][key_indexes[0]] = vertices[key]

        print(f"pomyslnie stworzono graf o {self.n} wierzchołkach!\n")

    def add_vertex(self, A):
        if A not in self.V:
            self.V[A] = self.n
            self.n+=1
            
            self.E.append([NONE_VAL for i in range(self.n-1)])

            for row in self.E:
                row.append(NONE_VAL)

            self.E[len(self.V)-1][len(self.V)-1] = 0

    def min_dist(self, vertex_dist, visited):
        # funkcja zwraca sobie najblizszy wierzcholek do danego, ktory nie zostal wczesniej odwiedzony

        min = MIN_DIST
        min_index = 0

        for v in range(self.n):
            # teraz sobie przechodzimy, zeby znalezc wierzcholek, który jest najblizej source i dodatkowo nie byl jeszcze odwiedzony
            if vertex_dist[v] < min and visited[v] == False:
                min = vertex_dist[v]
                min_index = v

        return min_index


    def dijkstra(self, source):
        """
        wyszukuje sobie najkrótsze drogi do wierzchołkow 
        Args:
            source -> skad poszukujemy drog
        """
        vertex_dist = [MIN_DIST] * self.n
        visited = [False] * self.n

        s_index = self.V[source]
        vertex_dist[s_index] = 0

        for i in range(self.n):
            # przechodzimy sb po prostu n razy przez wszystkie wierzchołki
            
            next_vertex = self.min_dist(vertex_dist, visited)
            print(next_vertex)
            visited[next_vertex] = True

            # teraz modyfikujemy odległosci w dist
            for v in range(self.n):
                v_dist = self.E[next_vertex][v]
                if v_dist > 0 and vertex_dist[v] > v_dist + vertex_dist[next_vertex] and visited[v] == False:
                    vertex_dist[v] =  v_dist + vertex_dist[next_vertex]

        return vertex_dist


    def shortest_path(self, A, B):
        distances = self.dijkstra(A)

        b = self.V[B]

        return distances[b]



def najkrotsza_sciezka(G, A, B):
    """
    algorytm wypisuje najkrótszą ścieżkę pomiędzy dwoma zadanymi wierzchołkami A i B grafu G, gdzie G jest podany jako słownik z krotkami 
    """
    graph = Graph(G)

    print(graph.shortest_path(A, B))

