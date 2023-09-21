def heapify(arr,n,i):
    smallest = i
    l = 2*i+1
    r = 2*i+2
    if l<n and arr[i] >arr[l]:
        smallest = l
    if r<n and arr[i]>arr[r]:
        smallest = r
    if smallest != i:
        arr[i],arr[smallest] = arr[smallest],arr[i]
        heapify(arr,n,smallest)
def insert(array,newnum):
    size = len(array)
    if size == 0:
        array.append(newnum)
    else:
        array.append(newnum)
        for i in range((size//2)-1,-1,-1):
            heapify(array,size,i)
            
def deleteNode(array,num):
    size= len(array)
    for i in range(0,size):
        if num == array[i]:
            break
    array[i],array[size-1] = array[size-1],array[i]
    array.remove(num)
    for i in range((size//2)-1,-1,-1):
        heapify(array,len(array),i)

arr =[]
insert(arr,3)
insert(arr,5)
insert(arr,10)
insert(arr,15)
insert(arr,1)
insert(arr,23)
insert(arr,19)
print("min heap :",str(arr))
deleteNode(arr,15)
print("min heap :",str(arr))
