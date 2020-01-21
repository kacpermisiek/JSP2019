import re

text = input("Podaj tekst ")
a  = re.findall(' a[a-zA-Z]+| A[a-zA-Z]+| e[a-zA-Z]+| E[a-zA-Z]+',text)
print(a)
