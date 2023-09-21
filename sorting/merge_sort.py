def merged_sort(arr):
    if len(arr) <= 1:
        return arr
    mid =  len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merged_sort(left_half)
    right_half = merged_sort(right_half)
    return merge(left_half,right_half)

def merge(left,right):
    merged = []
    right_index,left_index = 0,0
    while left_index < len(left) and right_index <len(right):
        if left[left_index] <= right[left_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

arr = [9,8,7,6,5]
sorted_arr = merged_sort(arr)
print(sorted_arr)