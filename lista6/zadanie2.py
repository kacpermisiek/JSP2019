import SzyfrCezara as sc

git = False

while git== False:
    wybor = int(input("Co chcesz zrobic: \nSZYFROWANIE[1]\nDESZYFROWANIE[2]\n"))
    if wybor == 1:
        print("Wybrano: SZYFROWANIE")
        zdanie = input("Podaj zdanie do zaszyfrowania\n")
        zdanie = sc.zaszyfruj(zdanie)
        print("tresc zaszyfrowanego zdania:\n" , zdanie)
        wybor2 = int(input("Czy chcesz teraz odszyfrowac zdanie?\nTAK[1]\nNIE[2]\n"))
        if wybor2 == 1:
            print("tresc odszyfrowanego zdania:\n" , sc.odszyfruj(zdanie),"\n\n")
    if wybor == 2:
        print("Wybrano: ODSZYFROWANIE")
        zdanie = input("Podaj zdanie do odszyfrowania\n")
        zdanie = sc.zaszyfruj(zdanie)
        print("tresc odszyfrowanego zdania:\n" , zdanie)
