import SzyfrCezara as SC
import time as t
import glob, os


gituwa, gituwa2=True,True

path = input('Podaj ścieżkę do folderu z zaszyfrowanymi plikami\n')

os.chdir(path)
for file in glob.glob("plik_zaszyfrowany*.txt"):
    k=int(file[17:18])
    print(k)
  
    path2=path+'/'+file
    data = open(path2,"r")
    tekst = data.read()
    SC.odszyfruj(tekst,k)
    gituwa=False



Y=t.strftime("%Y")
m=t.strftime("%m")
d=t.strftime("%d")

sciezka = input('Podaj ścieżkę, gdzie plik ma być zapisany(zakończ \, jeżeli w obecnym folderze kliknij enter): ')
plik=sciezka+'plik_deszyfrowany{}_{}{}{}.txt'.format(k,Y,m,d)
szyfr=(SC.odszyfruj(tekst,k))

zapis = open(plik,"w")
zapis.write(szyfr)
zapis.close()
warunek2=False

