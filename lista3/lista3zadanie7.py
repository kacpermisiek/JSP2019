n = int(input("Podaj liczbe n\n"))
i= 1
x = range(0,n)
lista = []
for i in x:
    if i == 0:
        lista.append(0)
    elif i == 1:
        lista.append(1)
    else:
        lista.append(lista[i-1] + lista[i-2])
print(lista)
        
