import math
print ("zamiana(0) = radiany --> stopnie")
print ("zamiana(1) = stopnie --> radiany\n")

def zamiana(N):
    if N==0:
        rad = float(input("Podaj wartosc w radianach\n"))
        stopnie = rad*180/math.pi
        print("{} rad = {:.2f} stopnie/i".format(rad,stopnie))
    if N==1:
        stopnie = float(input("Podaj wartosc w stopniach\n"))
        rad = stopnie*math.pi/180
        print("{} stopnie/i = {:.4f} rad".format(stopnie,rad))
