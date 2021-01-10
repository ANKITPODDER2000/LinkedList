from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def middle_to_head(head):
    prev = None
    mid  = head
    temp_head = head
    c = 0
    while head:
        if c & 1 == 1:
            prev = mid
            mid = mid.next
        head = head.next
        c += 1
    prev.next = mid.next
    mid.next = temp_head
    return mid
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    l1.display()
    l1.head = middle_to_head(l1.head)
    l1.display()
if __name__ == "__main__":
    main()
