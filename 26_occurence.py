from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def count(head , num):
    c = 0
    while head:
        if head.val == num:
            c += 1
        head = head.next
    return c
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    num = int(input("Enter the number : "))
    print("Occurence of %d in the linkedlist is = %d"%(num , count(l1.head , num)))
if __name__ == "__main__":
    main()