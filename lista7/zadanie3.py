import random
import time as t


def babelkowe(A):
    start = t.time()
    for i in range(len(A) - 1, 0, -1):
        for j in range(i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    print (A)
    return t.time()-start


lista=[]
for i in range (0,300):
    lista.append(random.randint(0,20))
print(lista)
print(babelkowe(lista))

#czas dzialania funkcji to ok 0.17sek




