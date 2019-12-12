import random
import os

def czyPrzestepny(rok):
    return (rok % 4 == 0) and (rok % 100 != 0) or (rok % 400 == 0)


def pesel():
    rok = random.randint(1800,2099)
    miesiac = random.randint(1,12)
    srok = str(rok)
    if miesiac in [1,3,5,7,8,10,12]: x=31
    elif miesiac in [4,6,9,11]: x=30
    else:
        if czyPrzestepny(rok) is False: x = 28
        else: x=29
    dzien = random.randint(1,x)
    sdzien = str(dzien)
    
    if rok < 1900:
        miesiac += 80
        
    elif rok < 2000:
        miesiac += 0
    elif rok < 2100:
        miesiac += 20
    else:
        miesiac += 40
 

    smiesiac = str(miesiac)

    
    cyfra1 = srok[2]
    cyfra2 = srok[3]
    if miesiac < 10:
        cyfra3=str(0)
        cyfra4=smiesiac
    else:
        cyfra3 = smiesiac[0]
        cyfra4 = smiesiac[1]


    if dzien <10:
        cyfra5 = str(0)
        cyfra6 = sdzien
    else:
        cyfra5 = sdzien[0]
        cyfra6 = sdzien[1]

    cyfra7 = str(random.randint(0,9))
    cyfra8 = str(random.randint(0,9))
    cyfra9 = str(random.randint(0,9))
    cyfra10 = str(random.randint(0,9))
    cyfra11 = 9*int(cyfra1)+7*int(cyfra2)+3*int(cyfra3)+int(cyfra4)+9*int(cyfra5)+7*int(cyfra6)+3*int(cyfra7)+int(cyfra8)+9*int(cyfra9)+7*int(cyfra10)
    scyfra11 = str(cyfra11)
    scyfra11=scyfra11[-1]
    PESEL = str(cyfra1+cyfra2+cyfra3+cyfra4+cyfra5+cyfra6+cyfra7+cyfra8+cyfra9+cyfra10+scyfra11)
    return PESEL
    

f1 = open('PESEL.txt', 'w')
for i in range(0,10):
    f1.write(pesel())
    f1.write('\n')
f1.close() 
