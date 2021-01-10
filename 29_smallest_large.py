from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def find_max_min(head):
    if not head:
        return None , None
    MAX = MIN = head.val
    while head:
        if head.val>MAX:
            MAX = head.val
        elif head.val < MIN:
            MIN = head.val
        head = head.next
    return MAX , MIN
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    MAX , MIN = find_max_min(l1.head)
    print("MAX = ",MAX)
    print("MIN = ",MIN)
if __name__ == "__main__":
    main()