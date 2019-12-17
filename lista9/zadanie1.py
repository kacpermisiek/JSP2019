import numpy as np
"""
np.std()
np.mean()
np var()
sys.argv
"""
A = np.array([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],[2,6,7,-5,1],[1,2,6,-4,-10]])

B = np.array([[ 6,2,-5,17,12]]).T

wynik = np.linalg.solve(A,B)

print("x: " , wynik[0],'\n','y: ',wynik[1],'\n','z: ' , wynik[2],"\nt: ",wynik[3],"\nu: ", wynik[4], sep='')



