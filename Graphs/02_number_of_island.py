import collections

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(row, col):
            q = collections.deque()
            visit.add((row, col))
            q.append((row, col))

            while q:
                row, col = q.popleft()
                directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

                for dirRow, dirCol in directions:
                    r, c = row + dirRow, col + dirCol
                    if ((r) in range(rows) and
                        (c) in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visit:
                    bfs(row=row, col=col)
                    islands += 1

        return islands






if __name__ == "__main__":

    obj = Solution()
    
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(obj.numIslands(grid=grid1))

    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(obj.numIslands(grid=grid2))

    grid3 = [
        ["1","1","1"],
        ["0","1","0"],
        ["1","1","1"]
    ]
    print(obj.numIslands(grid=grid3))

