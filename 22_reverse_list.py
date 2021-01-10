from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def reverse(head):
    if not head:
        return None
    prev = None
    next = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    l1.display()
    l1.head = reverse(l1.head)
    l1.display()
if __name__ == "__main__":
    main()