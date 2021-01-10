from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def multiply(l1 , l2):
    LEN = l1.length() - 1
    num1 = 0
    head = l1.head
    while head:
        num1 = num1 + (head.val*(10 ** LEN))
        LEN -= 1
        head = head.next
    
    LEN = l2.length() - 1
    num2 = 0
    head = l2.head
    while head:
        num2 = num2 + (head.val*(10 ** LEN))
        LEN -= 1
        head = head.next
    return num1 * num2
    
def main():
    l1 = LinkedList()
    l2 = LinkedList()
    CreateLinkedList(l1)
    CreateLinkedList(l2)
    print("Mul : ",multiply(l1 , l2))
if __name__ == "__main__":
    main()
