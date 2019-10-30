import re

git = False


while git == False:
    haslo = input("Podaj haslo\n")
    
    xaz = re.search("[a-z]" , haslo)
    xAZ = re.search("[A-Z]" , haslo)
    x09 = re.search("[0-9]" , haslo)
    xspec = re.search("[$#@]" , haslo)
    if xaz is None:
        print("Hasło niepoprawne! Musi zawierac conajmniej jedna mala litere a-z")
        git = False
    else:
        git=True
    if xAZ is None:
        print("Hasło niepoprawne! Musi zawierac conajmniej jedna duza litere A-Z")
        git = False
    else:
        git=True
    
    if x09 is None:
        print("Hasło niepoprawne! Musi zawierac conajmniej jedna cyfre 0-9")
        git = False
    else:
        git=True
    
    if xspec is None:
        print("Hasło niepoprawne! Musi zawierac conajmniej jeden znak specjalny [$#@]")
        git = False
    else:
        git=True
    
    if len(haslo) < 6 or len(haslo)>16:
        print("Haslo musi miec nie mniej niz 6-16 znakow!")
        git = False
    else:
        git=True
if git == True:
    print("Podane haslo jest poprawne :)")

