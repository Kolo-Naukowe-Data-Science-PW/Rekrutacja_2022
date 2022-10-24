###Brute force

Przykladowe = {
  ("B", "D"): 2,
  ("D", "A"): 1,
  ("B", "A"): 4,
  ("A", "C"): 2,
  ("B", "E"): 3,
  ("C", "D"): 7,
  ("E", "C"): 3
}

def dict_to_list(dane):
    lista = list(dane.items())
    return lista

##------- Znajdz cokolwiek to funkcja, która szuka pojedyńczej ścieżki w danym zbiorze. Jeśli nie znajdzie żadnej, to zwraca -1
def znajdz_co_kolwiek(start_co, koniec_co, dane_co):
    start_kopia = start_co
    koniec_kopia = koniec_co
    dane_kopia = dane_co.copy()
    droga = []
    zle = 0
    while(True):
        for i in dane_kopia:
            if i[0][0] == start_kopia:
                start_kopia = i[0][1]
                droga.append(i)
                dane_kopia.remove(i)
                break
            elif i[0][1] == start_kopia:
                start_kopia = i[0][0]
                droga.append(i)
                dane_kopia.remove(i)
                break
        try:
            if(droga[-1][0][0] == koniec_kopia):
                return droga
            elif(droga[-1][0][1] == koniec_kopia):
                return droga
        except:
            return -1
        if zle == len(droga):
            return -1
        else:
            zle = len(droga)

##-------- Brute force wykorzystuje Znajdz cokolwiek by uzyskać ścieżkę, po czym powtarza proces by sprawdzić inne możliwości
def brutforce(start, koniec, dane):
    mozliwosci = []
    while(True):
        tymczasowy = znajdz_co_kolwiek(start, koniec, dane)
        #print("dane", dane)
        #print("tymczasowy", tymczasowy, "Start i koniec", start, koniec)
        if(tymczasowy == -1):
            return mozliwosci
        else:
            for a in tymczasowy:
                dane_tymczasowe = dane.copy()
                dane_tymczasowe.remove(a)
                b = brutforce(start, koniec, dane_tymczasowe)
                if b != []:
                    for element in b:
                        mozliwosci.append(element)
            mozliwosci.append(tymczasowy)
            dane.remove(tymczasowy[-1])

##------- Liczenie czasu sprawdza czas znalezionych ścieżek
def liczenie_czasu(rozwiaz):
    naj = 9999999
    naj_i = 0
    for i in range(len(rozwiaz)):
        #print("petla i:", rozwiaz[i])
        zliczanie = 0
        for x in range(len(rozwiaz[i])):
            zliczanie = zliczanie + rozwiaz[i][x][1]
        if naj > zliczanie:
            naj = zliczanie
            naj_i = i
    return naj, naj_i

##----- Przeszukiwanie brutforce zbiera wszystkie poprzednie funckje w jedną komendę, by ułatwić użytkowanie
def przeszukanie_brutforce(sta, ko, da):
    if sta == ko:
        print("Odległość zero, jesteś w celu")
        exit()
    dan = dict_to_list(da)
    roz = brutforce(sta, ko, dan)
    try:
        na, na_i = liczenie_czasu(roz)
        print('')
        print("Czas najkrótszej drogi:", na)
        print("Najkrótsza droga:", roz[na_i])
    except:
        print("Nie ma połączenia lub punkty nie istnieją :(")

if __name__ == '__main__':
    przeszukanie_brutforce('C', 'D', Przykladowe)


