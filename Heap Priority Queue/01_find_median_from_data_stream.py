import heapq

class MedianFinder:

    def __init__(self):
        # Two heaps, small(maxheap) and large(minheap)
        # Heaps should be equal size
        self.small, self.large = [], []


    def addNum(self, num: int) -> None:
        # Adding the num in maxheap by multiplying it with -1
        heapq.heappush(self.small, -1 * num)

        # Make sure every num(element) in small heap is <= every num(element) in large heap
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # uneven size? checking the length of both heapqueues which should be approximately equal
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
            

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return (-1 * self.small[0])
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return ((-1 * self.small[0]) + self.large[0]) / 2




if __name__ == "__main__":

    obj = MedianFinder()
    obj.addNum(2)
    med1 = obj.findMedian()
    print(med1)
    obj.addNum(3)
    obj.addNum(4)
    med2 = obj.findMedian()
    print(med2)
    obj.addNum(5)
    med3 = obj.findMedian()
    print(med3)
