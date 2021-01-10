from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def print_alternative(head , t):
    if not head:
        return
    else:
        if t:
            print(head.val , end=" ")
        t = not t
        return print_alternative(head.next, t)
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    print("Linkedlist is (alternative ) : ",end="")
    print_alternative(l1.head  , True)
if __name__ == "__main__":
    main()
