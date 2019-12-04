import time as t

start = t.time()
a=0
b=1
n=50
print(a)
print(b)
for i in range(1, n - 1):
    a, b = b, a + b
    print(b)

print("\n")
print (t.time()-start)

#czas wyniosl ok. 0,7sek
