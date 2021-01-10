from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def swap(head):
    while head:
        if not head.next:
            return
        head.val, head.next.val = head.next.val , head.val
        head = head.next.next
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    l1.display()
    swap(l1.head)
    l1.display()
if __name__ == "__main__":
    main()
