from LinkedListHelper import CreateLinkedList
def _isCircular(l1):
    head = l1
    l1 = l1.next
    while l1!=None and l1!=head:
        l1 = l1.next
    return l1==head
def main():
    l1 = CreateLinkedList()
    # temp = l1.head
    # while temp.next != None:
    #     temp = temp.next
    # temp.next = l1.head
    print("Is there any circle in linked list : ",_isCircular(l1.head))
    
    
if __name__ == "__main__":
    main()