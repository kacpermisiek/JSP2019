napis = input("Wpisz tekst\n")
py = "Python"
polowa = int((len(napis)/2))

a = napis[0:polowa]
b = napis[polowa:]
napis_nowy = a[0:] + py[0:] + b[0:]
print (napis_nowy)


