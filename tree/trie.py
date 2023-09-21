class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfword = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        current = self.root 
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.endOfword = True
    def search(self,word):
        current = self.root
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.endOfword
    def startsWith(self,prefix):
        current = self.root
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
            return True
t = Trie()
t.insert('apple')
t.insert('pineapple')
c = t.search('apple')
print(c)
s = t.startsWith("zebra")
print(s)