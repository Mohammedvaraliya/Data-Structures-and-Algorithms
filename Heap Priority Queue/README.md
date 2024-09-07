# Heap Data-Structures and Algorithms

## 01. Find Median from Data Stream

[Leetcode Problem URL](https://leetcode.com/problems/find-median-from-data-stream/description/)

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

```bash
Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

### Explanation

This solution utilizes two heaps (`small` and `large`) to keep track of the data stream and efficiently find the median.

#### Key Points:

1. **Heap Structure:**

   - We use two heaps:
     - `small`: A max-heap (stores the smaller half of the elements in descending order). Python's `heapq` module doesn't have a built-in max-heap, so we achieve this by negating the elements before inserting them.
     - `large`: A min-heap (stores the larger half of the elements in ascending order).

2. **Adding Numbers:**

   - When a new number (`num`) is added (`addNum` function):
     - We negate `num` and push it onto the `small` heap (`heapq.heappush(self.small, -1 * num)`).

3. **Balancing the Heaps:**

   - After adding, we need to ensure both heaps have roughly the same number of elements to accurately calculate the median. Here's how we achieve balance:

     - **Case 1: Small Heap Overflows:**

       - If the `small` heap has more elements than the `large` heap by more than 1 (`len(self.small) > len(self.large) + 1`), we:
         - Pop the largest element (`val`) from `small` (max-heap, so it's the most negative value). Don't forget to negate it back to its original value.
         - Push this element (`val`) onto the `large` heap (min-heap). This maintains balance and ensures the larger half has at least the same number of elements as the smaller half.

     - **Case 2: Large Heap Overflows:**
       - Similarly, if the `large` heap has more elements than the `small` heap by more than 1 (`len(self.large) > len(self.small) + 1`), we:
         - Pop the smallest element (`val`) from `large` (min-heap).
         - Negate `val` to convert it back to its original value before pushing it onto the `small` heap (max-heap). This maintains balance and ensures the smaller half doesn't fall too far behind.

4. **Finding the Median:**

   - The `findMedian` function calculates the median based on the current heap sizes:
     - If `small` has more elements: The median is the (negated) maximum element from `small` (`-1 * self.small[0]`).
     - If `large` has more elements: The median is the minimum element from `large` (`self.large[0]`).
     - If both heaps have the same size: The median is the average of the maximum element from `small` (negated) and the minimum element from `large` (`(-1 * self.small[0]) + self.large[0]) / 2`).

**Efficiency:**

- This solution has a time complexity of O(log n) for `addNum` and O(1) for `findMedian` operations due to the efficient use of heaps.

---
