from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
class LinkedListMod(LinkedList):
    def length_recursive(self , node):
        if not node:
            return 0
        else:
            return 1 + self.length_recursive(node.next)
def main():
    l1 = LinkedListMod()
    print("Length of linked list is = %d"%(l1.length_recursive(l1.head)))
    CreateLinkedList(l1)
    print("Length of linked list is = %d"%(l1.length_recursive(l1.head)))
if __name__ == "__main__":
    main()
