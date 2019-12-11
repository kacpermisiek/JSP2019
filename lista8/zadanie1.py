import os
import SzyfrCezara as SC
import time as t

x=0
wiersze = ''
wiersze2=''



wybor = int(input("[1] Wybierz aktualna sciezke \n[2] Wpisz recznie sciezke"))
if wybor == 1:
    cwd = os.getcwd()
else:
    cwd = input("Podaj sciezke")
    f6=open(cwd)
     


gituwa = True
while gituwa:
    plik = input("Podaj nazwe pliku\n")
    try:  
        f1 = open(plik,"r")
        gituwa = False
    except:
        print("Podano nieprawidlowa nazwe pliku!")
        

folder = input("Podaj nazwe folderu do zapisu pliku\n")
gituwa = True
while gituwa:
    try:
        k = int(input("Podaj przesuniecie liter szyfru (1-10)\n"))
        if k < 1 or k >10:
            print("Podano nieprawidlowa wartosc k")    
        else:
            gituwa = False
    except:
        print("Podano nieprawidlowa wartosc")


Y = t.strftime("%Y")
m = t.strftime("%m")
d = t.strftime("%d")
plik_new = 'plik_zaszyfrowany{}_{}{}{}.txt'.format(k,Y,m,d)

if folder not in os.listdir(os.getcwd()):
    f3 = os.makedirs(folder)


f1.seek(0)

wiersze = f1.readlines()

for i in wiersze:
    try:
        wiersze2 +=(SC.zaszyfruj(wiersze[x],k))
        x+=1
    except:
        ValueError
f1.close()
f4 = os.chdir(os.getcwd()+"\\"+folder)
print(os.getcwd())
gituwa = True
while gituwa:
    try:
        f2 = open(plik_new,"w")
        f2.write(wiersze2)
        f2.close()
        gituwa = False
    except:
        print("ERROR -- nie mozna zapsisac niektorych znakow w pliku tekstowym. Zalecane jest zmniejszenie liczby k do 5)")
        gituwa = False
