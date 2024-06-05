class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()

        def dfs(row, col, i):
            if i == len(word):
                return True
            if (row < 0 or col < 0 or
                row >= rows or col >= cols or
                word[i] != board[row][col] or
                (row, col) in path):
                return False
            
            path.add((row, col))
            res = (dfs(row = row + 1, col = col, i = i + 1) or
                   dfs(row = row - 1, col = col, i = i + 1) or
                   dfs(row = row, col = col + 1, i = i + 1) or
                   dfs(row = row, col = col - 1, i = i + 1))
            path.remove((row, col))
            return res
        
        for row in range(rows):
            for col in range(cols):
                if dfs(row=row, col=col, i=0): return True

        return False




"""
Time complexity O(n * m * dfs())
n and m are the dimensions of our problem (rows and cols)
and the time complexity of dfs is 4^len(word) because we are calling 4 diff times in the function itself

so the final time complexity of this problem is O(n * m * 4^n)
"""


if __name__ == "__main__":

    obj = Solution()

    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word1 = "ABCCED"
    res1 = obj.exist(board=board1, word=word1)
    print(res1)

    board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word2 = "SEE"
    res2 = obj.exist(board=board2, word=word2)
    print(res2)

    board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word3 = "ABCB"
    res3 = obj.exist(board=board3, word=word3)
    print(res3)

