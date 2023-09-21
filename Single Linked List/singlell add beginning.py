class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data,end=" ")
            current = current.next
        print()
my_list =  LinkedList()
my_list.prepend(10)
my_list.prepend(5)
my_list.prepend(20)
my_list.display()