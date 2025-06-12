class Solution:
    # Time Complexity : O(n^2)
    # Space Complexity : O(1)
    def twoSum_brute_force(self, nums: list[int], target: int) -> list[int]:
        
        for i in range(len(nums) - 1):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
        return [0, 0]

    # Time Complexity : O(n)
    # Space Complexity : O(n)
    def twoSum_hash_table(self, nums: list[int], target: int) -> list[int]:
        ht = dict()

        for i in range(len(nums)):
            if nums[i] in ht:
                return [ht[nums[i]], i]
            else:
                ht[target - nums[i]] = i

        return [0, 0]

    # Time Complexity : O(n)
    # Space Complexity : O(1)
    # Works only if the input list is sorted
    def two_sum_slider(self, nums, target):
        i = 0
        j = len(nums) - 1
        
        while i <= j:
            if nums[i] + nums[j] == target:
                return [i, j]
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                # the case where array[i] + array[j] > target:
                j -= 1

        return [0, 0]







if __name__ == "__main__":

    obj = Solution()

    nums1 = [3,4,5,6]
    target1 = 7
    print(obj.twoSum_brute_force(nums=nums1, target=target1))
    print(obj.twoSum_hash_table(nums=nums1, target=target1))
    print(obj.two_sum_slider(nums=nums1, target=target1), "\n")

    nums2 = [4,5,6]
    target2 = 10
    print(obj.twoSum_brute_force(nums=nums2, target=target2))
    print(obj.twoSum_hash_table(nums=nums2, target=target2))
    print(obj.two_sum_slider(nums=nums2, target=target2), "\n")

    nums3 = [5,5]
    target3 = 10
    print(obj.twoSum_brute_force(nums=nums3, target=target3))
    print(obj.twoSum_hash_table(nums=nums3, target=target3))
    print(obj.two_sum_slider(nums=nums3, target=target3), "\n")

    nums4 = [-2, 1, 2, 4, 7, 11]
    target4 = 13
    print(obj.twoSum_brute_force(nums=nums4, target=target4))
    print(obj.twoSum_hash_table(nums=nums4, target=target4))
    print(obj.two_sum_slider(nums=nums4, target=target4))

