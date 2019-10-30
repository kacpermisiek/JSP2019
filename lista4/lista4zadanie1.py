lista = []
koniec =False
while koniec is False:
    a = int(input("Podaj liczbe do listy\n"))
    lista.append(a)
    b = int(input("Czy chcesz dodac kolejna liczbe do lsity?\nTAK:1\nNIE:2\n"))
    if b is 1:
        koniec = False
    else:
        koniec = True

dzialanie = int(input("Wybierz dzialanie \n [1] SUMA LICZB Z LISTY \n [2] ILOCZYN LICZB Z LISTY\n"))
x = 0
y = 1
if dzialanie == 1:
    for i in range (0,len(lista)):
        x += lista[i]
    print ("Suma liczb {} wynosi: {}".format(lista , x))
else:
    for i in range (0,len(lista)):
        y *= lista[i]
    print("Iloczyn liczb {} wynosi: {}".format(lista , y))
