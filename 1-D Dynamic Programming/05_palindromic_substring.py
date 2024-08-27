class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        for i in range(len(s)):
            # Odd length palindrome
            res += self.countPalindrome(i, i, s)
            
            # Even length palindrome
            res += self.countPalindrome(i, i + 1, s)
        
        return res
    
    def countPalindrome(self, left: int, right: int, s: str) -> str:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        
        return count


if __name__ == "__main__":
    
    obj = Solution()

    s1 = "abc"
    print(obj.countSubstrings(s = s1))

    s2 = "aaa"
    print(obj.countSubstrings(s = s2))
