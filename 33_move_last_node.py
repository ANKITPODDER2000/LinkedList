from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def move_tail(head):
    if not head or not head.next:
        return head
    temp_head = head
    while head.next.next:
        head = head.next
    temp_node= head.next
    head.next = None
    temp_node.next = temp_head
    return temp_node
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    l1.display()
    l1.head = move_tail(l1.head)
    l1.display()
if __name__ == "__main__":
    main()


