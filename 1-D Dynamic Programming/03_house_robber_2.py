class Solution:

    def rob(self, nums: list[int]) -> int:
        return max(nums[0], self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))

    def rob_helper(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        
        return rob2





if __name__ == "__main__":

    obj = Solution()

    nums1 = [2,3,2]
    print(obj.rob(nums = nums1))

    nums2 = [1,2,3,1]
    print(obj.rob(nums = nums2))

    nums3 = [1,2,3]
    print(obj.rob(nums = nums3))