import trojkat as t

git = False
lista=[]
while git == False:
    a = int(input("Podaj wartosc a\n"))
    b = int(input("Podaj wartosc b\n"))
    c = int(input("Podaj wartosc c\n"))
    lista.extend([a,b,c])
    lista.sort()
    if lista[2] >= lista[0] + lista[1]:
        git = False
        print ("Podano nieprawidlowe wartosci bokow trojkata. Sprobuj ponownie")
    else:
        git = True
        print ("Obwod trojkata:", t.obw(a,b,c))
        print ("Pole trojkata:" , t.pole(a,b,c))
        print (t.rodzaj(a,b,c))
        print (t.kat(a,b,c))
    


