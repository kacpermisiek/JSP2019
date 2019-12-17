import numpy as np
import matplotlib.pyplot as plt


g = 9.81
V0 = float(input("Podaj predkosc poczatkowa [m/s]\n"))
a = float(input("Podaj kat alfa [deg]\n"))

a = a*np.pi/180
hmax = (np.sin(a)*V0)**2/(2*g)
z = (V0**2*np.sin(2*a))/g
tl = (2*V0*np.sin(a))/g

print("Wysokosc maksymalna: {:.2f} metra/ow" .format(hmax))
print("Zasieg: {:.2f} metra/ow".format(z))
print("Czas lotu: {:.2f} sekund".format(tl))

Vy0 = np.sin(a)*V0
t = np.linspace(0,tl,100)
ones = np.linspace(1,1,100)
Vyt =(Vy0 - g*t)
Vx = V0*np.cos(a)
Vxt = Vx*ones
Xt = Vxt*t
Yt = Vy0*t-(g*t**2)/2

plt.subplots_adjust(hspace=0.9)
plt.subplot(311)
plt.grid()
plt.title('Predkosc chwilowa w kierunku pionowym i poziomym po czasie t', fontsize=10)
plt.ylabel('Vy[m/s]',color='b')
plt.xlabel('t[s]')

plt.plot(t,Vyt,'b-')

plt.twinx()

plt.plot(t,Vxt,'r-')
plt.ylabel('Vx[m/s]',color='r')





plt.subplot(312)
plt.grid()
plt.title('Polozenie w funkcji czasu')
plt.xlabel('t[s]')
plt.ylabel('r[m]')
r= np.sqrt((Xt**2)+(Yt**2))
plt.plot(t,r)


plt.subplot(313)
plt.ylabel('y[m]')
plt.xlabel('x[m]')
plt.axis('equal')
plt.plot(Xt,Yt)
plt.grid()


plt.show()








