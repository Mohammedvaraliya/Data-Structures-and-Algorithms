class TrieNode:

    def __init__(self) -> None:
        self.children = {}
        self.endOfWord= False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return cur.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
            
        return True



        

if __name__ == "__main__":

    obj = Trie()
    word1 = 'apple'
    obj.insert(word1)
    print(obj.search(word1)) # True
    word2 = 'app'
    print(obj.search(word2)) # False because the word "app" is not present in the Trie object
    prefix = 'app'
    print(obj.startsWith(prefix)) # True because the previously inserted string `word` has the prefix `prefix` 
    obj.insert(word2)
    print(obj.search(word2)) # True because the word "app" has been inserted in the Trie object
