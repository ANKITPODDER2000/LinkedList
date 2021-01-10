from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def sort(head):
    arr = [0] * 3
    temp = head
    while temp:
        arr[temp.val] += 1
        temp = temp.next
    temp = head
    for i in range(3):
        while arr[i]>0:
            temp.val = i
            temp = temp.next
            arr[i] -= 1
    
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    l1.display()
    sort(l1.head)
    l1.display()
if __name__ == "__main__":
    main()