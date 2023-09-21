class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.rear = self.front = None
    def Enqueue(self,data):
        temp = Node(data)
        if self.rear is None:
            self.rear = self.front = temp
        self.rear.next = temp
        self.rear = temp
    def isEmpty(self):
        return self.front == None
    def Dequeue(self):
        temp = self.front
        if self.isEmpty():
            return
        self.front = temp.next
        if self.front is None:
            self.rear = None
        

q = Queue()
q.Enqueue(20)
q.Enqueue(10)
q.Enqueue(30)
print("rear",q.rear.data)
q.Dequeue()
q.Dequeue()
q.Dequeue()
print("front",q.front.data)