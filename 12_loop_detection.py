from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
class LinkedListMod(LinkedList):
    def detect_loop(self):
        HASH = {}
        temp = self.head
        while temp and temp not in HASH:
            HASH[temp] = True
            temp = temp.next
        return not temp==None
def main():
    l1 = LinkedListMod()
    CreateLinkedList(l1)
    tail = l1.get_tail()
    tail.next = l1.head.next.next
    print("Is their any loop : ",l1.detect_loop())
if __name__ == "__main__":
    main()
