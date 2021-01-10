from LinkedList import LinkedList
class linkedlistmod(LinkedList):
    def delete(self,val):
        if not self.head:
            return False
        elif self.head.val == val:
            temp = self.head
            self.head = self.head.next
            del temp
            self.delete(val)
        else:
            prev = self.head
            next = self.head.next
            while next:
                if next.val == val:
                    prev.next = next.next
                    temp = next
                    del temp
                    next = prev.next
                else:
                    prev = next
                    next = next.next
def main():
    l1 = linkedlistmod()
    l1.insert_end(1)
    l1.insert_end(1)
    l1.insert_end(1)
    l1.insert_end(1)
    l1.insert_end(1)
    l1.insert_end(2)
    l1.insert_end(3)
    l1.insert_end(5)
    l1.insert_end(1)
    l1.insert_end(1)
    l1.insert_end(1)
    l1.display()
    l1.delete(1)
    l1.display()

if __name__ == "__main__":
    main()
