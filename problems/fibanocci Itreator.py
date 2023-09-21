class Fibanocci:
    def __init__(self):
        self.prev = 0
        self.curr = 1
    def __iter__(self):
        return self
    def __next__(self):
        value = self.curr
        self.curr,self.prev = self.curr+self.prev,self.curr
        return value
    
myIter = Fibanocci()
# for i in myIter:
#     if i>10:
#         break
#     print(i)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
