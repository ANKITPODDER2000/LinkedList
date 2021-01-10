from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def insert(head1 , head2 , k):
    c = 1
    while head1 and c<=k-1:
        head1 = head1.next
        c += 1
    if not head1:
        return
    temp = head1.next
    last_node = None
    while head2:
        last_node = head1
        head1.next = head2
        head1 = head1.next
        head2 = head2.next
    while temp:
        last_node.next = temp
        temp = temp.next
        last_node = last_node.next
        
def main():
    l1 = LinkedList()
    l2 = LinkedList()
    CreateLinkedList(l1)
    CreateLinkedList(l2)
    k = int(input("Enter the value of k : "))
    insert(l1.head , l2.head , k)
    l1.display()
if __name__ == "__main__":
    main()
