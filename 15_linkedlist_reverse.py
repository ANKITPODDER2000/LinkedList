from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def reverse_list(head):
    if not head:
        return
    reverse_list(head.next)
    print(head.val,end=" ")
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    if l1.head:
        print("Rev of linked list : ",end="")
        reverse_list(l1.head)
if __name__ == "__main__":
    main()