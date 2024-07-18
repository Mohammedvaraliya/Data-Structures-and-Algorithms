class Solution:
    def rob(self, nums: list[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = newRob
        
        return rob2





if __name__ == "__main__":

    obj = Solution()

    nums1 = [1,2,3,1]
    print(obj.rob(nums = nums1))

    nums2 = [2,7,9,3,1]
    print(obj.rob(nums = nums2))