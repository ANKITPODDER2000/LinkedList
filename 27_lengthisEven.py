from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def evenLength(l1):
    return (l1.length() % 2) == 0
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    print("Length of linkedlist is even : ",evenLength(l1))
if __name__ == "__main__":
    main()