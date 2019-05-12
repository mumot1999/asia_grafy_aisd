from collections import defaultdict
import sys
import time


# klasa reprezentujaca graf
class DFS_lkrawedz:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  #słownik
        self.V = vertices  #konstruktor wierzchołków

    # funkcja dodająca krawędź do grafu
    def addEdge(self, u, v):
        self.graph[u].append(v)


    def topologicalSort_Depth(self, v, odwiedzony, wyn):  #funkcja przeszukuje w głąb każdą sąsiadujący wierzchołek z wierzchołkiem bierzącym


        odwiedzony[v] = True  #zaznaczamy bierzącą wierzchołek jako odwieczoną

        #pętla przechodząca przez sąsiadujące wierzchołki
        for i in self.graph[v]:
            if odwiedzony[i] == False:
                self.topologicalSort_Depth(i, odwiedzony, wyn)


        wyn.insert(0, v) #wstawiamy bierzący wierzchołek, który nie ma już następników aby stworzyć stos przechowujący wyniki




    def topologicalSort_DFS(self):

        global listadfs

        odwiedzony = [False] * self.V #zaznaczamy wszsytkie wierzchołki jako nieodwiedzone
        wyn = []

        spr = 0
        #print(self.graph)

        for i in range(self.V):
            if odwiedzony[i] == False:
                self.topologicalSort_Depth(i, odwiedzony, wyn)  #wywołujemy funkcje pomocniczą aby zapisać topologicznie wierzchołek

        print(wyn) #jak chcesz wywalic wynik sortowania tutaj komentuj
        listadfs = wyn


class DEL_lkrawedzi:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  #słownik zawierający liste krawędzi
        self.V = vertices  #konstruktor wierzchołków

    #funkcja dodająca krawędz do grafu
    def addEdge(self, u, v):
        self.graph[u].append(v)



    def topologicalSort_DEL(self):

        global listadell
        global S
        S = False
        stopien = [0] * (self.V) #tworzymy tablice do przechowywania stopni wszystkich wierzchołków. Na początku nadajemy im wartość 0.

       #wypełniamy tablice ze stopniami aby mieć zapisane stopnie wejsciowe wierzchołków
        for i in self.graph:
            for j in self.graph[i]:
                stopien[j] += 1

        wierz_stop_0 = []

        #dodajemy do tablicy wszystkie wierzchołki ze stopniem wejściowym równym 0
        for i in range(self.V):
            if stopien[i] == 0:
                wierz_stop_0.append(i)


        odwiedzone = 0


        wyn = []


        while wierz_stop_0:


            u = wierz_stop_0.pop(0) #wyodrębniamy i usuwamy przód kolejki
            wyn.append(u)

           #przechodzimy przez wszystkie sąsiednie węzły i zmiejszamy ich stopien o 1 ponieważ przód kolejki został usunięty
            for i in self.graph[u]:
                stopien[i] -= 1

                #Jeśli stopien wejściowy wierzchołka staje się zerowy dodajemy go do kolejki
                if stopien[i] == 0:
                    wierz_stop_0.append(i)

            odwiedzone += 1

        #Spr czy istnieje cykl
        if odwiedzone != self.V:
            print ("Cykl istnieje nie można posortować topologicznie")
            S = True
            sys.exit()
        else:
            print(wyn) #jak chcesz wywalic wynik sortowania tutaj komentuj
            listadell = wyn



from helpers import Timer

def run(liczba):

    v = liczba
    wierzcholki = []
    b= [[0]*v for _ in range(v)]
    dell = DEL_lkrawedzi(v)
    dfs = DFS_lkrawedz(v)
    for i in range(liczba):
        for z in range(liczba):
            if z>i:
                razem = str(i)+str(z)
                w1 = int(i)
                w2 = int(z)
                dell.addEdge(w1,w2)
                dfs.addEdge(w1,w2)
                b[w1][w2] = 1
                wierzcholki.append(razem)


    print("Sortowanie topologiczne przez usuwanie: ")

    timer_sort_topological_del = Timer()
    timer_sort_topological_del.start()

    dell.topologicalSort_DEL()

    #print("Macierz sasiedztwa posortowana DELL:")

    for kl in listadell:
        'print(kl," - " ,b[kl])'

    timer_sort_topological_del.stop()

    if S == False:

        print("\n")
        print("Sortowanie topologiczne metoda DFS: ")

        timer_sort_topological_dfs = Timer()
        timer_sort_topological_dfs.start()

        #print("Macierz sasiedztwa posortowana DFS:")

        for kl in listadfs:
            'print(kl," - " ,b[kl])'

        timer_sort_topological_dfs.stop()

        return {
            'sort_top_del': timer_sort_topological_del.get_mean_time(),
            'sort_top_dfs': timer_sort_topological_dfs.get_mean_time()
        }

    else:
        return False


