import math as m

r=float(input("Podaj promien kola\t"))

class Kolo:
    def Pole(r):
        return m.pi*r**2
    def Obwod(r):
        return 2*m.pi*r

print("Pole kola wynosi:   {}".format(Kolo.Pole(r)))
print("Obwod kola wynosi:  {}".format(Kolo.Obwod(r)))
    
