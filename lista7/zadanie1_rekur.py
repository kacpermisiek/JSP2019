import time as t
start = t.time()
def fibo_rekur(n):
   if n <= 1:
       return n
   else:
       return(fibo_rekur(n-1) + fibo_rekur(n-2))

n=30

for i in range(n):
    print(fibo_rekur(i))

print ("\n" , t.time()-start)

#czas wyniosl ok. 5 sek
