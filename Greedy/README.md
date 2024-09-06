# Greedy Data-Structures and Algorithms

## 01. Maximum Subarray

[Leetcode Problem URL](https://leetcode.com/problems/maximum-subarray/description/)

Given an integer array nums, find the subarray with the largest sum, and return its sum.

A subarray is a contiguous non-empty sequence of elements within an array.

```bash
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
```

```bash
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
```

```bash
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
```

### Explanation

The problem of finding the maximum subarray sum is a classic example where a greedy algorithm is very effective.

A greedy approach is ideal for this problem because:

1. **Local Optimal Choice:** At each position in the array, we decide whether to add the current element to the existing subarray (which is being tracked by `curSub`), or to start a new subarray starting with the current element. This choice is made based on whether adding the current element would increase the sum.
2. **Global Optimal Solution:** The greedy choice made at each step helps to build towards the global optimal solution. By keeping track of the maximum sum seen so far (`maxSub`), we ensure that by the end of the array, `maxSub` holds the maximum sum possible for any subarray.

3. **Initialization:**

   - `maxSub` is initialized to `nums[0]` because the minimum possible subarray sum is any single element from the array.
   - `curSub` is initialized to `0`. This will be used to track the current subarray sum as we iterate through the array.

4. **Iteration:**

   - The loop iterates over each element in `nums`.
   - **Reset Condition:** If `curSub` is negative, it is reset to `0`. This is because a negative subarray sum will decrease the sum of any subsequent elements, so it's better to start fresh.
   - **Update Current Subarray:** `curSub` is updated by adding the current element.
   - **Update Maximum Subarray:** `maxSub` is updated to be the maximum of itself and `curSub`.

5. **Return Result:**
   - After iterating through the entire array, `maxSub` contains the maximum subarray sum.

#### Example Walkthrough

Let’s walk through the first example `nums = [-2,1,-3,4,-1,2,1,-5,4]`:

**Example 1:**

- Input: `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`

  **Step-by-Step Execution:**

  - Initialize `maxSub = -2`, `curSub = 0`
  - For `n = -2`:
    - `curSub = 0 + (-2) = -2`
    - `maxSub = max(-2, -2) = -2`
  - For `n = 1`:
    - `curSub = 0 + 1 = 1` (since `curSub` was negative, it was reset to `0`)
    - `maxSub = max(-2, 1) = 1`
  - For `n = -3`:
    - `curSub = 1 + (-3) = -2`
    - `maxSub = max(1, -2) = 1`
  - For `n = 4`:
    - `curSub = 0 + 4 = 4` (reset because `curSub` was negative)
    - `maxSub = max(1, 4) = 4`
  - For `n = -1`:
    - `curSub = 4 + (-1) = 3`
    - `maxSub = max(4, 3) = 4`
  - For `n = 2`:
    - `curSub = 3 + 2 = 5`
    - `maxSub = max(4, 5) = 5`
  - For `n = 1`:
    - `curSub = 5 + 1 = 6`
    - `maxSub = max(5, 6) = 6`
  - For `n = -5`:
    - `curSub = 6 + (-5) = 1`
    - `maxSub = max(6, 1) = 6`
  - For `n = 4`:
    - `curSub = 1 + 4 = 5`
    - `maxSub = max(6, 5) = 6`

  **Result:**

  - The maximum subarray sum is `6`, which corresponds to the subarray `[4, -1, 2, 1]`.

#### Time and Space Complexity

- **Time Complexity:** `O(n)` where `n` is the length of the input array `nums`. The algorithm makes a single pass through the array.
- **Space Complexity:** `O(1)` because no extra space is used that scales with the input size, only a few variables are used.

## 02. Jump Game

[Leetcode Problem URL](https://leetcode.com/problems/jump-game/description/)

You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return `true` if you can reach the last index, or `false` otherwise.

```bash
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
```

```bash
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
```

### Explanation
