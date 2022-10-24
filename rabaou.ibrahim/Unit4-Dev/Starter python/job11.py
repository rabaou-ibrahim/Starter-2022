from turtle import done


open('domains.xml', 'r')

with open('domains.xml') as domains:
    datafile = domains.readlines()
    i = 0
    for line in datafile:
        if 'domain' in line:
            i+= 1
print(i)
            

            