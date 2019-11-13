def zamien(rzym):
    slownik = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
    }
    liczr = list(rzym)
    i=len(rzym)
    last = 0
    res = 0
    while i>0:
        a = slownik[liczr[i-1]]
        if a>=last:
            last = a
            res+=a
        else:
            res-=a
        i-=1
    return(res)

liczba=input('Podaj liczbę rzymską: ')
print(zamien(liczba))
