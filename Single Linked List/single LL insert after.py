class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def insert_after(self,pos,new_data):
        new_node = Node(new_data)
        current = self.head
        while current:
            if current.data == pos:
                new_node.next = current.next
                current.next  = new_node
                break
            current = current.next
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
        
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.insert_after(20, 25)
my_list.display()