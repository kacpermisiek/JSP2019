import math
import sys
git = False

while git == False:
    a = float(input("Podaj liczbe a równania\n"))
    if a != 0:
        git = True
    else:
        print("a nie moze byc rowne 0 - nie bedzie to funkcja kwadratowa")
b = float(input("Podaj liczbe b równania\n"))
c = float(input("Podaj liczbe c równania\n"))

delta = float((b*b) - 4*(a*c))
if delta < 0:
    print("Równanie to nie ma rozwiązan w zbiorze liczb rzeczywistych.")
    sys.exit(0)
delta_pierw = float(math.sqrt(delta))


if delta > 0:
    print("Równanie to ma 2 rozwiązania:\n")
    x1 = float(-1*b - delta_pierw)/(2*a)
    x2 = float(-1*b + delta_pierw)/(2*a)
    print("x1= {}\n x2= {}".format(x1,x2))
else:
    print("Równanie to ma 1 rozwiązanie:\n")
    x1 = float((-1*b)/(2*a))
    print("x1=" , x1)








