#ZADANIE 1
l = [0,10,8,3,5,4,7]
for i in range (0, len(l)):
    if int(l[i])%2 ==1:
        print (l[i])

#ZADANIE 2

n = int(input("Podaj liczbe n\n"))

for i in range(1,n+1): print("*"*i)
for i in range(n-1,0,-1): print("*"*i)
