 

a = int(input("Taper a = "))
b = int(input("Taper b = "))
c = int(input("Taper c = "))
d = int(input("Taper d = "))
e = int(input("Taper e = "))
f = int(input("Taper f = "))

myList = []
for n in (a, b, c, d, e, f):
        myList.append(n)
for n in myList:
        if n%2 == 0:
            print(n)