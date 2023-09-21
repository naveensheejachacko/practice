class Node:
    def __init__(self,data):
        self.prev = None
        self.next = None
        self.data = data
class doubleLL:
    def __init__(self):
        self.head = None
    def append(self,data):
        if self.head is None:
            new_node = Node(data)
        else:
            current = self.head
            while current:
                current = current.next
            new_node = Node(data)
            current.next = new_node
            current.next.prev = current
    def display(self):
        current = self.head
        while current:
            print(current.data,end="->")