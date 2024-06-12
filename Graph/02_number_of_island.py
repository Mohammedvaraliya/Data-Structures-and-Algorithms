import collections

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        island = 0

        def bfs(row, col):
            q = collections.deque()
            visit.add(row, col)
            q.append((row, col))

            while q:
                row, col = q.popleft()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visit:
                    bfs(row=row, col=col)
                    island += 1






if __name__ == "__main__":

    obj = Solution()
