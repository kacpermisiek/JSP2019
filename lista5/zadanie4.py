klucz = {'a' : 'y','e' : 'i','i' : 'o','o' : 'a','y' : 'e'}


odklucz = {'y' : 'a','i' : 'e','o' : 'i','a' : 'o','e' : 'y'}


def szyfrowanie():
    t=input('Podaj tekst do zaszyfrowania: ')
    l=len(t)
    szyfr=''
    for i in range(l):
        if t[i] in klucz:
            szyfr+=klucz[t[i]]
        else:
            szyfr+=t[i]
    return szyfr

def deszyfrowanie():
    t=input('Podaj tekst do deszyfrowania: ')
    l=len(t)
    deszyfr=''
    for i in range(l):
        if t[i] in odklucz:
            deszyfr+=odklucz[t[i]]
        else:
            deszyfr+=t[i]
    return deszyfr

decyzja=int(input('Wybierz co chcesz zrobić(0 - szyfrowanie, 1 - deszyfrowanie): '))
if decyzja==0:
    print(szyfrowanie())
else:
    print(deszyfrowanie())

    




