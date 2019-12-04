import time as t
import random
def wstawianie(A):
    start = t.time();
    for i in range(1,len(A)):
        klucz = A[i]
        j = i - 1
        while j>=0 and A[j]>klucz:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = klucz
    koniec = t.time()-start
    print (A)
    return koniec

lista=[]
for i in range (0,300):
    lista.append(random.randint(0,20))
print(lista)
print(wstawianie(lista))
#czas dzialania funkcji wyniosl ok 0,04sekundy
