myList = [8, 10, 6, 2, 4, 7, 9, 10, 12, 8]  # list to sort


for i in range(len(myList)-1):
    for j in range(len(myList)-1):
        if myList[j] > myList[j + 1]:
            myList[j], myList[j + 1] = myList[j + 1], myList[j]


print(myList)
