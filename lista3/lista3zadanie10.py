x = range(100, 401)
lista=[]
for i in x:
    y = str(i)
    setki = str(y[0])
    setki = int(setki)
    dziesiatki = str(y[1])
    dziesiatki = int(dziesiatki)
    jednosci = str(y[2])
    jednosci = int(jednosci)
    if setki%2 == 0 and dziesiatki%2 == 0 and jednosci%2==0:
        lista.append(i)

print (lista)
        
