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
                current=current.next
            current.next = new_node
    def delete(self,value):
        current =  self.head
        if current and current.data == value:
            self.head = current.next
            current = None
            return
        prev = None
        while current is not None:
            if current.data == value:
                break
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None
    def display(self):
        current =  self.head
        while current:
            print(current.data,end = ' ')
            current=current.next
        print()
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.delete(10)
my_list.display()