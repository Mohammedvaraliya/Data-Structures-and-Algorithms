class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:

        # Time Complexity O(m*n)
        # Space Complexity O(1)
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False

        # Determine which rows/cols need to be zeroed
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # column
                    matrix[0][c] = 0
                    # row
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0





if __name__ == "__main__":

    obj = Solution()

    matrix1 = [
        [1,1,1],
        [1,0,1],
        [1,1,1]
    ]
    obj.setZeroes(matrix=matrix1)
    print(matrix1)

    matrix2 = [
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]
    ]
    obj.setZeroes(matrix=matrix2)
    print(matrix2)
