n = int(input("Podaj liczbe n\n"))

def harmoniczny(n):
    wynik = 0
    
    for i in range(1,n+1):
        wynik+=(1/i)
    return wynik
suma = harmoniczny(n)
print("Suma ciagu harmonicznego od 1/1 do 1/{} wynosi: {}".format(n,suma))
