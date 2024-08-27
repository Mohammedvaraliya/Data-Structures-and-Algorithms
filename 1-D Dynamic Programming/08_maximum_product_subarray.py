class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            
            tmp = n * curMax
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        
        return res



if __name__ == "__main__":
    
    obj = Solution()

    nums1 = [2,3,-2,4]
    print(obj.maxProduct(nums = nums1))

    nums2 = [-2,0,-1]
    print(obj.maxProduct(nums = nums2))
