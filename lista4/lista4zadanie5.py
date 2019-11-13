from itertools import permutations
lista = []
koniec =False
while koniec is False: #Petla dodajaca liczby do listy
    a = int(input("Podaj liczbe do listy\n"))
    lista.append(a)
    b = int(input("Czy chcesz dodac kolejna liczbe do lsity?\nTAK:1\nNIE:2\n"))
    if b is 1:
        koniec = False
    else:
        koniec = True

def funkcja(*lista): 
    return (list(permutations(lista)))
    
wynik = funkcja(*lista)
print(wynik)
