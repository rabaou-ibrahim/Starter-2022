def myList_odd_numbers(*args):

    myList = []
    for n in args:
        myList.append(n)
    for n in myList:
        if n%2 == 0:
            print(n)

