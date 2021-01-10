from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def getString(head):
    Str = ""
    while head:
        Str += head.val
        head = head.next
    return Str
def isPalindrome(head):
    Str = getString(head)
    # print(str)
    l   = len(Str)
    i   = 0
    while i < (l // 2):
        if Str[i] != Str[l-i-1]:
            return False
        i+=1
    return True
def main():
    l1 = LinkedList()
    CreateLinkedList(l1,func=str)
    l1.display()
    print("is linkedlist form a palindrome : ",isPalindrome(l1.head))
if __name__ == "__main__":
    main()