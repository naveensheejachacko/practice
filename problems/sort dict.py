my_dict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

myKeys = list(my_dict.keys())

myKeys.sort()

sorted_dict = {i: my_dict[i] for i in myKeys}

print(sorted_dict)
