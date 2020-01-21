import urllib as url
import sys


x = sys.argv[1:][0]
print(x)
if x[-1] is "/":
    baza = 'index.html'
else:
    end = len(x)
    f = x.rfind('/')
    baza = x[f+1:]

print(baza)


f1 = open(baza, "w")
f1.write(x)
f1.close()
