import math

a = float (input("Podaj warosc boku a\n"))
b = float (input("Podaj wartosc boku b\n"))
alfa = float (input("Podaj wartosc kata alfa (w stopniach)\n"))
pi = math.pi
sinus_alfa = alfa * pi / 180
pole_trojkata = a * b * sinus_alfa
print ("Pole trojkata wynosi: {:.2f}".format(pole_trojkata))
