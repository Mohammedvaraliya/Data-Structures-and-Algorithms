class Solution:
   def is_palindrome(self, num: int) -> bool:
      original = num
      reversed_num = 0

      while num > 0:
         digit = num % 10
         reversed_num = reversed_num * 10 + digit
         num //= 10
      return original == reversed_num

   def nextPalindromeNumber(self, num: int) -> int:
      num += 1
      while not self.is_palindrome(num):
         num += 1
      return num



if __name__ == "__main__":

   obj = Solution()

   print(obj.nextPalindromeNumber(123))
   print(obj.nextPalindromeNumber(121))
   print(obj.nextPalindromeNumber(1221))
   print(obj.nextPalindromeNumber(999))
     
    