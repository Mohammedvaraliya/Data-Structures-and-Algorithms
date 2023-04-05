def subarraySum(nums, k: int) -> int:

    sumdict = {0:1}
    n = len(nums)
    count = 0
    s = 0

    for num in nums:
        s += num
        if s - k in sumdict:
            count += sumdict[s - k]
        if s in sumdict:
            sumdict[s] += 1
        else:
            sumdict[s] = 1

    return count


if __name__ == "__main__":

    nums1 = [1, 1, 1]
    nums2 = [1, 2, 3]
    nums3 = [3, 4, 7, 2, -3, 1, 4, 2, 1]

    X = subarraySum(nums1, k=2)
    print(X) # Output: 2

    Y = subarraySum(nums2, k=3)
    print(Y) # Output: 2

    Z = subarraySum(nums3, k=7)
    print(Z) # output: 6