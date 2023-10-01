class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, product):
        node = self.root
        for char in product:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.suggestions.append(product)
            node.suggestions.sort()  # Sort the suggestions lexicographically
            if len(node.suggestions) > 3:
                node.suggestions.pop()
                
    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.suggestions

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for product in products:
            trie.insert(product)
        result = []
        prefix = ""
        
        for char in searchWord:
            prefix += char
            suggestions = trie.search(prefix)
            result.append(suggestions)
            
            if not suggestions:  # If there are no suggestions, stop inserting further characters
                while len(searchWord) - len(prefix) > 0:
                    result.append([])
                    prefix += searchWord[len(prefix)]
                break
                
        return result