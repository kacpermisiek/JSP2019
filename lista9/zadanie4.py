import numpy as np
import matplotlib.pyplot as plt

etykiety =['Java' , 'C' , 'Python' , 'C++' , 'C#' , 'VisualBasic.NET' , 'JavaScript' , 'PHP' , 'SQL' , 'Swift']
wartosci = [17.253,16.086,10.308,6.196,4.801,4.743,2.090,2.048,1.843,1.490]
plt.bar(etykiety,wartosci)
plt.tick_params(labelsize=5)
plt.ylabel("Popularnosc [%]")
plt.xlabel("Język")
plt.grid(axis='y')
plt.title("TIOBE Index for December 2019")
plt.show()
