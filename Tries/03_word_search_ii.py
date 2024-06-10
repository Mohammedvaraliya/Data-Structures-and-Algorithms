class TrieNode:

    def __init__(self) -> None:
        self.children = {}
        self.endOfWord= False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.refs += 1
        
        cur.endOfWord = True
    
    def removeWord(self, word):
        cur = self
        cur.refs -= 1

        for c in word:
            if c in cur.children:
                cur = cur.children[c]
                cur.refs -= 1

class Solution:

    def __init__(self) -> None:
        self.root = TrieNode()

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = self.root

        for w in words:
            root.addWord(w)
        
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(row, col, node, word):
            if (
                row not in range(rows) 
                or col not in range(cols)
                or board[row][col] not in node.children
                or node.children[board[row][col]].refs < 1
                or (row, col) in visit
            ):
                return
            
            visit.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]

            if node.endOfWord:
                node.endOfWord = False
                res.add(word)
                root.removeWord(word)
            
            dfs(row = row - 1, col = col, node = node, word = word)
            dfs(row = row + 1, col = col, node = node, word = word)
            dfs(row = row, col = col - 1, node = node, word = word)
            dfs(row = row, col = col + 1, node = node, word = word)

            visit.remove((row, col))
        
        for row in range(rows):
            for col in range(cols):
                dfs(row = row, col = col, node = root, word = "")

        return list(res)







if __name__ == "__main__":

    obj = Solution()

    board1 = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words1 = ["oath","pea","eat","rain"]
    res1 = obj.findWords(board=board1, words=words1)
    print(res1)

    board2 = [["a","b"],["c","d"]]
    word2 = ["abcb"]
    res2 = obj.findWords(board=board2, words=word2)
    print(res2)
