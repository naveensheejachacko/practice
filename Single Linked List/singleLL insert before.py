class Node:
    def __init__(self,data):
        self.data =  data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:      
            current =  self.head
            while current.next:
                current = current.next
            current.next =  new_node
    def insert_before(self,value,new_data):
        new_node =  Node(new_data)
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev is None:
                    self.head = new_node
                else:
                    prev.next = new_node
                new_node.next = current
                break
            prev = current
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
my_list.insert_before(30, 27)
my_list.display()
