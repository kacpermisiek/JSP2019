jednosci_nastki = { "jeden":1,
             "dwa":2,
             "trzy":3,
             "cztery":4,
             "piec":5,
             "szesc":6,
             "siedem":7,
             "osiem":8,
             "dziewiec":9,
                "dziesiec":10,
                   "jedenascie":11,
                    "dwanascie":12,
                    "trzynascie":13,
                    "czternascie":14,
                    "pietnascie":15,
                    "szescnascie":16,
                    "siedemnascie":17,
                    "osiemnascie":18,
                    "dziewietnascie":19,}


dziesiatki = {"dwadziescia":2 ,
              "trzydziesci":3 ,
              "czterdziesci":4 ,
              "piecdziesiat":5}
def wypisz(a):
        b=""
        c=""
        
        x=a.find(" ")
        if x is not -1:
                for i in range (0, x):
                        b+= a[i]
                for i in range (x+1 , len(a)):
                        c+= a[i]
                
                print("{}{}".format(dziesiatki[b],jednosci_nastki[c]))
                wynik = int("{}{}".format(dziesiatki[b],jednosci_nastki[c]))
                
                return wynik
        if x is -1:
                if a in jednosci_nastki:
                        print(jednosci_nastki[a]);
                        return (int(jednosci_nastki[a]))
                if a in dziesiatki:
                     print(dziesiatki[a])
                     return (int((dziesiatki[a])))
a = input("Podaj liczbe\n")
wypisz(a)

assert wypisz('trzydziesci trzy') == 33
assert wypisz ('trzynascie') == 13

        


