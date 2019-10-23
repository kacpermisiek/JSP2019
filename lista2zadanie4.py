tekst = input("Wpisz tekst:\n")
x = tekst[0]
tekst =  tekst.replace( x , "$")
tekst = x + tekst[1:]
print (tekst)