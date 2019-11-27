import re

def zaszyfruj(jawny):
    k = 3
    szyfr=[]
    szyfr2=[]
    szyfr_str='  '
    low = False
    up= False
    special = "!@#$%^&*()1234567890_+ {[}]:;|\?/';.>,<`~\""
    for i in range (0,len(jawny)):
        if jawny[i] not in special:
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
    special = "!@#$%^&*()1234567890_+ {[}]:;|\?/';.>,<`~\""
    for i in range (0,len(szyfrowany)):
        if szyfrowany[i] not in special:
            normal.append(ord(szyfrowany[i])+k)
            
        else:
            normal.append(ord(szyfrowany[i]))
    for i in range (0,len(normal)):
        normal2.append(chr(normal[i]))
        normal_str = normal_str[:i] + normal2[i] + normal_str[i+1:]

    return normal_str
    
