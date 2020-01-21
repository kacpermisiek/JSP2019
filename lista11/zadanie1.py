import urllib.request

serwer = 'http://panoramx.ift.uni.wroc.pl/~kmisiek/'
strona = input("Podaj strone\n")
adres = serwer+strona

try:
    urllib.request.urlopen(adres)
    print("Znaleziono strone")
except:
    print("Nie znaleziono storny")
