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
f1.close()
c112=str(c112)
c112=c112[-1]
dzien = c5+c6
plec=''
if int(c112) == int(c11):
    if int(c10)%2==0:
        plec = "Kobieta"
    else:
        plec = "Mężczyzna"
    
PESEL = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11

miesiac = c3+c4
if int(miesiac)>80:
    rok = '18'
    imiesiac=int(miesiac)-80
elif int(miesiac) > 60:
    rok = '22'
    imiesiac=int(miesiac)-60
elif int(miesiac) > 40:
    rok = '21'
    imiesiac= int(miesiac)-40
elif int(miesiac) > 20:
    rok = '20'
    imiesiac= int(miesiac)-20
else:
    rok = '19'
    imiesiac = int(miesiac)

rok += c1+c2

print("nr PESEL: {}\nData urodzenia: {}-{}-{};   płeć: {}".format(PESEL,dzien,imiesiac,rok,plec))
