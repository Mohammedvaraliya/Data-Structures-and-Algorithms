class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        map = {}

        max_length = start = 0

        for i in range(len(s)):
            if s[i] in map and start <= map[s[i]]:
                start = map[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            map[s[i]] = i
        return max_length


if __name__ == "__main__":

    obj = Solution()

    X = obj.lengthOfLongestSubstring("abcabcbb")
    print(X)

    Y = obj.lengthOfLongestSubstring("bbbbb")
    print(Y)
    
    Z = obj.lengthOfLongestSubstring("pwwkew")
    print(Z)