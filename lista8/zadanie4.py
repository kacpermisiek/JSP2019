import os









try:
    f1 = open('PESEL.txt')
except FileNotFoundError:
                    print('Plik z podanej ścieżki nie istnieje')


def odczyt(x):
    f1.seek(x)
    return f1.read(1)

c1 =  odczyt(0)
c2 =  odczyt(1)
c3 =  odczyt(2)
c4 =  odczyt(3)
c5 =  odczyt(4)
c6 =  odczyt(5)
c7 =  odczyt(6)
c8 =  odczyt(7)
c9 =  odczyt(8)
c10= odczyt(9)
c11= odczyt(10)
c112 = 9*int(c1)+7*int(c2)+3*int(c3)+int(c4)+9*int(c5)+7*int(c6)+3*int(c7)+int(c8)+9*int(c9)+7*int(c10)


print (c112)
print(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11)
    
