from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def delete(head):
    if not head:
        return None
    else:
        temp = head.next
        del head
        return delete(temp)
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    l1.display()
    l1.head = delete(l1.head)
    l1.display()
if __name__ == "__main__":
    main()