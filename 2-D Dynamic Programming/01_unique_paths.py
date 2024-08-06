class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]

            row = newRow
        
        return row[0]




if __name__ == "__main__":
    obj = Solution()

    m1 = 3
    n1 = 7
    print(obj.uniquePaths(m = m1, n = n1))

    m2 = 3
    n2 = 2
    print(obj.uniquePaths(m = m2, n = n2))
