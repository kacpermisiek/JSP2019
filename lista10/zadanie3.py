import itertools as it

class klasa:
    def __init__(self,lista):
        self.lista = lista
    def perm(self):
        lista2=[]
        a = it.combinations(self.lista,3)
        for z in list(a):
            if sum(z)==0:
                lista2.append(z)
        return lista2
        
a = klasa([1,2,3,4,5,-7,-3])
print(a.perm())
