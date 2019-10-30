#Z UŻYCIEM IF
a = int(input("Podaj liczbe calkowita\n"))

if a%2 == 0:
    print("Podana liczba jest parzysta\n")
else:
    print("Podana liczba nie jest parzysta\n")

#BEZ UŻYCIA IF
print ("BEZ UŻYCIA IF")

b = int(input("Podaj liczbe:\n"))
wybory = ["liczba jest parzysta","liczba jest nieparzysta"]
print (wybory[0 + b%2])        
