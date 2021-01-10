class Node:
    def __init__(self , val = 0 , next = None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_end(self , val = 0):
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
        print()
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
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    def get_tail(self):
        temp = self.head
        if not temp:
            return None
        while temp.next:
            temp = temp.next
        return temp
    def getIndex(self , k):
        count = 0
        temp = self.head
        if k < 0:
            return None
        while count < k and temp:
            temp = temp.next
            count += 1
        if count != k:
            return None
        if not temp:
            return None
        return temp
    def insert_beg(self , val=0):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node