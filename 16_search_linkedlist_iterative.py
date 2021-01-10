from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def serach(head , key):
    while head:
        if head.val == key:
            return True
        head = head.next
    return False
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    key = int(input("Enter the key to search : "))
    print("%d is in the linked list : %s" % (key, str(serach(l1.head, key))))
    l1.display()
if __name__ == "__main__":
    main()
