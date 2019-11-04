n=int(input("Liczba wierszy: "))
a=[]
i=0
for i in range(i, n):
    a.append([])#dodaje tyle list ile jest n
    a[i].append(1)#dodaje jedynki w kazdej podliscie
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])#rozszerza liste o element ktory jest suma dwoch elementow z poprzedniej listy (4=3+1)
    if(n!=0):#dodaje na koniec listy 1
       a[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ")#robi odstep po lewej stronie piramidy
    for j in range(0,i+1):
        print('{0:5}'.format(a[i][j]),end=" ")#drukuje kolejno elementy wszystkich podlist
    print()
