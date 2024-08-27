class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]




if __name__ == "__main__":
    
    obj = Solution()

    text1_1 = "abcde"
    text2_1 = "ace" 
    print(obj.longestCommonSubsequence(text1 = text1_1, text2 = text2_1))

    text1_2 = "abc"
    text2_2 = "abc" 
    print(obj.longestCommonSubsequence(text1 = text1_2, text2 = text2_2))

    text1_3 = "abc"
    text2_3 = "def" 
    print(obj.longestCommonSubsequence(text1 = text1_3, text2 = text2_3))


