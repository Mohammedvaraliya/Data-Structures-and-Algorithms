# Arrays Data-Structures and Algorithms

## 01. Greedy Algorithms: Optimal Task Assignment

    Assign tasks to workers such that the time it takes to complete all tasks is minimized.
    here, the elements in an array is duration of time

---

## 02. Sorting Algorithms: Intersection of Two Sorted Arrays

    Given two arrays, A and B, determine their intersection. That is, what elements are common to A and B?

---

## 03. Binary Search: Find Closest Number

    given a sorted array and a target number. we need to find a number in the array that is closest to the target number.

    The array may contain duplicate values and negative numbers.

    Example 1:
        Input : arr[] = {1, 2, 4, 5, 6, 6, 8, 9}
        Target number = 11
        Output : 9
        9 is closest to 11 in given array

    Example 2:
        Input :arr[] = {2, 5, 6, 7, 8, 8, 9};
        Target number = 4
        Output : 5

---

## 04. Binary Search: Find Fixed Point

    A fixed point in an array "A" is an index "i" such that A[i] is equal to "i".

    Given an array of n distinct integers sorted in ascending order, write a function that returns a "fixed point" in the array. If there is not a
    fixed point return "None".

    Problem is to find only one fixed point.

    Examples:
        # Fixed point is 3:
        A = [-10, -5, 0, 3, 7]

        # Fixed point is 0:
        A = [0, 2, 5, 8, 17]

        # No fixed point. Return "None":
        A = [-10, -5, 3, 4, 7, 9]

---

## 05. Binary Search: Find Bitonic Peak

    Define a bitonic sequence as a sequence of integers such that:
        x_1 <= ... <= x_k >= ... >= x_n-1 for some k, 0 <= k < n.

    For example:
        1, 2, 3, 4, 5, 4, 3, 2, 1

    is a bitcoin sequence. write a program to find the largest element in
    such a sequence. In the above example, the program should return "5".

    we assume that such a peak element exists.

---

