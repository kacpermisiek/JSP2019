import os


class CiagArytmetyczny:
    def __init__(self,a1,r,n):
        self.a1 = a1
        self.r  = r
        self.n  = n

    def __iter__(self):
        self.start = 1
        return self

    def __next__(self):
        if self.start < self.n:
            i = self.a1
            self.a1 = self.__len__()
            self.start +=1
            return i
        else:
            raise StopIteration()

    def save(self,a1,r,n):
        with open("plik.txt" , "w") as plik:
            tekst = 'a1 = '+str(a1)+'\n r = '+str(r)+'\n n = '+str(n)
            plik.write(tekst)

    def __len__(self):
        return self.a1 + self.r


a = CiagArytmetyczny(1,2,3)
