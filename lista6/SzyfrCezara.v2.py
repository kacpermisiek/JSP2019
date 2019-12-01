def zaszyfruj(jawny):
    k = 3
    szyfr=[]
    szyfr2=[]
    szyfr_str='  '
    
    for i in range (0,len(jawny)):
        if (ord(jawny[i]) >=65 and  ord(jawny[i])<=90) or (ord(jawny[i]) >=97 and ord(jawny[i])<=122):
            szyfr.append(ord(jawny[i])+k)
            
        else:
            szyfr.append(ord(jawny[i]))


    for i in range (0,len(szyfr)):
        szyfr2.append(chr(szyfr[i]))
        szyfr_str = szyfr_str[:i] + szyfr2[i] + szyfr_str[i+1:]

    return szyfr_str

def odszyfruj(szyfrowany):
    k = -3
    normal=[]
    normal2=[]
    normal_str='  '
   
    for i in range (0,len(szyfrowany)):
        if (ord(szyfrowany[i]) >=65 and  ord(szyfrowany[i])<=90) or (ord(szyfrowany[i]) >=97 and ord(szyfrowany[i])<=122):
            normal.append(ord(szyfrowany[i])+k)
        else:
            normal.append(ord(szyfrowany[i]))
    for i in range (0,len(normal)):
        normal2.append(chr(normal[i]))
        normal_str = normal_str[:i] + normal2[i] + normal_str[i+1:]

    return normal_str
