# A = [23,12,43,10,6,34]

# for i in range(len(A)):
#     min_index = i
#     for j in range(i+1,len(A)):
#         if A[min_index] > A[j]:
#             min_index = j 
#     A[i],A[min_index] = A[min_index],A[i]

# for i in range(len(A)):
#     print(A[i],end=" ")

def selection_sort(arr):
	for i in range(len(arr)):
		min_index = i
	for j in range(i+1,len(arr)):
		if arr[min_index] > arr[j]:
			min_index = j
	arr[i],arr[min_index] = arr[min_index],arr[i]




arr=[23,12,43,10,6,34]
selection_sort(arr)
print(arr)