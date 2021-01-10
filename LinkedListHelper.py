def CreateLinkedList(l1, func=int):
    print("Enter the number : ",end="")
    num = [func(x) for x in input().split(" ")]
    for i in num:
        l1.insert_end(i)
    return l1
