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

The problem of determining whether you can reach the last index in the array is solved efficiently using a **greedy approach**. The greedy approach aims to continuously evaluate the farthest point you can jump to while traversing backward through the array. This is more efficient than other approaches like dynamic programming or brute force.

I've chose the greedy approach because:

- **Efficiency**: The greedy approach runs in $O(n)$ time, which is more efficient than other approaches like dynamic programming that may take $O(n^2)$ time.
- **Optimal for this problem**: Instead of storing states or calculating sub-problems like in DP, we only need to track the farthest we can reach, making it an ideal choice.

1. **Goal Position**: We initialize a variable `goal` to track the farthest position we need to reach, starting with the last index (`goal = len(nums) - 1`).

2. **Traverse Backward**: We iterate through the array backward from the second-to-last element (`i = len(nums) - 2`) down to the first element (`i = 0`).

3. **Update Goal**:

   - At each position `i`, check if you can jump from position `i` to the current `goal` (i.e., if `i + nums[i] >= goal`).
   - If you can, update the `goal` to be the current position `i` because now we need to reach `i` instead of the original `goal`.
   - The logic here is simple: if you can jump to the goal from the current position, then the goal moves closer.

4. **Final Check**:

   - After finishing the loop, if `goal == 0`, it means you can reach the first index and then jump all the way to the end. If not, return `false`.

#### Example Walkthrough

##### Example 1: `nums = [2,3,1,1,4]`

1. **Initialization**:

   - Start with `goal = 4` (last index).

2. **Iteration**:

   - `i = 4`: `4 + nums[4] = 4 + 4 = 8 >= goal` → Update `goal = 4`.
   - `i = 3`: `3 + nums[3] = 3 + 1 = 4 >= goal` → Update `goal = 3`.
   - `i = 2`: `2 + nums[2] = 2 + 1 = 3 >= goal` → Update `goal = 2`.
   - `i = 1`: `1 + nums[1] = 1 + 3 = 4 >= goal` → Update `goal = 1`.
   - `i = 0`: `0 + nums[0] = 0 + 2 = 2 >= goal` → Update `goal = 0`.

3. **Final Check**: Since `goal == 0`, return `True`.

##### Example 2: `nums = [3,2,1,0,4]`

1. **Initialization**:

   - Start with `goal = 4` (last index).

2. **Iteration**:

   - `i = 4`: `4 + nums[4] = 4 + 4 = 8 >= goal` → Update `goal = 4`.
   - `i = 3`: `3 + nums[3] = 3 + 0 = 3 < goal`, so `goal` remains 4.
   - `i = 2`: `2 + nums[2] = 2 + 1 = 3 < goal`, so `goal` remains 4.
   - `i = 1`: `1 + nums[1] = 1 + 2 = 3 < goal`, so `goal` remains 4.
   - `i = 0`: `0 + nums[0] = 0 + 3 = 3 < goal`, so `goal` remains 4.

3. **Final Check**: Since `goal != 0`, return `False`.

---

#### Time Complexity

- **O(n)**: We only traverse the array once, from the end to the beginning. Each index is processed in constant time, resulting in linear time complexity.

### Space Complexity

- **O(1)**: We only use a few variables (`goal`) for tracking the farthest reachable position. The space complexity is constant.
