import math
a = 100
print("a // b: \n" , "100//3=" , 100//3 ,"\n", "2//3=" ,  2//3  , "\n"  , "53//2=" ,  53//2 , "\n" , "5//2=" ,5//2 , "\n")
print("round(a / b): \n" , "100/3=" , round(100/3 , 6) ,"\n", "2/3=" ,  round(2/3 , 16)  , "\n"  , "53/2=" ,  round(53/2) , "\n" , "5/2=" ,round(5/2 , 1) , "\n")
print("floor(a / b): \n" , "100/3=" , math.floor(100/3) ,"\n", "2/3=" ,  math.floor(2/3)  , "\n"  , "53/2=" ,  math.floor(53/2) , "\n" , "5/2=" , math.floor(5/2
                                                                                                                                                             ) , "\n") 

#Opcja dzielenia bez reszty zwraca wynik dzielenia, ucinajac przy tym liczby po przecinku
#Opcja round(float) zaokragla liczbe do x cyfr po przecinku (zmienna float moze miec maksymalnie 16 cyfr po przecinku
#Opcja floor(float) zwraca liczbe calkowita mniejsza badz rowna liczbie x
