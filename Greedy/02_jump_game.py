class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False





if __name__ == "__main__":

    obj = Solution()

    nums1 = [2,3,1,1,4]
    print(obj.canJump(nums = nums1))

    nums2 = [3,2,1,0,4]
    print(obj.canJump(nums = nums2))
