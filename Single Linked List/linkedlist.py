# singly linked ist construction

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singleLinkedList:
    def __init__(self):
        self.head=None
    def add_node(self,data):
        new_node= Node(data)
        new_node.next=self.head
        self.head=new_node



