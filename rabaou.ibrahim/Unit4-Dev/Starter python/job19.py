from platform import java_ver
from re import A


def myList(*args):
    myList = []
    for n in args:
        myList.append(n)

    for i in range(len (myList)):
        temp = i                        #temp = valeur i
        for j in range(len (myList)):
            if myList[j] > myList[temp]:                            
                temp = j
                myList[i], myList[temp] = myList[temp], myList[i]    #i = valeur j et j = valeur i
    print(myList)

myList(85,16,343,25,4)