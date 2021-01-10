from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def merge(head1 , head2):
    l1 = LinkedList()
    while head1 or head2:
        if not head1:
            l1.insert_end(head2.val)
            head2 = head2.next
        elif not head2:
            l1.insert_end(head1.val)
            head1 = head1.next
        elif head1.val > head2.val:
            l1.insert_end(head2.val)
            head2 = head2.next
        else:
            l1.insert_end(head1.val)
            head1 = head1.next
    return l1
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    l2 = LinkedList()
    CreateLinkedList(l2)
    l3 = merge(l1.head , l2.head)
    l3.display()
    
if __name__ == "__main__":
    main()
