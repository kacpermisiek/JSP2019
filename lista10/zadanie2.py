import itertools as it

class klasa:
    def __init__(self,lista):
        self.lista = lista
    def perm(self):
        lista2=[]
        for i in range(len(self.lista)+1):
            a = it.combinations(self.lista,i)
            for z in list(a):
                lista2.append(z)
        return lista2               

wynik = klasa([1,2,3])
print("Podlisty danej listy:  {}".format(wynik.perm()))
