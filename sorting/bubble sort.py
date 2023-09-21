def bubble(arr):
    n=len(arr)
    for i in range(len(arr)):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    for i in range(len(arr)):
        print(arr[i],end =" ")

arr = [23,4,64,5,76,2,1]
bubble(arr)