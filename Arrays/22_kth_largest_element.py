import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
            
        return heap[0]




if __name__ == "__main__":
    
    obj = Solution()

    nums1 = [3,2,1,5,6,4]
    k1 = 2
    print(obj.findKthLargest(nums = nums1, k = k1))

    nums2 = [3,2,3,1,2,4,5,5,6]
    k2 = 4
    print(obj.findKthLargest(nums = nums2, k = k2))
    
    
    