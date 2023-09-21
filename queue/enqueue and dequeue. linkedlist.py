class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = self.rear = None
    def Enqueue(self,data):
        temp=Node(data)
        if self.rear is None:
            self.rear = self.front = temp
        self.rear.next =  temp
        self.rear = temp

    def isEmpty(self):
        return self.front == None
    def Dequeue(self):
        if self.isEmpty():
            return
        temp=self.front
        self.front = temp.next
        if self.front == None:
            self.rear = None
q = Queue()
q.Enqueue(10)
q.Enqueue(20)
q.Enqueue(30)
print("front",q.front.data,end=" ")
print("rear",q.rear.data,end=" ")
q.Dequeue()
# q.Dequeue()
# q.Dequeue()
print("\n queue front :"+ str(q.front.data if q.front != None else -1))
