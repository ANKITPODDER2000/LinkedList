from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def sort_012(l1):
    pointer0 = pointer1 = pointer2 = None
    temp0 = temp1 = temp2 = None
    head = l1.head
    while head:
        if head.val==0:
            if pointer0==None:
                pointer0 = head
                temp0 = pointer0
            else:
                pointer0.next = head
                pointer0 = pointer0.next
        elif head.val == 1:
            if pointer1 == None:
                pointer1 = head
                temp1 = pointer1
            else:
                pointer1.next = head
                pointer1 = pointer1.next
        else:
            if pointer2 == None:
                pointer2 = head
                temp2 = pointer2
            else:
                pointer2.next = head
                pointer2 = pointer2.next
        head = head.next
    pointer0.next = temp1
    pointer1.next = temp2
    pointer2.next = None
    l1.head = temp0

def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    l1.display()
    sort_012(l1)
    l1.display()
if __name__ == "__main__":
    main()
