from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def deleteMiddle(head):
    prev = None
    mid = head
    count = 0
    while head:
        if count & 1 == 1:
            prev = mid
            mid = mid.next
        head = head.next
        count += 1
    prev.next = mid.next
    del mid
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    l1.display()
    deleteMiddle(l1.head)
    l1.display()
if __name__ == "__main__":
    main()