m = int(input("Podaj liczbe wierszy\n"))
n = int(input("Podaj liczbe kolumn\n"))
m+=1
n+=1
for y in range(1, m):
    print ("\t".join( (str(x*y) for x in range(1, n))))
