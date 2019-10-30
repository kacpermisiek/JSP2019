lista = []
lista2 = []
x = range(0 , 100 , 3)

for i in x:
    lista.append(i)
print (lista)

del lista[3 : len(lista) :3]
print(lista)
suma = sum(lista)
ilosc = len(lista)
srednia_arytmetyczna = float(suma / ilosc)
print (srednia_arytmetyczna)

