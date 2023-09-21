from functools import reduce
arr = [1,2,3,4,5]
def squared(x,y):
    return x*y
    
result = reduce(squared,arr)
print(result)