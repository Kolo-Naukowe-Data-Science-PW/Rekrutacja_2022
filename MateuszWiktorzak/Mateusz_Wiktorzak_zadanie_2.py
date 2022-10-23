import sys

# Sluzy do stwarzania wierzcholkow
class Wierzcholek:

    def __init__(self, odw, pop, dys):
        self.odwiedzony = odw
        self.poprzednik = pop
        self.dystans = dys

# Znajduje najkrotsza dostepna droge od danego wierzcholka
def znajdz_najmniejsza_odleglosc(lista):

    min_wierzcholek = -1
    min_dystans = sys.maxsize

    for i in range(len(lista)):
        if lista[i].odwiedzony == False and lista[i].dystans < min_dystans:
            min_wierzcholek = i
            min_dystans = lista[i].dystans

    return min_wierzcholek

# Glowny algorytm, aktualizuje najkrotsze drogi do wirzcholkow
def znajdz_najkrotsza_droge(graf, poczatkowy):

    poczatkowy -= 1

    lista = []

    for i in range(len(graf)):
        lista.append(Wierzcholek(False, -1, sys.maxsize))

    act = poczatkowy
    lista[act].dystans = 0

    while act != -1:
        lista[act].odwiedzony = True

        for i in range(len(lista)):
            if graf[act][i] > 0 and lista[act].dystans + graf[act][i] < lista[i].dystans:
                lista[i].dystans = lista[act].dystans + graf[act][i]
                lista[i].poprzednik = act

        act = znajdz_najmniejsza_odleglosc(lista)

    return lista

# Wypisuje szukany wynik: pomiedzy jakimi punktami jest droga i jaki jest wtedy dystans
def pokaz_najkrotsza_sciezke(lista, koncowy):

    koncowy -= 1

    act = koncowy
    res = [koncowy]
    while lista[act].poprzednik != -1:
        res.insert(0,lista[act].poprzednik)
        act = lista[act].poprzednik

    if len(res) == 1:
        print("Nie ma drogi z punktu do tego samego punktu")
        return

    print(f"Oto najkrótsza droga od wierzchołka {res[0] + 1} do {res[len(res)-1] + 1}: ")
    for i in range(len(res) - 1):
        print(res[i] + 1, end= "->")

    print(res[len(res) - 1] + 1)
    print(f"Dystans wynosi {lista[koncowy].dystans}")

# operuje pozostalymi funkcjami, pyta na konsoli pomiedzy jakimi wierzcholkami jest szukana droga
def znajdz_najkrotsza_sciezke_w_grafie(graf):

    poczatkowy = int(input("Podaj wierzchołek początkowy (liczbę, A -> 1, B -> 2, itd.) : "))

    koncowy = int(input("Podaj wierzchołek końcowy (liczbę, A -> 1, B -> 2, itd.) : "))

    lista = znajdz_najkrotsza_droge(graf, poczatkowy)

    pokaz_najkrotsza_sciezke(lista, koncowy)

def main():

    #sprawdzenie zadanego przykladu:

    '''
    {
    ("B", "D"): 2,
    ("D", "A"): 1,
    ("B", "A"): 4,
    ("A", "C"): 2,
    ("B", "E"): 3,
    ("C", "D"): 7,
    ("E", "C"): 3
    }
    '''

    # graf przedstawiony jako macierz
    graf = [[0,4,2,1,0],
            [4,0,0,2,3],
            [2,0,0,7,3],
            [1,2,7,0,0],
            [0,3,3,0,0]]

    # Znajdywanie najkrotszej drogi (poczatkowy i koncowy wierzcholek wprowadza sie na konsoli)
    znajdz_najkrotsza_sciezke_w_grafie(graf)


if __name__ == '__main__':
    main()










