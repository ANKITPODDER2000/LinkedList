from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def get_ans(head , k):
    ans = None
    c = 1
    while head:
        if c % k == 0:
            ans = head
        head = head.next
        c += 1
    return ans.val
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    k = int(input("Enter the value of k : "))
    ans = get_ans(l1.head , k)
    print("Ans : ",ans)
if __name__ == "__main__":
    main()