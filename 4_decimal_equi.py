from LinkedList import LinkedList
class ModList(LinkedList):
    def binary_equ(self):
        l = self.length() - 1
        temp = self.head
        ans = 0
        while temp:
            ans += ((2**l) * temp.val)
            temp = temp.next
            l -= 1
        return ans

def main():
    print("Enter the number : ",end="")
    num = [int(x) for x in input().split(" ")]
    l1 = ModList()
    for i in num:
        l1.inset_end(i)
    print("Binary equivalent is : ",l1.binary_equ())
    
if __name__ == "__main__":
    main()
