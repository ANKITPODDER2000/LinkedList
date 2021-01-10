from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def find_middle(L):
    LEN = L.length()
    if LEN % 2 != 0:
        LEN = LEN - 1
    pos = LEN // 2
    head = L.head
    for _ in range(pos):
        head = head.next
    return head

def find_middle_method2(head):
    count = 0
    node  = head 
    while head:
        if (count & 1) == 1:
            node = node.next
        count += 1
        head = head.next
    return node

def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    node = find_middle(l1)
    print("Value of middle node is : ",node.val)
    node = find_middle_method2(l1.head)
    print("Value of middle node is : ", node.val)
if __name__ == "__main__":
    main()
