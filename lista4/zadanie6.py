print ("RGB --> HSV")
R = float(input("Podaj wartosc R\n"))
G = float(input("Podaj wartosc G\n"))
B = float(input("Podaj wartosc B\n"))
R=R/255
G=G/255
B=B/255

def Minimalna(R,G,B):#Funkcja znajdujaca najmniejsza liczbe sposrod RGB
    Cmin=0
    if R<G and R<B:
        Cmin = R
    if G<R and G<B:
        Cmin = G
    if B<R and B<G:
        Cmin = B
    return Cmin


def Maksymalna(R,G,B):#Funkcja znajdujaca najwieksza liczbe sposrod RGB
    Cmax=R
    if G>Cmax:
        Cmax = G
    if B>Cmax:
        Cmax=B
    return Cmax

Cmax= Maksymalna(R,G,B)
Cmin = Minimalna(R,G,B)
delta = Cmax-Cmin

warunek_delta = True
if delta ==0:
    warunek_delta=False


def Hue(R,G,B,Cmax,delta):#Obliczanie H
    if delta == 0:
        H=0
        
    if warunek_delta == True:
        if Cmax==R:
            H=60*(((G-B)/delta)%6)
        if Cmax==G:
            H=60*(((B-R)/delta)+2)
        if Cmax ==B:
            H=60*(((R-G)/delta)+4)
    
    return H

H=Hue(R,G,B,Cmax,delta)


warunek_Cmax =True
if Cmax==0:
    warunek_Cmax=False
    
def Saturation (delta,Cmax,warunek_Cmax):#Obliczanie S
    if warunek_Cmax ==False:
        S=0
    else:
        S=delta/Cmax*100
        print (S)
    return S
S = Saturation (delta,Cmax,warunek_Cmax)
V = Cmax*100
print ("H: " , H,"°")
print ("S: " , S,"%")
print ("V: " , V,"%")
print("(H , S , V): ({:.0f}° ,{:.0f}% ,{:.0f}%) ".format(H,S,V))




    
    
