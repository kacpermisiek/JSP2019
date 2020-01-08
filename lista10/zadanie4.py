import xml.etree.ElementTree as ET
import pprint
pp = pprint.PrettyPrinter(indent=4)
sciezka = input("Podaj sciezke pliku\n")
class Kurs:
    def __init__(self,path):
        self.path = path
    def wszystkie_kursy(self):
        root = ET.parse(self.path).getroot()
        nazwy = []
        kurs_sredni = []
        kursy = {}
        for x in root.findall('pozycja/nazwa_waluty'):
            nazwy.append(x.text)
        for y in root.findall('pozycja/kurs_sredni'):
            kurs_sredni.append(y.text)
        for i in range(len(nazwy)):
            kursy[nazwy[i]]= float(kurs_sredni[i])
        pp.pprint(kursy)
        return kursy
    def PLN_convert(self):
        root = ET.parse(self.path).getroot()
        cur = self.wszystkie_kursy()
        pp.pprint(cur)
        kasa = float(input("Podaj kwote  "))
        nazwy = []
        for x in root.findall('pozycja/nazwa_waluty'):
            nazwy.append(x.text)
        nazwa = input("Wybierz walute(wpisz pelna nazwe)  ")
        if nazwa in nazwy:
            print('[1]PLN --> {}'.format(nazwa))
            print('[2]{} --> PLN'.format(nazwa),end="  ")
            wyb = int(input())
            if wyb == 1:
                wynik = kasa/cur[nazwa]
                print("\n{} {} = {:.3f} PLN\n".format(kasa, nazwa, wynik))
            else:
                wynik = kasa*cur[nazwa]
                print("\n{} PLN = {:.3f} {}\n".format(kasa,wynik,nazwa))
            return wynik
        else:
            print("Nie znaleziono waluty")
    def X_to_Y(self):
        root = ET.parse(self.path).getroot()
        cur = self.wszystkie_kursy()
        pp.pprint(cur)
        
        waluta1 = input("Wybierz walute poczatkowa  ")
        waluta2 = input("Wybierz walute koncowa  ")
        kasa = float(input("Wpisz kwote  "))
        nazwy = []
        for x in root.findall('pozycja/nazwa_waluty'):
            nazwy.append(x.text)
        if (waluta1 in nazwy) and (waluta2 in nazwy):
            wynik = kasa*cur[waluta1]/cur[waluta2]
            print("\n{} {} = {:.3f} {}\n".format(kasa,waluta1,wynik,waluta2))
            return wynik
        
#Menu
menu = 10
while menu!=0:
    print("""
        $$$ SUPER PRZELICZNIK PIENIEDZY v 1.0.0 $$$
            by: Kacper Misiek
        Wybierz dzialanie:
        [1] Lista dostępnych kursów
        [2] PLN <--> Wybrana waluta
        [3] Wybrana waluta <--> Wybrana waluta
        [0] Zakończ
        """)
    menu = int(input())
    if menu == 1:
          a = Kurs(sciezka).wszystkie_kursy()
          print(a)
    if menu == 2:
          a = Kurs(sciezka).PLN_convert()
    if menu == 3:
          a = Kurs(sciezka).X_to_Y()
