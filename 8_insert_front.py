from LinkedList import LinkedList, Node
class linkedListMod(LinkedList):
    def insert_beg(self , val=0):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
def main():
    l1 = linkedListMod()
    l1.insert_beg(5)
    l1.insert_beg(6)
    l1.insert_beg(7)
    l1.insert_end(8)
    l1.display()
    l1.reverse()
    l1.display()
if __name__ == "__main__":
    main()