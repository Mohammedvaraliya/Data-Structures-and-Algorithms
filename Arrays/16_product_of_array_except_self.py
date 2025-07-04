class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res



if __name__ == "__main__":

    obj = Solution()

    X = obj.productExceptSelf(nums = [1, 2, 3, 4])
    print(X)

    Y = obj.productExceptSelf(nums = [-1, 1, 0, -3, 3])
    print(Y)