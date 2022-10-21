import ast

def dijkstra(graph, n, dest, src):
    """
    :param graph: graf w formie mapy sąsiedztwa
    :param n: liczba wierzchołków w grafie
    :param dest: wybrany wierzchołek grafu, który jest początkiem wyznaczania najkrótszych ścieżek do wszystkich pozostałych wierzchołków.
    :return: Dla każdego wierzchołka i  algorytm wyznacza koszt dojścia d [ i  ] oraz poprzednika p [ i  ] na najkrótszej ścieżce.
    """
    QS = [False] * n                # czy i-ty wierzchołek został już przetworzony
    dist = [float("inf")] * n       # tablica minimalnych odległości
    prev = [-1 for _ in range(n)]   # tablica poprzedników
    hlen = n                        # wielkość kopca
    heap = [0] * n                  # kopiec (kolejka priorytetowa)
    heap_pointer = [0] * n          # informacja o położeniu i-tego wierzchołka w kopcu
    for i in range(n):              # ustawienie początkowe kopca
        heap[i] = i
        heap_pointer[i] = i
    dist[dest] = 0
    if dest != 0:
        x = heap[0]
        heap[0] = heap[dest]
        heap[dest] = x
        heap_pointer[0] = dest
        heap_pointer[dest] = 0
    for i in range(n):                                      # ściąganie elementu z góry kopca(o najmniejszej odległości)
        u = heap[0]
        hlen = hlen - 1                                     # zmiejszenie wielkości kopca i wciągniecie ostatniego elementu na pozycję 0
        heap[0] = heap[hlen]
        heap_pointer[heap[0]] = 0
        parent = 0
        while True:                                         # aktualizowanie kopca (w dół)
            left = 2 * parent + 1
            right = left + 1
            if left >= hlen:
                break
            dmin = dist[heap[left]]
            pmin = left
            if right < hlen:
                if dmin > dist[heap[right]]:
                    dmin = dist[heap[right]]
                    pmin = right
            if dist[heap[parent]] <= dmin:
                break
            x = heap[parent]
            heap[parent] = heap[pmin]
            heap[pmin] = x
            heap_pointer[heap[parent]] = parent
            heap_pointer[heap[pmin]] = pmin
            parent = pmin
        QS[u] = True                                        # oznaczenie wierzchołka u jako przetworzonego
        if u != src:                                        # jeśli jeszcze nie dotarliśmy do celu to aktualizujemy odległości nieprzetworzonych sąsiadów u
            for v in graph[u]:
                if not QS[v[0]] and dist[v[0]] > dist[u] + v[1]:
                    dist[v[0]] = dist[u] + v[1]
                    prev[v[0]] = u
                    child = heap_pointer[v[0]]
                    while child > 0:                        # aktualizowanie kopca (w górę)
                        parent = child // 2
                        if dist[heap[parent]] <= dist[heap[child]]:
                            break
                        x = heap[parent]
                        heap[parent] = heap[child]
                        heap[child] = x
                        heap_pointer[heap[parent]] = parent
                        heap_pointer[heap[child]] = child
                        child = parent
    s = chr(src + 65) + ", "                                # wypisanie
    j = src
    while prev[j] > -1:
        s = s + chr(prev[j] + 65) + ", "
        j = prev[j]
    s += str(dist[src])
    print(s)


def graph_to_adjacency_dict(tupla_dict):
    '''
    :param tupla_dict: słownik, gdzie kluczem jest tupla, a wartością odległość między punktami
    :return: łownik, gdzie kluczem wierzchołki, a wartością krotka (wierzchołek,odległość od niego)
    '''
    adj_dict = {}
    for key in tupla_dict:
        if not ord(key[0]) - 65 in adj_dict.keys():
            adj_dict[ord(key[0]) - 65] = []
        adj_dict[ord(key[0]) - 65].append((ord(key[1]) - 65, tupla_dict[key]))
        if not ord(key[1]) - 65 in adj_dict.keys():
            adj_dict[ord(key[1]) - 65] = []
        adj_dict[ord(key[1]) - 65].append((ord(key[0]) - 65, tupla_dict[key]))
    return adj_dict


def main():
    with open('graf.txt', 'r') as f:       # wczytanie grafu z pliku
        s = f.read()
        graph = ast.literal_eval(s)

    adj = graph_to_adjacency_dict(graph)

    print("Do którego wierzchołka chcesz się udać?")
    dst = input()
    print("Z którego wierzchołka startujesz?")
    src = input()
    if not (isinstance(src, str) and isinstance(dst, str) and len(src) == 1 and len(dst) == 1):
        print("Nie ma takiego wierzchołka")
    else:
        if not ord(src) - 65 in adj.keys() or not ord(dst) - 65 in adj.keys():
            print("Nie ma takiego wierzchołka")
        else:
            dijkstra(adj, len(adj), ord(dst) - 65,  ord(src) - 65)


if __name__ == "__main__":
    main()
