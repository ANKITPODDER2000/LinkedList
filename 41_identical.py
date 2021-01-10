from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def isIdentical(head1,head2):
    while head1 and head2:
        if head1.val != head2.val:
            return False
        head1 = head1.next
        head2 = head2.next
    if not head1 and not head2:
        return True
    return False
def main():
    l1 = LinkedList()
    l2 = LinkedList()
    CreateLinkedList(l1)
    CreateLinkedList(l2)
    print("Is identical : ",isIdentical(l1.head , l2.head))
if __name__ == "__main__":
    main()