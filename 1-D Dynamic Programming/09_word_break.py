class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]



if __name__ == "__main__":
    
    obj = Solution()

    s1 = "leetcode"
    wordDict1 = ["leet","code"]
    print(obj.wordBreak(s = s1, wordDict = wordDict1))

    s2 = "applepenapple"
    wordDict2 = ["apple","pen"]
    print(obj.wordBreak(s = s2, wordDict = wordDict2))

    s3 = "catsandog"
    wordDict3 = ["cats","dog","sand","and","cat"]
    print(obj.wordBreak(s = s3, wordDict = wordDict3))
