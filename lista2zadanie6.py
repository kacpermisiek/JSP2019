lista = ["Kasia" , "Basia" , "Marek" , "Darek"]
lista.append("Józek")
lista_2 = ["Ania" , "Basia"]
lista = lista + lista_2
lista.sort()
print(lista)
print("Czwarty student na liscie: " , lista[4] , "\n")

print("Dwoch pierwszych studentow na liscie: " , lista[:2] , "\n")

print("Dwoch ostatnich studentow na liscie: " , lista[-2:] , "\n")

while "Basia" in lista:
    lista.remove("Basia")


print(lista)
i = len(lista)
print ("Ilosc studentow: " , i)

krotka = tuple(lista)

print (krotka)