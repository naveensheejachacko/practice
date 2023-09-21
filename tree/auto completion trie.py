class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class AutocompleteTrie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._get_words_with_prefix(node, prefix)
    def _get_words_with_prefix(self, node, prefix):
        results = []
        if node.is_end_of_word:
            results.append(prefix)
        for char, child in node.children.items():
            results.extend(self._get_words_with_prefix(child, prefix + char))
        return results

# Example usage
trie = AutocompleteTrie()
words = ["apple", "appetite", "banana", "bat", "ball", "cat", "dog"]

for word in words:
    trie.insert(word)

prefix = "c"
autocomplete_words = trie.search(prefix)
print(f"Autocomplete suggestions for '{prefix}': {autocomplete_words}")
