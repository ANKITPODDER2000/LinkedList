from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def rotate(l1 , k):
    k = k % l1.length()
    head = l1.head
    if k == 0:
        return
    c = 1
    temp_head = head
    while c<k:
        head = head.next
        c += 1
    temp = head.next
    temp1 = temp
    while temp.next:
        temp = temp.next
    head.next = temp.next
    temp.next = temp_head
    l1.head = temp1

def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    k = int(input("Enter the value of k : "))
    l1.display()
    rotate(l1 , k)
    l1.display()
if __name__ == "__main__":
    main()
