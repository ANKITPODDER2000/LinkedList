class Node:
    def __init__(self , val = 0 , next = None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def inset_end(self , val = 0):
        if not self.head:
            self.head = Node(val=val)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(val=val)
    def display(self):
        if not self.head:
            print("Linked list is empty!")
            return
        temp = self.head
        print("Linked list is",end="")
        while temp:
            print(" -> "+str(temp.val),end="")
            temp = temp.next
    def reverse(self):
        temp = self.head
        prev = None
        while temp:
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        self.head = prev
    def get_num(self):
        temp = self.head
        num = 0
        i = 0
        while temp:
            num += ((10**i) * temp.val)
            temp = temp.next
            i+=1
        return num
def main():
    num = input("Enter the number : ")
    l1 = LinkedList()
    for i in num:
        l1.inset_end(int(i))
    l1.reverse()
    num = l1.get_num() + 1
    l2 = LinkedList()
    while num != 0:
        l2.inset_end(num%10)
        num //= 10
    l2.reverse()
    return l2
if __name__ == "__main__":
    l = main()
    l.display()
