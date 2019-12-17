#aby wlaczyc wpisz: "python statystyka.py liczba1,liczba2,liczba3,..."

import sys
import numpy as np

x =''
arg=[]

for i in sys.argv:
    x += i

y = x.find("statystyka.py")+13
x =x[y:]



z = x.split(',')



for i in range(len(z)):
    z[i] = int(z[i])

print(z)

z = np.array(z)
avg = np.mean(z)
print("Średnia liczb:         ", avg)
war = np.var(z)
print("Wariancja liczb:       ",war)
odchylenie = np.std(z)
print("Odchylenie standardowe:",odchylenie)
