from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def rev(s):
    STR = ""
    for i in range(len(s)-1 , -1 , -1):
        STR += s[i]
    return STR
def reverse_list(head):
    while head:
        head.val = rev(head.val)
        head = head.next
def main():
    l1 = LinkedList()
    CreateLinkedList(l1 , func=str)
    l1.display()
    reverse_list(l1.head)
    l1.display()
if __name__ == "__main__":
    main()
