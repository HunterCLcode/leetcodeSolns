class TreeNode:
    def __init__(self):
        self.hmap = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.hmap: cur.hmap[c] = TreeNode()
            cur = cur.hmap[c]
        cur.end = True

    def search(self, word: str) -> bool:
        
        def DFS(node, word):
            if word == "": return node.end
            
            char = word[0]
            
            if char != '.': return char in node.hmap and DFS(node.hmap[char], word[1:])

            for n in node.hmap:
                 if DFS(node.hmap[n], word[1:]): return True
            return False
                
            
        return DFS(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
