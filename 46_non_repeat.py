from LinkedList import LinkedList
from LinkedListHelper import CreateLinkedList
def findNumber(head):
    h = {}
    c = 0
    while head:
        if head.val not in h:
            h[head.val] = {} 
            h[head.val]['count'] = 0
            h[head.val]['pos']   = c
        c += 1
        h[head.val]['count'] += 1
        head = head.next
    ans = None
    # print(h)
    for i in h:
        if h[i]['count']==1:
            if ans==None:
                ans = i
            else:
                if h[ans]['pos']>h[i]['pos']:
                    ans = i
    return ans
def main():
    l1 = LinkedList()
    CreateLinkedList(l1)
    print("Number is : ",findNumber(l1.head))
if __name__ == "__main__":
    main()
