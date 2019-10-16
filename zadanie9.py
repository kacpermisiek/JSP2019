import math

Z = complex(input("Podaj liczbe zespolona\n"))
print (Z)
a = float(Z.real)
b = float(Z.imag)
Z_modul = float(math.sqrt(a**2 + b**25))

Z_arg = float(math.cos(a/Z_modul))
print ("Modul liczby zepolonej Z wynosi{}".format(Z_modul))
print ("Argument liczby zespolonej Z wynosi {}".format(Z_arg))
