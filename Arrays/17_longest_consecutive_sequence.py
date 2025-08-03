class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
            
        return longest


if __name__ == "__main__":

    obj = Solution()

    X = [100,4,200,1,3,2]
    Y = [0,3,7,2,5,8,4,6,0,1]

    print(obj.longestConsecutive(X))
    print(obj.longestConsecutive(Y))