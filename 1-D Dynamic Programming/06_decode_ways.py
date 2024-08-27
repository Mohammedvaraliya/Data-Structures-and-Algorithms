class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s): 1 }

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            if (i + 1 < len(s) and 
                (s[i] == "1" or
                s[i] == "2" and 
                s[i + 1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            
            return res
        
        return dfs(0)




if __name__ == "__main__":
    
    obj = Solution()

    s1 = "12"
    print(obj.numDecodings(s = s1))

    s2 = "226"
    print(obj.numDecodings(s = s2))

    s3 = "06"
    print(obj.numDecodings(s = s3))
