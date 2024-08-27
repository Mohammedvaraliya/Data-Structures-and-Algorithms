class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        pass




if __name__ == "__main__":

    obj = Solution()

    nums1 = [-2,1,-3,4,-1,2,1,-5,4]
    print(obj.maxSubArray(nums = nums1))

    nums2 = [1]
    print(obj.maxSubArray(nums = nums2))

    nums3 = [5,4,-1,7,8]
    print(obj.maxSubArray(nums = nums3))