## 06. Binary Search: Find First Entry in List with Duplicates

    writing a function that takes an array of sorted integers and a key and returns the index of the first occurrence of that key from the array.

    Example:
        Index:      0   1   2   3    4    5    6    7    8    9
        Array:   [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        Target:  108

        Returns index 3 since 108 appear for the first time at index 3.

---

## 07. Arrays: Array Advance Game

    "array advance game"

    you are given an array of non-negative integers. For example:

    [3,3,1,0,2,0,1].

    Each number represents the maximum you can advance in the array.

    Question:
    Is it possible to advance from the start of the array to the last element?

---

## 08. Arrays: Arbitrary Precision Increment

    Given:
        An array of non-negative digits that represent a decimal integer.

    Problem:
        Add one to the integer. Assume the solution still works even if implemented in a language with finite-precision arithmetic.

---

## 09. Binary Search: Cyclically Shifted Array

[Leetcode Problem URL](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

```bash
Binary Search: Cyclically Shifted Array
An array is "cyclically sorted" if it is possible to cyclically shift
its entries so that it becomes sorted.

The following list is an example of a cyclically sorted array:

    A = [4, 5, 6, 7, 1, 2, 3]

Write a function that determines the index of the smallest element
of the cyclically sorted array.
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
```

---

## 10. Arrays: Two Sum Problem

[Leetcode Problem URL](https://leetcode.com/problems/two-sum/)

```bash
Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
```

---

## 11. Arrays: Buy and Sell Stock

[Leetcode Problem URL](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

```bash
Problem:
    Given an array of numbers consisting of daily stock prices, calculate the maximum amount of profit that can be made from buying on one day and selling on another day.

    We consider two approaches to this problem. In the first, we consider a brute force approach that solves the problem in O(N^2), where N is the size of the array of numbers. We then improve upon this solution to take our solution to a time complexity of O(N).

    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

    Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.
```

---

## 12. Subarray Sum Equals K

[Leetcode Problem URL](https://leetcode.com/problems/subarray-sum-equals-k/)

```bash
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
```

---

## 13. Contains Duplicate

[Leetcode Problem URL](https://leetcode.com/problems/contains-duplicate/)

```bash
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

---

## 14. Group Anagrams

[Leetcode Problem URL](https://leetcode.com/problems/group-anagrams/)

```bash
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
```

---

## 15. Top K Frequent Elements - Bucket Sort

[Leetcode Problem URL](https://leetcode.com/problems/top-k-frequent-elements/)

```bash
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Time coplexity of this solution which i solved is O(n)
```

---

## 16. Product of Array Except Self

[Leetcode Problem URL](https://leetcode.com/problems/product-of-array-except-self/)

```bash
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

---

## 17. Product of Array Except Self

[Leetcode Problem URL](https://leetcode.com/problems/longest-consecutive-sequence/)

```bash
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

---

## 18. 3Sum

[Leetcode Problem URL](https://leetcode.com/problems/3sum/)

```bash
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

---

## 19. Container With Most Water

[Leetcode Problem URL](https://leetcode.com/problems/container-with-most-water/)

```bash
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
```

---

## 20. Unique Number of Occurrences

[Leetcode Problem URL](https://leetcode.com/problems/unique-number-of-occurrences/)

```bash
Given an array of integers arr, return `true` if the number of occurrences of each value in the array is unique or `false` otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
```

---

## 21. Split the Array

[Leetcode Problem URL](https://leetcode.com/problems/split-the-array/)

```bash
You are given an integer array nums of even length. You have to split the array into two parts `nums1` and `nums2` such that:

`nums1.length == nums2.length == nums.length / 2`.
`nums1` should contain distinct elements.
`nums2` should also contain distinct elements.

Return `true` if it is possible to split the array, and `false` otherwise.

Example 1:
Input: nums = [1,1,2,2,3,4]
Output: true
Explanation: One of the possible ways to split nums is nums1 = [1,2,3] and nums2 = [1,2,4].

Example 2:
Input: nums = [1,1,1,1]
Output: false
Explanation: The only possible way to split nums is nums1 = [1,1] and nums2 = [1,1]. Both nums1 and nums2 do not contain distinct elements. Therefore, we return false.
```

### Explanation

The provided solution tackles the problem of splitting an even-length integer array (nums) into two equal-sized sub-arrays that could potentially fulfill the conditions: nums1 and nums2 having distinct elements. While we don't explicitly create these sub-arrays in the code, the logic ensures that a valid split is possible.

The key lies in utilizing a dictionary, named counter, to efficiently track the frequency of each number encountered in nums. By iterating through the array, we check if the current number (num) already exists in counter.

If it's present, its count is incremented. However, if the count goes beyond 2 (meaning more than two occurrences), it violates the distinct element requirement for a valid split, and the function returns False.
If the number is not yet encountered, a new entry is created in counter with a count of 1.

Since the array has an even length and we require distinct elements in each sub-array (implicit in the problem statement), allowing more than two occurrences of any number would prevent a valid split. Therefore, this approach efficiently determines if a valid split is possible based on the frequency of elements in the array, without explicitly creating the sub-arrays.

---

## 22. Kth Largest Element in an Array

[Leetcode Problem URL](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

Given an integer array `nums` and an integer k, return the kth largest element in the array.

Note that it is the $k^{th}$ largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

```bash
Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```

```bash
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```

### Explanation

To solve this problem without sorting the array, I've used min-heap (also known as a priority queue) to efficiently find the kth largest element. Here’s how we can do it:

1. **Initialize a Min-Heap**:

   - A min-heap is a binary tree where the parent node is always less than or equal to its child nodes.
   - The smallest element is always at the root of the heap.
   - We start with an empty heap called `heap`.

2. **Iterate through Each Element**:

   - For each element `num` in the array `nums`, we push it into the heap using `heapq.heappush(heap, num)`.
   - After adding the element, if the size of the heap exceeds `k`, we remove the smallest element using `heapq.heappop(heap)` to ensure the heap size is always `k`.

3. **Return the kth Largest Element**:

   - After processing all elements, the smallest element in the heap is the kth largest element in the array. We return `heap[0]`.

#### Efficiency Analysis

- **Time Complexity**: $O(n \log k)$
  - Adding an element to the heap and removing the smallest element both take $O(\log k)$ time.
  - Since we perform these operations for all `n` elements, the total time complexity is $O(n \log k)$.
- **Space Complexity**: $O(k)$
  - The space complexity is $O(k)$ because the heap will contain at most `k` elements.

#### Why This Approach?

Using a min-heap of size `k` is efficient for finding the kth largest element because:

- It avoids the need to sort the entire array, which would take \(O(n \log n)\) time.
- Maintaining a heap of size `k` ensures that we always have the top `k` largest elements seen so far, and accessing the smallest of these (the kth largest in the array) is \(O(1)\).

By following this approach, we efficiently find the kth largest element with optimal time and space complexity.
