# original = {'a':1,'b':2,'c':3}
# swapped = {value:key for key,value in original.items()}
# print(swapped,end=" ")


original = {'apple':1,"banana":2}
# swapped = {value:key for key,value in original.items()}
# print(swapped)

val = {}

for key,value in original.items():
    val[value] = key

print(val)