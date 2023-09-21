# class Node:
#     def __init__(self,data):
#         self.data =  data
#         self.next = None
        
# class Queue:
#     def __init__(self):
#         self.rear = self.front = None
#     def Enqueue(self,data):
#         temp = Node(data)
#         if self.rear is None:
#             self.rear = self.front = temp
#         self.rear.next = temp
#         self.rear = temp
#     def isEmpty(self):
#         return self.front == None
#     def Dequeue(self):
#         temp = self.front
#         if self.isEmpty():
#             return
#         temp = self.front
#         self.front = temp.next
#         if self.front == None:
#             self.rear = None
            
# q = Queue()
# q.Enqueue(10)
# q.Enqueue(20)
# q.Enqueue(30)

# print(q.rear.data)
# q.Dequeue()
# q.Dequeue()
# q.Dequeue()
# print(str(q.front.data if q.front != None else -1) )


# linked list adding values at end

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def append(self,data):
#         new_data = Node(data)
#         if self.head is None:
#             self.head = new_data
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_data
#     def printdata(self):
#         current = self.head 
#         while current:
#             print(current.data)
#             current = current.next
            
# l=LinkedList()
# l.append(10)
# l.append(20)
# l.append(30)
# l.printdata()


# add value in begginnig

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def beginning(self,data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data,end = "->")
#             current = current.next
# l=LinkedList()
# l.beginning(10)
# l.beginning(20)
# l.beginning(30)
# l.display()



# bubble sort

def bubble_sort(arr):
    for i in range(len(arr)):
        n=len(arr)
        for j in range(0,n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)
arr = [9,4,64,3,23,3]
bubble_sort(arr)
    