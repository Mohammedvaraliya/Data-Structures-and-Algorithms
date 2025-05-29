class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            
            dp[i] = 1 + dp[i - offset]
        
        return dp





if __name__ == "__main__":

    obj = Solution()

    n1 = 2
    print(obj.countBits(n=n1))

    n2 = 5
    print(obj.countBits(n=n2))