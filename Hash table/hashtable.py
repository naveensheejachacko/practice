# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.array = [None] * size

#     def _hash(self, key):
#         # Hash function to convert key into array index
#         return hash(key) % self.size

#     def put(self, key, value):
#         index = self._hash(key)
#         self.array[index] = value

#     def get(self, key):
#         index = self._hash(key)
#         return self.array[index]

#     def remove(self, key):
#         index = self._hash(key)
#         self.array[index] = None


# # Create a hash table
# hash_table = HashTable(10)

# # Add key-value pairs
# hash_table.put("apple", 3)
# hash_table.put("banana", 5)
# hash_table.put("orange", 2)

# # Retrieve values
# print(hash_table.get("apple"))  # Output: 3
# print(hash_table.get("banana"))  # Output: 5

# # Remove a key-value pair
# hash_table.remove("orange")

# # Retrieve the removed value
# print(hash_table.get("orange"))  # Output: None


class HashTable:
    def __init__(self, size) -> None:
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_(key)
        for i in self.table[index]:
            if i[0] == key:
                i[1] = value
                return
        self.table[index].append((key, value))

    def get_(self, key):
        index = self.hash_(key)
        for i in self.table[index]:
            if key == i[0]:
                print(i[1])

    def delete(self, key):
        index = self.hash_(key)
        for i in self.table[index]:
            if key == i[0]:
                del self.table[index]


c = HashTable(5)
c.insert("dayon", 22)
c.insert("roshan", 24)
c.insert("akhil", 22)
c.insert("irfan", 22)
c.insert("abin", 26)
print(c.table)
c.get_("abin")
c.delete("dayon")
print(c.table)