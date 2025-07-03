class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = dict()
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



if __name__ == "__main__":

    obj = Solution()

    nums1 = [1,1,1,2,2,3]
    k1 = 2
    X = obj.topKFrequent(nums1, k1)
    print(X)

    nums2 = [1]
    k2 = 1
    Y = obj.topKFrequent(nums2, k2)
    print(Y)