class Solution:
    def transform_to_even_product(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 1
        mod = (2**9 + 7)
        ans = pow(2, n, mod) # 2^n % mod
        return (ans - 1) % mod





if __name__ == "__main__":
    
    obj = Solution()

    nums1 = [1, 3]
    print(obj.transform_to_even_product(nums = nums1))

    nums2 = [3]
    print(obj.transform_to_even_product(nums = nums2))

    nums3 = [1, 3, 5, 7, 9]
    print(obj.transform_to_even_product(nums = nums3))