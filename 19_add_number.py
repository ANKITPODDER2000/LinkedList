from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def add(l1,l2):
    l1 = l1.head
    l2 = l2.head
    new_ll = LinkedList()
    carry = 0
    while l1 or l2 or carry!=0:
        if l1 and l2:
            s = l1.val+l2.val+carry
            carry = s // 10
            s     = s %  10
            new_ll.insert_end(s)
            l1 = l1.next
            l2 = l2.next
        elif l1:
            s = l1.val+carry
            carry = s // 10
            s = s % 10
            new_ll.insert_end(s)
            l1 = l1.next
        elif l2:
            s = l2.val+carry
            carry = s // 10
            s = s % 10
            new_ll.insert_end(s)
            l2 = l2.next
        else:
            new_ll.insert_end(carry)
            carry = 0
    return new_ll
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    l2 = LinkedList()
    CreateLinkedList(l2)
    result = add(l1,l2)
    result.display()
    

if __name__ == "__main__":
    main()
