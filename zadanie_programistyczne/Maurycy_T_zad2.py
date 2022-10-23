import ast#Pobiera z pliku


def znajdz_najblizszy(odleglosc, zrobione):#Znajduje njbliższą nie sprawdzaną ścieżkę wartość
    naj = float('inf')
    naj_klucz = None

    for nazwa, odl in odleglosc.items():
        if nazwa not in zrobione and odl < naj:
            naj = odl
            naj_klucz = nazwa

    return naj_klucz

def dis(graf,start,odleglosc):# algorytm Dis-cośtam

    od={}

    zrobione=[]
    obecny=start
    odleglosc[obecny]=0
    od[obecny]=None

    while obecny:

        for i in graf:# z to sprawdzana druga wartość z tupla
            if obecny in i:
                z = 'A'
                if i[0]==obecny:
                    z=i[1]
                else:
                     z=i[0]

                if odleglosc[z]>odleglosc[obecny]+graf[i]:#SErce jeśli odległóść od punktu jest mniejsza nadpisz punkt
                    odleglosc[z]=odleglosc[obecny]+graf[i]
                    od[z]=obecny
        zrobione.append(obecny)
        obecny=znajdz_najblizszy(odleglosc,zrobione)


    tabela = {}

    for d,c in odleglosc.items():#zapisz do tabeli c= odleglość d=do któego punktu
        tabela[d]=[c,[]]
        ob_d=d
        if ob_d in od: #jakby nie było powiązania
            while od[ob_d]:
                tabela[d][1].append(ob_d)
                ob_d=od[ob_d]

            else:
                tabela[d][1].append(ob_d)

        tabela[d][1]=tabela[d][1][::-1]

    return tabela


def wyswietl(tabela, y):#do punktu chcianego
    if tabela[y][0]==float("inf"):#jak brak powiązania
        print("Nie ma powiązania :(")
        exit()

    print('\n',tabela[y][0],'->',end=' ')
    t=tabela[y][1]
    for i in t:
        print(i,end=' ')

    if len(t) > 2:# szczegóły trasy
        print('\n(')
        for i in range(len(t) - 1):
            try:
                print(t[i], "=>", t[i + 1], ":", graf[t[i], t[i + 1]])
            except KeyError:
                print(t[i], "=>", t[i + 1], ":", graf[t[i + 1], t[i]])
        print(')')

    print("\n\nUdało się"," Udało"*2,"O tak\n Yes I did it ,To sukces")



with open('graf.txt') as f:#pobieranko pliku
    data = f.read()

graf= ast.literal_eval(data)

def pobierz(t,punkty):#sprawdzanie czy dane występują w grafie
    x=''
    while x not in punkty:
        if x!='':
            print("Wartość nie istnieje w grafie")
        x=input(t+' ktorego punktu ')

    return x

punkty=[]
odleglosc={}
for i in graf.keys():#zapisywanie wszyskich punktów i wyznaczenie odległości od każdej najbliższej na nieskończoność
    if i[0] not in punkty:
        punkty.append(i[0])
        odleglosc[i[0]] = float('inf')
    if i[1] not in punkty:
        punkty.append(i[1])
        odleglosc[i[1]] = float('inf')

x=pobierz('Od',punkty)
y=pobierz("Do",punkty)



wyswietl(dis(graf,x,odleglosc),y)
