class Solution:
   def twoSum(self, numbers: list[int], target: int) -> list[int]:
      l, r = 0, len(numbers) - 1

      while l < r:
         curSum = numbers[l] + numbers[r]

         if curSum > target:
               r -= 1
         elif curSum < target:
               l += 1
         else:
               return [l + 1, r + 1]
      return []
    
   
if __name__ == "__main__":
    
   obj = Solution()
   X = [2,7,11,15]
   Y = [2,3,4]
   Z = [-1,0]

   print(obj.twoSum(X, 9))
   print(obj.twoSum(Y, 6))
   print(obj.twoSum(Z, -1))