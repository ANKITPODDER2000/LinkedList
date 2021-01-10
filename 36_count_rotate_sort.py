from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def count_rotate(head):
    count = 0
    while head.next and head.val < head.next.val:
        count += 1
        head = head.next
    count += 1
    return count
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    count = count_rotate(l1.head)
    print("Count = ",count)
if __name__ == "__main__":
    main()