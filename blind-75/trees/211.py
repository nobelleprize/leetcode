class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = True

    def search(self, word: str):
        node = self.root
        return self.helper(node, word)

    def helper(self, node, word):
        for i in range(len(word)):
            char = word[i]
            if char not in node.children:
                if char == ".": 
                    for child in node.children:
                        if self.helper(node.children[child], word[i+1:]):
                            return True
                return False
            else:
                node = node.children[char]
        return node.word

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
wD = WordDictionary()

wD.addWord("bad")
wD.addWord("dad")
wD.addWord("mad")
print(wD.search("pad")) # return False
print(wD.search("bad")) # return True
print(wD.search(".ad")) # return True
print(wD.search("b..")) # return True