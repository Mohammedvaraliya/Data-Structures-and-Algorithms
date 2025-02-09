class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        l, r = 0, len(matrix)- 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # Save the top left
                topLeft = matrix[top][l + i]
                
                # Move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move top left into top right
                matrix[top + i][r] = topLeft
            
            r -= 1
            l += 1
        






if __name__ == "__main__":

    obj = Solution()

    matrix1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    obj.rotate(matrix=matrix1)
    print(matrix1)

    matrix2 = [
        [5,1,9,11],
        [2,4,8,10],
        [13,3,6,7],
        [15,14,12,16]
    ]
    obj.rotate(matrix=matrix2)
    print(matrix2)

    matrix3 = [
        [1,2],
        [3,4]
    ]
    obj.rotate(matrix=matrix3)
    print(matrix3)