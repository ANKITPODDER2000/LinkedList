from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def delete_alternative(l1):
    head = l1.head
    if not head:
        return
    while head:
        if not head.next:
            return
        head.next = head.next.next
        head = head.next
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    l1.display()
    delete_alternative(l1)
    l1.display()
if __name__ == "__main__":
    main()
