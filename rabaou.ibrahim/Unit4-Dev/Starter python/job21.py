from inspect import ArgSpec

def mySort(*args):
    
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

def myDisplay(*args):
    myList = []
    print(myList)

mySort(2, 4, 4, 1, 10, 4)