def myList(*args):
    myList = []
    for n in args:
        myList.append(n)
        myList.sort()
    
    print(myList)

