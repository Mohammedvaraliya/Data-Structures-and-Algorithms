def search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        
        # Left sorted portion
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        # Right sorted portion
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    
    return -1




if __name__ == "__main__":

    nums1 = [4,5,6,7,0,1,2]
    target1 = 0
    print(search(nums=nums1, target=target1))

    nums2 = [4,5,6,7,0,1,2]
    target2 = 3
    print(search(nums=nums2, target=target2))

    nums3 = [1]
    target3 = 0
    print(search(nums=nums3, target=target3))