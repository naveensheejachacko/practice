class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def Middle(self):
        fast = slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("the middle is" , slow.data)

l = LinkedList()
for i in range(0,5,1):
    l.push(i)
l.Middle()