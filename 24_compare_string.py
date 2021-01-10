from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def compare(head1 , head2):
    while head1 and head2:
        if head1.val == head2.val:
            head1 = head1.next
            head2 = head2.next
        elif head1.val > head2.val:
            return  1
        else:
            return -1
    if not head1 and not head2:
        return 0
    elif head1:
        return 1
    return -1
def main():
    l1 = LinkedList()
    CreateLinkedList(l1 , func=str)
    l2 = LinkedList()
    CreateLinkedList(l2 , func=str)
    print("Ans of comparision is = %d"%compare(l1.head , l2.head))
if __name__ == "__main__":
    main()
