class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(row, col, visit, prevHeight):
            if ((row, col) in visit or
                row < 0 or col < 0 or
                row == rows or col == cols or
                heights[row][col] < prevHeight):
                return
            
            visit.add((row, col))
            dfs(row = row + 1, col = col, visit = visit, prevHeight = heights[row][col])
            dfs(row = row - 1, col = col, visit = visit, prevHeight = heights[row][col])
            dfs(row = row, col = col + 1, visit = visit, prevHeight = heights[row][col])
            dfs(row = row, col = col - 1, visit = visit, prevHeight = heights[row][col])

        for col in range(cols):
            dfs(row = 0, col = col, visit = pac, prevHeight = heights[0][col])
            dfs(row = rows - 1, col = col, visit = atl, prevHeight = heights[rows - 1][col])
        
        for row in range(rows):
            dfs(row = row, col = 0, visit = pac, prevHeight = heights[row][0])
            dfs(row = row, col = cols - 1, visit = atl, prevHeight = heights[row][cols - 1])

        # res = []
        # for row in range(rows):
        #     for col in range(cols):
        #         if (row, col) in pac and (row, col) in atl:
        #             res.append([row, col])
        
        return list(pac.intersection(atl))




if __name__ == "__main__":

    obj = Solution()
    
    heights1 = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
    print(obj.pacificAtlantic(heights = heights1))
    
    heights2 = [
        [1]
    ]
    print(obj.pacificAtlantic(heights = heights2))
