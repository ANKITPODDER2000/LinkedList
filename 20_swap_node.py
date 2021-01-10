from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def swap(head , x , y):
    prev_x = None
    cur_x  = head
    while cur_x and cur_x.val != x:
        prev_x = cur_x
        cur_x = cur_x.next
    if not cur_x:
        print("%d not in Linkedlist."%x)
        return
    
    cur_y = head
    prev_y = None
    while cur_y and cur_y.val != y:
        prev_y = cur_y
        cur_y = cur_y.next
    if not cur_y:
        print("%d not in Linkedlist." % y)
        return
    if not prev_x:
        temp = cur_y.next
        cur_y.next = cur_x.next
        cur_x.next = temp
        prev_y.next = cur_x
        return cur_y
    elif not prev_y:
        temp = cur_y.next
        cur_y.next = cur_x.next
        cur_x.next = temp
        prev_x.next = cur_y
        return cur_x
    else:
        temp = cur_y.next
        cur_y.next = cur_x.next
        prev_y.next = cur_x
        cur_x.next = temp
        prev_x.next = cur_y
        return head
        

def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    x , y = input("Enter the x and y : ").split(" ")
    x , y = int(x) , int(y)
    l1.display()
    l1.head = swap(l1.head , x , y)
    l1.display()
if __name__ == "__main__":
    main()
