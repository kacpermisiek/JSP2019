import math as m
def obw(a,b,c):
    return a+b+c
def pole(a,b,c):
    wynik = (m.sqrt(float((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))))/4
    return wynik
def rodzaj(a,b,c):
    if a==b==c:
        return 'Trojkat abc jest rownoboczny'
        
    elif a==b or b==c or a==c:
        return 'Trojkat jest rownoramienny'
    else:
        return 'Trojkat jest roznoboczny'
def kat(a,b,c):
    lista=[]
    lista.extend([a,b,c])
    lista.sort()
    
    if lista[2]**2 > lista[0]**2 + lista[1]**2:
        return 'trojkat jest rozwartokatny'
    elif lista[2]**2 == lista[0]**2 + lista[1]**2:
        return 'trojkat jest prostokatny'
    else:
        return'trojkat jest ostrokatny'
    
        
    
        

    
