class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None
    def creat(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")
l1= Linked_list()
l1.creat(20)
l1.creat(30)
l1.creat(40)
l1.creat(50)
l1.display()

        
        