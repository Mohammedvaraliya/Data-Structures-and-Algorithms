class TrieNode:

    def __init__(self) -> None:
        self.children = {}
        self.endOfWord= False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.endOfWord = True

    def search(self, word: str) -> bool:

        def dfs(j: int, root: None) -> bool:
            cur = root

            for i in range(j, len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    
                    return False

                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
                
            return cur.endOfWord
        
        return dfs(j=0, root=self.root)


        

if __name__ == "__main__":

    obj = WordDictionary()
    word1 = 'bad'
    word2 = 'dad'
    word3 = 'mad'
    obj.addWord(word1)
    obj.addWord(word2)
    obj.addWord(word3)
    print(obj.search("pad")) # False because "pad" is not present in the Trie object
    print(obj.search(".ad")) # True because ".ad" matches "bad", "dad", or "mad"
    print(obj.search("b..")) # True because "b.." matches "bad"
