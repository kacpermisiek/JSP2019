n = int(input("Podaj liczbe n:\n"))

def silnia(n):
    x = range(1, n+1)
    wynik =1
    for i in x:
        wynik = wynik*i
    return wynik

factorial = silnia(n)

print("Silnia z liczby {} wynosi {}" .format(n , factorial))
