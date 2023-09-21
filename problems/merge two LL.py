class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head =  None
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current =  current.next
            current.next = new_node
    def mergeLinkedList(self,l1,l2):
        dummy = Node(0)
        current =  dummy
        while l1 and l2:
            if  l1.data <= l2.data:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 =  l2.next
            current = current.next
        if l1:
            current.next =  l1
        else:
            current.next = l2
        return dummy.next
    def display(self):
        if self.head is None:
            print("empty")
        else:
            current =  self.head
            while current:
                print(current.data,end="-->")
                current =  current.next
        print("None")

l1 = LinkedList()
l2 = LinkedList()
merged_list= LinkedList()
arr1 = [1,1,2,3,4]
arr2= [2,3,5,6]
for i in arr1:
    l1.append(i)
for i in arr2:
    l2.append(i)
l1.display()
print()
l2.display()
print()
output =  merged_list.mergeLinkedList(l1.head,l2.head)
merged_list.head =  output
merged_list.display()