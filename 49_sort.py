from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def sort_ll(l1):
    head = l1.head
    while head.next:
        if head.next.val < 0:
            val = head.next.val
            head.next = head.next.next
            l1.insert_beg(val)
            temp = head.next
            del temp
        else:
            head = head.next

def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    sort_ll(l1)
    l1.display()
if __name__ == "__main__":
    main()