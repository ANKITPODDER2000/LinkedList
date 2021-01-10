from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def remove_duplicates(head):
    while head:
        temp = head.next
        while temp and temp.val==head.val:
            temp = temp.next
        head.next = temp
        head = head.next
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    l1.display()
    remove_duplicates(l1.head)
    l1.display()
if __name__ == "__main__":
    main()