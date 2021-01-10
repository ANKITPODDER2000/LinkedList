from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def getNth(head, k):
    count = 0
    temp = head
    while count < k-1 and temp:
        temp = temp.next
        count += 1
    if not temp:
        return -1
    return temp.val

def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    print("Item : ", getNth(l1.head, int(input("Enter the index : "))))
    return 0
if __name__ == "__main__":
    main()
