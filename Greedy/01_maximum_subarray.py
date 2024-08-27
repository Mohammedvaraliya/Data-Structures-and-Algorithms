class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSub = nums[0]
        curSub = 0

        for n in nums:
            if curSub < 0:
                curSub = 0
            curSub += n
            maxSub = max(maxSub, curSub)
        
        return maxSub




if __name__ == "__main__":

    obj = Solution()

    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    print(obj.maxSubArray(nums = nums1))

    nums2 = [1]
    print(obj.maxSubArray(nums = nums2))

    nums3 = [5,4,-1,7,8]
    print(obj.maxSubArray(nums = nums3))
