class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) -1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        
        return max(LIS)



if __name__ == "__main__":
    
    obj = Solution()

    nums1 = [10,9,2,5,3,7,101,18]
    print(obj.lengthOfLIS(nums = nums1))

    nums2 = [0,1,0,3,2,3]
    print(obj.lengthOfLIS(nums = nums2))

    nums3 = [7,7,7,7,7,7,7]
    print(obj.lengthOfLIS(nums = nums3))
