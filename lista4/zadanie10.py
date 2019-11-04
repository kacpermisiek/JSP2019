a = int(input("Podaj liczbe a\n"))
b = int(input("Podaj liczbe b\n"))
lista_a=list()
lista_b=list()

def pierwsza(a):
    for i in range(2,a+1):
        if a%i==0:
            lista_a.append(i)
    return lista_a
lsita_a=pierwsza(a)

def druga(b):
    for i in range(2,b+1):
        if b%i==0:
            lista_b.append(i)
    return lista_b
lista_b=druga(b)

lista_a.reverse()
lista_b.reverse()
print(lista_a)
print(lista_b)
wynik=0

def TaSama(lista_a,lista_b, wynik):
    for i in range (0, len(lista_a)):
        if lista_a[i] in lista_b:
            wynik = lista_a[i]
            break
    return wynik

wynik=TaSama(lista_a,lista_b,wynik)
print(wynik)
if wynik ==0:
    print("Podane liczby nie maja wspolnego dzielnika")
else:
    print("Najwiekszy wspolny dzielnik podanych liczb wynosi: " ,wynik)
    

