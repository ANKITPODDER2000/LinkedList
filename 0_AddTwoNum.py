# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getNumber(self,l):
        num = 0
        i = 0
        temp = l
        while temp:
            num = num + ((10**i)*temp.val)
            temp = temp.next
            i+=1
        return num
    def addTwoNumbers(self, l1 , l2):
        num1 = self.getNumber(l1)
        num2 = self.getNumber(l2)
        add = num1+num2
        l = ListNode(add%10)
        temp = l
        add = add // 10
        while add!=0:
            l.next = ListNode(add%10)
            l = l.next
            add = add // 10
        return temp
        

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
###############
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l = Solution().addTwoNumbers(l1,l2)
while l:
    print(l.val)
    l = l.next
        