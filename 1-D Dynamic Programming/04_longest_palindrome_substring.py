class Solution:
    def checkPalindrome(self, left: int, right: int, s: str) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        resString = ""
        
        for i in range(len(s)):
            # Odd length palindrome
            palindrome1 = self.checkPalindrome(i, i, s)
            if len(palindrome1) > len(resString):
                resString = palindrome1
            
            # Even length palindrome
            palindrome2 = self.checkPalindrome(i, i + 1, s)
            if len(palindrome2) > len(resString):
                resString = palindrome2
        
        return resString


if __name__ == "__main__":
    obj = Solution()

    s1 = "babad"
    print(obj.longestPalindrome(s = s1))

    s2 = "cbbd"
    print(obj.longestPalindrome(s = s2))
