def zaszyfruj(jawny,k):
    male , duze = range(97,123), range(65,91)
    
    x= 0
    tekst = ''
    for i in jawny: 
        if (ord(i) in male) or (ord(i) in duze):
            tekst = tekst+chr(ord(jawny[x])+k)
            x+=1
        else:
            tekst = tekst+jawny[x]
            x+=1
    return tekst


def odszyfruj(szyfrowany,k):
    x=0
    tekst=''
    male,duze =  range(97+k,123+k),range(65+k,91+k)
    for i in szyfrowany: 
        if (ord(i) in male) or (ord(i) in duze):
            tekst = tekst+chr(ord(szyfrowany[x])-k)
            x+=1
        else:
            tekst = tekst+szyfrowany[x]
            x+=1
    return tekst
