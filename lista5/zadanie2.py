a = int(input("Podaj liczbe od 1 do 1999\n"))

jednosci = [" ", "jeden","dwa","trzy","cztery","piec","szesc",
                    "siedem","osiem","dziewiec",]
nastki =["dziesiec","jedenascie",
                    "dwanascie","trzynascie","czternascie","pietnascie",
                    "szescnascie","siedemnascie","osiemnascie","dziewietnascie",]
dziesiatki = ["","","dwadziescia","trzydziesci","czterdziesci","piecdziesiat",
              "szescdziesiat","siedemdziesiat","osiemdziesiat","dziewiecdziesiat",]

setki = ["", "sto" , "dwiescie" , "trzysta" , "czterysta" , "piecset" ,
         "szescset" , "siedemset" , "osiemset", "dziewiecset"]

tysiac = 'tysiac'

def wypisz(a):
    a2 = str(a)
    x = len(str(a))
    lista =[]
    for i in range (0,x):#utworzenie listy z pojdeynczymi cyframi
        lista.append(a2[i])
    for i in range (0,x):#zamiana cyfr z str na int
        lista[i] = int(lista[i])
    cyfry = len(lista)
    if a<20 and a>9:
        wynik = nastki[a-10]
        print (wynik)
        return wynik
    elif lista[-2] is 1:
        if cyfry is 3:
            wynik = (str(setki[lista[0]])+' '+str(nastki[lista[0-1]]))
            szukaj1 = wynik.find('   ')
            szukaj = wynik.find('  ')
            if szukaj1 != -1:
                wynik= wynik[0:szukaj1] + wynik[szukaj1+2:]
            elif szukaj != -1:
                wynik= wynik[0:szukaj] + wynik[szukaj+1:]
            print(wynik)
            return wynik
        if cyfry is 4:
            wynik = (str(tysiac)+' '+str(setki[lista[1]])+' '+str(nastki[lista[0-1]]))
            szukaj1 = wynik.find('   ')
            szukaj = wynik.find('  ')
            if szukaj1 != -1:
                wynik= wynik[0:szukaj1] + wynik[szukaj1+2:]
            elif szukaj != -1:
                wynik= wynik[0:szukaj] + wynik[szukaj+1:]
            print (wynik)
            return wynik
        
    else:
        if cyfry is 1:
            wynik = jednosci[lista[0]]
            print(wynik)
            return wynik
        if cyfry is 2:
            wynik = str((dziesiatki[lista[0]]) +' '+ str(jednosci[lista[1]]))
            szukaj1 = wynik.find('   ')
            szukaj = wynik.find('  ')
            if szukaj1 != -1:
                wynik= wynik[0:szukaj1] + wynik[szukaj1+2:]
            elif szukaj != -1:
                wynik= wynik[0:szukaj] + wynik[szukaj+1:]
            print(wynik)
            return wynik
        if cyfry is 3:
            wynik = (str(setki[lista[0]])+' '+str(dziesiatki[lista[1]])+' '+ str(jednosci[lista[2]]))
            szukaj1 = wynik.find('   ')
            szukaj = wynik.find('  ')
            if szukaj1 != -1:
                wynik= wynik[0:szukaj1] + wynik[szukaj1+2:]
            elif szukaj != -1:
                wynik= wynik[0:szukaj] + wynik[szukaj+1:]
            print(wynik)
            return wynik
        if cyfry is 4:
            wynik = (str(tysiac)+' '+str(setki[lista[1]])+' '+ str(dziesiatki[lista[2]])+' ' +str(jednosci[lista[3]]))
            szukaj1 = wynik.find('   ')
            szukaj = wynik.find('  ')
            if szukaj1 != -1:
                wynik= wynik[0:szukaj1] + wynik[szukaj1+2:]
            elif szukaj != -1:
                wynik= wynik[0:szukaj] + wynik[szukaj+1:]
            print (wynik)
            return wynik
    
                                          
wypisz(a)
assert wypisz(698) == 'szescset dziewiecdziesiat osiem'
assert wypisz(1511) == 'tysiac piecset jedenascie'
