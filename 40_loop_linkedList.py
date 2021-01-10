from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
class modLinkedList(LinkedList):
    def display(self , l):
        temp = self.head
        if not temp:
            print("Linked list is empty ..")
            return
        print("Linkedlist is : ",end="")
        for _ in range(l+4):
            print(temp.val , end="->")
            temp = temp.next
            if not temp:
                print("NULL")
                return
        print("......")
        
def createLoop(head , k):
    node = prev = None
    c = 1
    while head:
        if c == k:
            node = head
        c+=1
        prev = head
        head = head.next
    if not node:
        return
    prev.next = node
def main():
    l1 = modLinkedList()
    CreateLinkedList(l1)
    l = l1.length()
    l1.display(l)
    k = int(input("Enter the value of k : "))
    createLoop(l1.head , k)
    l1.display(l)
if __name__ == "__main__":
    main()