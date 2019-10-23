import math
#zadanie 1
d = int (input("Wpisz liczbe a\n"))
e = int (input ("Wpisz liczbe b\n"))
f = d%e
print ("Reszta z dzielenia a/b wynosi: {}".format(f))

#zadanie 2

a = float(input("Wpisz dlugosc boku a\n"))
b = float(input("Wpisz dlugosc boku b\n"))
c = float(input("Wpisz dlugosc boku c\n"))

cosinus = math.acos((a**2+b**2-c**2)/(2*a*b))
alfa = float(cosinus * 180  / math.pi)

print (round(alfa , 3))
