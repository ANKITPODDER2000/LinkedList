from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def print_alternative(head):
    if not head:
        return
    print("Values are : ",end="")
    while head:
        print(head.val,end=" ")
        if not head.next:
            return
        head = head.next.next
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    print_alternative(l1.head)
if __name__ == "__main__":
    main()
