from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
class LinkedListMod(LinkedList):
    def remove_allnode(self):
        while self.head:
            temp = self.head
            self.head = self.head.next
            del temp
def main():
    l1 = LinkedListMod()
    CreateLinkedList(l1)
    l1.display()
    print("Remove the Linked List.....")
    l1.remove_allnode()
    l1.display()
if __name__ == "__main__":
    main()