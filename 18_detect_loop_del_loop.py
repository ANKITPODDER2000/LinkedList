from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList

class LinkedListMod(LinkedList):
    def display(self , len):
        if not self.head:
            print("Linked list is empty!")
            return
        temp = self.head
        print("Linked list is : ", end="")
        count  = 0
        while temp and count < len+2:
            print(str(temp.val)+"->", end="")
            temp = temp.next
            count += 1
        if temp:
            print(" ............")
        print("None")

def detect_remove_loop(head):
    slow = head
    fast = head.next
    while slow and fast and slow != fast:
        if not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    if not slow or not fast:
        return False
    temp1 = head
    temp2 = fast
    while temp1 and temp2:
        while temp2!=temp1 and temp2.next!=fast:
            temp2 = temp2.next
        if temp1==temp2:
            break
        temp1 = temp1.next
        temp2 = fast
    while temp2.next != temp1:
        temp2 = temp2.next
    temp2.next = None
    return True
    
def main():
    l1 = LinkedListMod()
    CreateLinkedList(l1)
    l = l1.length()
    n = int(input("Enter the pos of loop : "))
    if l1.getIndex(n):
        tail = l1.get_tail()
        tail.next = l1.getIndex(n)
    l1.display(l)
    detect = detect_remove_loop(l1.head)
    print("Is their any loop : ",detect)
    l1.display(10)
if __name__ == "__main__":
    main()
