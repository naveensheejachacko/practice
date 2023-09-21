class Node:
    def __init__(self,data):
        self.data = data
        self.next =  None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node =  Node(data)
        current = self.head
        if self.head is None:
            self.head = new_node
        else:
            while current.next:
                current = current.next
            current.next = new_node
    def duplicate(self):
        current = self.head
        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data,end = " ")
            current = current.next
        print()

my_list = LinkedList()
my_list.append(10)
my_list.append(10)
my_list.append(20)
my_list.append(20)
my_list.append(30)
my_list.duplicate()
my_list.display()