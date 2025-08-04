# Arrays Data-Structures and Algorithms

## 01. Greedy Algorithms: Optimal Task Assignment

    Assign tasks to workers such that the time it takes to complete all tasks is minimized.
    here, the elements in an array is duration of time

---

---

## 02. Sorting Algorithms: Intersection of Two Sorted Arrays

    Given two arrays, A and B, determine their intersection. That is, what elements are common to A and B?

---

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

---

## 06. Binary Search: Find First Entry in List with Duplicates

    writing a function that takes an array of sorted integers and a key and returns the index of the first occurrence of that key from the array.

    Example:
        Index:      0   1   2   3    4    5    6    7    8    9
        Array:   [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        Target:  108

        Returns index 3 since 108 appear for the first time at index 3.

---

---

## 07. Arrays: Array Advance Game

    "array advance game"

    you are given an array of non-negative integers. For example:

    [3,3,1,0,2,0,1].

    Each number represents the maximum you can advance in the array.

    Question:
    Is it possible to advance from the start of the array to the last element?

---

---

## 08. Plus One

[Leetcode Problem URL](https://leetcode.com/problems/plus-one/)

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

```bash
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```

```bash
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
```

```bash
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
```

### Explanation

1.  Why This Approach Was Chosen

    - Instead of converting the entire array to a number (which could lead to overflow in some languages), we use an **in-place digit-level carry propagation** approach. This method is:

    - Efficient.
    - Safe for arbitrarily large integers.
    - Avoids unnecessary conversions or libraries.

2.  Problem-Solving Pattern Used

    - **Reverse Iteration + Carry Handling** (similar to manual addition)
    - This approach is related to the **greedy pattern**, making the locally optimal choice (increase from the end) for a globally correct solution.

3.  How It’s Efficient Compared to Other Methods

    - **Avoids integer overflow** by not converting the entire number.
    - Works **in-place** with constant space.
    - Handles edge cases like multiple trailing 9s naturally.

#### Step-by-Step Walkthrough

1. Let’s consider the input:

   ```python
   digits = [1, 4, 9]
   ```

   We are adding 1 to the number 149.

2. Initial State:

   - Start from the last digit (i = 2)

3. Iteration Breakdown

   | Step | Index (i) | Value at digits\[i] | Action               | digits         |
   | ---- | --------- | ------------------- | -------------------- | -------------- |
   | 1    | 2         | 9                   | 9 → 0, carry over    | \[1, 4, **0**] |
   | 2    | 1         | 4                   | 4 + 1 = 5, stop here | \[1, **5**, 0] |

4. Final Output:

   ```python
   [1, 5, 0]  # Which represents 150
   ```

5. Edge Case: All Nines

   For `digits = [9, 9, 9]`, you would get:

   | Step | Index | Value     | Action          | digits     |
   | ---- | ----- | --------- | --------------- | ---------- |
   | 1    | 2     | 9         | → 0, carry over | \[9, 9, 0] |
   | 2    | 1     | 9         | → 0, carry over | \[9, 0, 0] |
   | 3    | 0     | 9         | → 0, carry over | \[0, 0, 0] |
   | 4    | -     | prepend 1 | \[1, 0, 0, 0]   |            |

#### Time and Space Complexity

| Metric               | Complexity | Explanation                                                                                                                         |
| -------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Time Complexity**  | $O(n)$     | Traverse the list once from right to left (worst case: all 9s).                                                                     |
| **Space Complexity** | $O(1)$     | Modifies in-place, with the exception of one inserted digit in worst-case (`[1, 0, 0, 0]`). This does not count as auxiliary space. |

#### Summary

- This is a classic digit manipulation problem.
- Efficient single-pass, constant space solution.
- Mastering this problem improves your understanding of digit-by-digit algorithms (similar to handling carry in addition).

---

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

### Explanation

#### Why this Approach?

- We want a **fast and efficient solution**.
- Brute force takes **O(n²)** time – not acceptable for large inputs.
- This approach brings the complexity down to **O(n)** by **trading space for time**.
- I've used a **dictionary (hash table)** to store the complement (`target - nums[i]`) as key and its index as value.

#### Algorithm Explanation

- Initialize an empty hash table (dictionary).
- Iterate over the array.
- For each number `nums[i]`, check:

  - If `nums[i]` exists in the hash table, that means the **complement** was seen before → return `[ht[nums[i]], i]`.
  - Else, store the **complement** (`target - nums[i]`) with index `i`.

#### Example Walkthrough

1. Let’s walk through the function with the input:

   ```python
   nums = [3, 2, 4]
   target = 6
   ```

   We aim to find two indices such that `nums[i] + nums[j] = 6`.

2. Initialization:

   ```python
   ht = {}
   ```

3. Iteration:

   | Iteration | i   | nums\[i] | ht (before check) | Check Condition (nums\[i] in ht?) | Action                                      | ht (after update) |
   | --------- | --- | -------- | ----------------- | --------------------------------- | ------------------------------------------- | ----------------- |
   | 0         | 0   | 3        | {}                | No                                | Store complement 6 - 3 = 3 → ht\[3] = 0     | {3: 0}            |
   | 1         | 1   | 2        | {3: 0}            | No                                | Store complement 6 - 2 = 4 → ht\[4] = 1     | {3: 0, 4: 1}      |
   | 2         | 2   | 4        | {3: 0, 4: 1}      | Yes                               | Match found → return \[ht\[4], 2] = \[1, 2] | Done              |

4. Output: `[1, 2]`

   This means:

   ```python
   nums[1] + nums[2] = 2 + 4 = 6
   ```

#### Time and Space Complexity

| Metric           | Value  | Explanation                               |
| ---------------- | ------ | ----------------------------------------- |
| Time Complexity  | $O(n)$ | Single traversal of array using loop      |
| Space Complexity | $O(n)$ | Worst-case hash table stores all elements |

#### Why This is Efficient

- **No nested loops** unlike the brute-force solution.
- Fast lookups using a **dictionary (hash table)**.
- Provides **immediate complement match** using pre-calculated difference.
- This approach is **scalable for large datasets** due to linear performance.

#### Comparison With Other Approaches

| Approach              | Time Complexity | Space Complexity | Notes                               |
| --------------------- | --------------- | ---------------- | ----------------------------------- |
| Brute Force (2 loops) | $O(n²)$         | $O(1)$           | Inefficient for large `n`           |
| Hash Table            | $O(n)$          | $O(n)$           | Most efficient for unsorted input   |
| Two-pointer (slider)  | $O(n)$          | $O(1)$           | Only works **when array is sorted** |

---

---

## 11. Arrays: Buy and Sell Stock

[Leetcode Problem URL](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

```bash
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
```

```bash
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

### Explanation

We will use a **greedy algorithm** to solve this problem efficiently. The goal is to find the maximum profit by tracking the minimum price seen so far and calculating potential profits as we iterate through the prices.

#### Approach Explanation

1. Why This Approach?

   A brute-force method using two nested loops checks every pair of days to find the maximum profit. However, this is inefficient for large inputs.

   Instead, an **efficient one-pass approach** is used where we keep track of:

   - The **minimum price so far**
   - The **maximum profit so far**

   This allows us to evaluate profit opportunities as we scan through the prices **only once**.

2. Pattern Used

   - **Greedy Algorithm**
   - **Single Pass Scan**
   - You make the locally optimal choice (buy at the lowest price so far) in hope that it leads to the global optimum (maximum overall profit).

3. Why This Is Efficient

   - It avoids unnecessary comparisons.
   - It works in linear time and uses constant space.
   - It’s intuitive, making it ideal for both interviews and production code.

#### Step-by-Step Walkthrough

1. Let’s go through the code using this example:

   ```python
   prices = [7, 1, 5, 3, 6, 4]
   ```

2. Initialization:

   - `min_price = 7` (set to prices\[0])
   - `max_profit = 0`

3. Iteration:

   | Day | Price | min_price   | Current Profit (price - min_price) | max_profit  |
   | --- | ----- | ----------- | ---------------------------------- | ----------- |
   | 0   | 7     | 7           | 0                                  | 0           |
   | 1   | 1     | 1 (updated) | 0                                  | 0           |
   | 2   | 5     | 1           | 4                                  | 4 (updated) |
   | 3   | 3     | 1           | 2                                  | 4           |
   | 4   | 6     | 1           | 5                                  | 5 (updated) |
   | 5   | 4     | 1           | 3                                  | 5           |

4. Final Result:

   - **Maximum Profit = 5**

#### Time and Space Complexity

| Method             | Time Complexity | Space Complexity | Explanation                                                 |
| ------------------ | --------------- | ---------------- | ----------------------------------------------------------- |
| Brute-force        | $O(n²)$         | $O(1)$           | Compares all pairs `(i, j)` where `i < j`                   |
| Optimized (Greedy) | $O(n)$          | $O(1)$           | Single scan; tracks min and max profit using constant space |

#### Summary

- The brute-force approach is easy to understand but not suitable for large inputs.
- The optimal solution uses a **greedy approach** to continuously track the lowest buying price and update maximum profit accordingly.
- This solution is **efficient**, **clean**, and **ideal for interview coding problems**.
- Time complexity is **O(n)**, and space complexity is **O(1)**, making it a top-tier solution.

---

---

## 12. Subarray Sum Equals K

[Leetcode Problem URL](https://leetcode.com/problems/subarray-sum-equals-k/)

Given an array of integers nums and an integer `k`, return the total number of subarrays whose sum equals to `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

```bash
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
```

```bash
Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
```

### Explanation

We will use a trick called cumulative sum (think of it like adding up the numbers one by one) and a little memory helper (called a hashmap) to keep track of things we've already added up.

We use a **prefix sum with hashmap** approach to solve this problem in linear time. This is an optimized method that avoids brute-force checking of all subarrays.

#### **Why This Approach Was Chosen**

- A brute-force solution would require checking all subarrays and computing their sums, which leads to **O(n²)** time complexity. This is inefficient for large arrays.
- The prefix sum method allows us to calculate the sum of any subarray in **O(1)** time using previously stored cumulative sums.
- A hashmap helps us efficiently track how many times a specific cumulative sum has occurred, which allows us to count valid subarrays without iterating over them again.

#### **Underlying Pattern**

This solution is based on the **prefix sum** technique combined with **hashing** for fast lookups.

We maintain:

- Cumulative Sum: We keep adding the numbers one by one. Each time we do that, we check if the difference between the current sum (s) and k has appeared before.
- Map: The map remembers all the sums we've seen so far, and how many times we’ve seen them. This helps us check quickly if there's a subarray that sums to k.

The key idea is:

> If `s` is the current cumulative sum and `s - k` has appeared before, then there exists a subarray ending at the current index which sums to `k`.

#### Step-by-Step Walkthrough

1. Let’s walk through this with the input:

   ```python
   nums = [1, 1, 1], k = 2
   ```

2. Initialization:

   - `sumdict = {0: 1}`
     (There's one way to have a sum of 0 before starting) This means we’ve seen a sum of 0 once (before starting).
   - `count = 0`
   - `s = 0` (Running sum)

3. Iteration Details:

   | Iteration | num | s (cumulative sum) | s - k | sumdict lookup | count (subarrays) | sumdict updated        |
   | --------: | --- | ------------------ | ----- | -------------- | ----------------- | ---------------------- |
   |         1 | 1   | 1                  | -1    | not found      | 0                 | `{0:1, 1:1}`           |
   |         2 | 1   | 2                  | 0     | found → +1     | 1                 | `{0:1, 1:1, 2:1}`      |
   |         3 | 1   | 3                  | 1     | found → +1     | 2                 | `{0:1, 1:1, 2:1, 3:1}` |

4. Final Result:

   - `count = 2`

   This means there are **2 subarrays** whose sum is `k = 2`.

   - Subarray `[1,1]` at index 0 to 1
   - Subarray `[1,1]` at index 1 to 2

5. **Example: nums = `[1, 1, 1]`, k = 2**

6. **Start with an empty list** and a running sum of 0.

   - **Map** (`sumdict`): This will keep track of how many times a certain sum has appeared.
   - Start with `{0: 1}`. This means we’ve seen a sum of 0 **once** (before starting).

7. **Start walking through the list:**

8. Step 1: Take the first number, which is `1`.

   - **Running sum (s)**: Add `1` to our current sum, so `s = 1`.
   - **Check if we’ve seen `s - k`** before:

   - We want to know if `s - k = 1 - 2 = -1` has been seen. It hasn’t, so no new subarray found.
   - **Update the map**: We’ve now seen a sum of `1`, so we update the map: `{0: 1, 1: 1}`.
   - No subarray found yet, so `count = 0`.

9. Step 2: Take the second number, which is `1`.

   - **Running sum (s)**: Add `1` again, so `s = 2`.
   - **Check if we’ve seen `s - k`** before:

   - We want to know if `s - k = 2 - 2 = 0` has been seen. Yes! The sum `0` was seen before (at the start).
   - This means there’s a subarray that ends here and has a sum of `2`! The subarray is `[1, 1]`.
   - **Update the map**: Now we’ve seen a sum of `2`, so we update the map: `{0: 1, 1: 1, 2: 1}`.
   - We found **1 subarray** so far, so `count = 1`.

10. Step 3: Take the third number, which is `1`.

    - **Running sum (s)**: Add `1` again, so `s = 3`.
    - **Check if we’ve seen `s - k`** before:

    - We want to know if `s - k = 3 - 2 = 1` has been seen. Yes! The sum `1` was seen before (at step 1).
    - This means there’s another subarray that ends here and has a sum of `2`! The subarray is `[1, 1]`.
    - **Update the map**: Now we’ve seen a sum of `3`, so we update the map: `{0: 1, 1: 1, 2: 1, 3: 1}`.
    - We found **another subarray**. Now, `count = 2`.

11. Final Result:

    We have found **2 subarrays** with a sum of `2`:

    1. Subarray `[1, 1]` at indices 0 to 1
    2. Subarray `[1, 1]` at indices 1 to 2

    So, the output is `2`.

#### Time and Space Complexity Analysis

1. **Time Complexity: O(n)**

   - We iterate over the array exactly once.
   - All operations inside the loop (sum calculation, dictionary lookup and update) are O(1).

2. **Space Complexity: O(n)**

   - In the worst case, all prefix sums are unique, and we store `n` sums in the hashmap.

#### Strengths of This Solution:

- **Optimal Time:** Achieves linear time, a significant improvement over brute-force O(n²).
- **In-place Processing:** Only uses a hashmap for auxiliary storage.
- **Scalable:** Works efficiently even on large arrays (e.g., 10⁵+ elements).

#### When to Use This Pattern:

Look for these cues:

- You are asked to count subarrays or ranges that meet a specific sum or condition.
- Prefix sums or differences are relevant.
- You need an efficient way to search previous computations → use a hashmap.

---

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

### Explanation

#### Why this Approach?

- Anagrams have **exactly the same letters** with **the same frequency**.
- Instead of sorting strings (which costs O(n log n)), we can use a **fixed-size frequency count array** of 26 letters as a **hashable key**.
- This allows **constant-time comparison** between different anagram groups and leads to **better performance** on large input sizes.

#### Key Idea:

Use a **dictionary (hash map)** where:

- **Key** = A **tuple of 26 integers**, each representing the **frequency of a character** in the word (from `'a'` to `'z'`)
- **Value** = List of strings (words) that match that frequency key (i.e., are anagrams)

#### Example Walkthrough

1. Let’s walk through the input:

   ```python
   strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
   ```

   - We want to group anagrams together.
   - We will build a dictionary where the **key is the character frequency tuple**.

2. Initial State:

   ```python
   res = defaultdict(list)
   ```

3. `s = "eat"`

   - count = `[0, 0, ..., 0]` (length 26)
   - Processing `'e'`: `count[4] += 1`
   - Processing `'a'`: `count[0] += 1`
   - Processing `'t'`: `count[19] += 1`
   - count = `[1, 0, 0, 0, 1, ..., 1, ..., 0]`
   - Key = `(1, 0, 0, 0, 1, ..., 1, ..., 0)`
   - Store: `res[key] = ["eat"]`

4. `s = "tea"`

   - `'t'` → `count[19] += 1`
   - `'e'` → `count[4] += 1`
   - `'a'` → `count[0] += 1`
   - Key is same as previous → group with "eat"
   - Store: `res[key] = ["eat", "tea"]`

5. `s = "tan"`

   - `'t'` → `count[19] += 1`
   - `'a'` → `count[0] += 1`
   - `'n'` → `count[13] += 1`
   - Key = `(1, 0, 0, 0, 0, ..., 1 (at index 13), ..., 1 (at 19))`
   - New key → `res[key] = ["tan"]`

6. `s = "ate"`

   - Same frequency as `"eat"` and `"tea"`
   - Store: `res[previous_key] = ["eat", "tea", "ate"]`

7. `s = "nat"`

   - Same frequency as `"tan"`
   - Store: `res[previous_key] = ["tan", "nat"]`

8. `s = "bat"`

   - `'b'` → `count[1] += 1`
   - `'a'` → `count[0] += 1`
   - `'t'` → `count[19] += 1`
   - New key → `res[key] = ["bat"]`

9. Final Dictionary:

   ```python
   {
   (1, 0, 0, 0, 1, ..., 1): ["eat", "tea", "ate"],
   (1, 0, 0, 0, 0, ..., 1 at index 13, ..., 1): ["tan", "nat"],
   (1, 1, 0, ..., 1, ..., 0): ["bat"]
   }
   ```

10. Output:

    ```python
    [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    ```

#### Time and Space Complexity

| Metric           | Value     | Explanation                                                 |
| ---------------- | --------- | ----------------------------------------------------------- |
| Time Complexity  | O(n \* k) | `n` = number of words, `k` = average length of each word    |
| Space Complexity | O(n \* k) | Storing all words in groups + frequency array as tuple keys |

- **Building frequency array** takes O(k) time per string.
- In total, the time is O(nk), which is **better than sorting each string** (O(nk log k)).

#### Why This is Efficient

- **Sorting-based approach** would require O(k log k) per word. With n words → O(nk log k)
- **This approach** uses **O(k)** per word using **fixed-size counting array** → more efficient.
- The use of **tuple as a hash key** is a Pythonic way to ensure dictionary lookups are fast and unique for each anagram group.

#### Comparison With Other Approaches

| Approach                  | Time Complexity | Space Complexity | Notes                                                |
| ------------------------- | --------------- | ---------------- | ---------------------------------------------------- |
| Sort each word + hashmap  | O(nk log k)     | O(nk)            | Slower due to string sorting                         |
| Frequency count + hashmap | O(nk)           | O(nk)            | Optimal, avoids sorting, used in this implementation |

#### Final Thoughts

- The **frequency-count approach** is the most optimal for grouping anagrams in Python.
- Using **defaultdict** simplifies grouping logic.
- This approach ensures performance even on larger inputs while maintaining clarity and correctness.

---

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

### Explanation

A standard approach using a heap would give a time complexity of O(n log k). - However, we can solve it in **O(n)** time using **Bucket Sort**, which is more efficient and optimal for this problem when `k` is small relative to `n`.

#### Step-by-Step Algorithm

1. **Frequency Counting**

   - Use a hash map (`count`) to count the frequency of each number in the array.

2. **Bucket Indexing**

   - Create a list of empty buckets (`freq`), where index `i` represents all numbers with frequency `i`.

3. **Populating Buckets**

   - For each key-value pair in the frequency map, place the number in the bucket at index equal to its frequency.

4. **Collect Top K Frequent**

   - Traverse the bucket list in reverse (from high to low frequency).
   - Accumulate the numbers in the result list until `k` elements are collected.

#### Example Walkthrough

1. Let’s walk through:

   ```python
   nums = [1,1,1,2,2,3]
   k = 2
   ```

2. Step 1: Frequency Count

   - Using a dictionary:

     ```python
     count = {
        1: 3,
        2: 2,
        3: 1
     }
     ```

   - Explanation:

     - `1` appears 3 times
     - `2` appears 2 times
     - `3` appears 1 time

3. Step 2: Bucket Initialization

   - Create an array of empty lists of size `len(nums) + 1 = 7`:

     ```python
     freq = [[], [], [], [], [], [], []]  # indices 0 to 6
     ```

4. Step 3: Fill the Buckets

   - We loop through `count.items()`:

   - `count[1] = 3` → place `1` in `freq[3]`
   - `count[2] = 2` → place `2` in `freq[2]`
   - `count[3] = 1` → place `3` in `freq[1]`

   - Resulting buckets:

   ```python
   freq = [[], [3], [2], [1], [], [], []]
            0   1    2    3
   ```

5. Step 4: Collecting Top K Frequent Elements

   - Start from the end of the `freq` list and move backwards:

     ```python
     res = []

     i = 6 → freq[6] is empty → skip
     i = 5 → empty → skip
     i = 4 → empty → skip
     i = 3 → freq[3] = [1]
           res = [1]

     i = 2 → freq[2] = [2]
           res = [1, 2]

     len(res) == k → stop
     ```

6. Final Output:

   ```python
   [1, 2]
   ```

#### Time and Space Complexity

| Metric           | Value  | Explanation                                  |
| ---------------- | ------ | -------------------------------------------- |
| Time Complexity  | $O(n)$ | Single pass to count frequency + bucket scan |
| Space Complexity | $O(n)$ | Frequency map + buckets list                 |

#### Comparison With Other Approaches

| Approach               | Time Complexity | Space Complexity | Notes                                        |
| ---------------------- | --------------- | ---------------- | -------------------------------------------- |
| HashMap + Heap         | $O(n log k)$    | $O(n + k)$       | Slower due to heap operations                |
| **Bucket Sort (used)** | **O(n)**        | **O(n)**         | Optimal – constant time for frequency lookup |

#### Final Thoughts

- Bucket sort shines in problems like this, where frequencies are bounded and we care about top-K.
- This implementation uses a clean and readable Pythonic approach using:

  - `dict` for counting
  - `list` of buckets
  - reverse loop to collect top-k items efficiently

---

---

## 16. Product of Array Except Self

[LeetCode Problem URL](https://leetcode.com/problems/product-of-array-except-self/)

Given an integer array nums, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

```bash
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
```

```bash
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

**Constraints:**

- Do **not** use the division operator.
- Time complexity must be **O(n)**.
- The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

### Explanation

We solve the problem using **two passes** over the array:

1. First pass (Left to Right): Compute **prefix products**.
2. Second pass (Right to Left): Compute **postfix products** and multiply with prefix values stored earlier.

This avoids the use of division and achieves O(n) time and O(1) auxiliary space (not counting the output array).

#### What Pattern Should We Look For?

When the problem requires calculating results **excluding** the current index, and when:

- The operation is associative (like multiplication or addition),
- Division is not allowed,
- You must preserve the result in a single pass or two passes efficiently,

**Prefix and Postfix technique** is the ideal pattern.

#### Step-by-Step Breakdown of Logic

1. #### Walkthrough with Input:

   ```python
   nums = [1, 2, 3, 4]
   ```

2. Initialize result array `res` to hold prefix products:

   ```python
   res = [1, 1, 1, 1]  # This will eventually hold our result
   ```

3. First Pass: Prefix Product

   Start from left to right and compute product of all elements to the **left of current index**.

4. **Iteration-wise update:**

   | i   | prefix | res\[i] | prefix update (prefix \*= nums\[i]) |
   | --- | ------ | ------- | ----------------------------------- |
   | 0   | 1      | 1       | prefix = 1 × 1 = 1                  |
   | 1   | 1      | 1       | prefix = 1 × 2 = 2                  |
   | 2   | 2      | 2       | prefix = 2 × 3 = 6                  |
   | 3   | 6      | 6       | prefix = 6 × 4 = 24                 |

5. After this step:

   ```python
   res = [1, 1, 2, 6]
   ```

6. Second Pass: Postfix Product

   Start from right to left and multiply current `res[i]` with product of all elements **to the right**.

7. **Iteration-wise update:**

   | i   | postfix | res\[i] (before) | res\[i] (after \*= postfix) | postfix update (postfix \*= nums\[i]) |
   | --- | ------- | ---------------- | --------------------------- | ------------------------------------- |
   | 3   | 1       | 6                | 6                           | postfix = 1 × 4 = 4                   |
   | 2   | 4       | 2                | 2 × 4 = 8                   | postfix = 4 × 3 = 12                  |
   | 1   | 12      | 1                | 1 × 12 = 12                 | postfix = 12 × 2 = 24                 |
   | 0   | 24      | 1                | 1 × 24 = 24                 | postfix = 24 × 1 = 24                 |

8. Final `res` after this step:

   ```python
   [24, 12, 8, 6]
   ```

9. #### Walkthrough with Input:

   ```python
   nums = [-1, 1, 0, -3, 3]
   ```

10. Initial state:

    ```python
    res = [1, 1, 1, 1, 1]
    ```

11. First Pass (Prefix):

    | i   | prefix | res\[i] | prefix \*= nums\[i]  |
    | --- | ------ | ------- | -------------------- |
    | 0   | 1      | 1       | prefix = 1 × -1 = -1 |
    | 1   | -1     | -1      | prefix = -1 × 1 = -1 |
    | 2   | -1     | -1      | prefix = -1 × 0 = 0  |
    | 3   | 0      | 0       | prefix = 0 × -3 = 0  |
    | 4   | 0      | 0       | prefix = 0 × 3 = 0   |

12. After prefix step:

    ```python
    res = [1, -1, -1, 0, 0]
    ```

13. Second Pass (Postfix):

    | i   | postfix | res\[i] (before) | res\[i] (after) | postfix update        |
    | --- | ------- | ---------------- | --------------- | --------------------- |
    | 4   | 1       | 0                | 0               | postfix = 1 × 3 = 3   |
    | 3   | 3       | 0                | 0               | postfix = 3 × -3 = -9 |
    | 2   | -9      | -1               | -1 × -9 = 9     | postfix = -9 × 0 = 0  |
    | 1   | 0       | -1               | -1 × 0 = 0      | postfix = 0 × 1 = 0   |
    | 0   | 0       | 1                | 1 × 0 = 0       | postfix = 0 × -1 = 0  |

14. **Final Output:**

    ```python
    [0, 0, 9, 0, 0]
    ```

#### Time and Space Complexity

| Metric           | Value  | Explanation                                    |
| ---------------- | ------ | ---------------------------------------------- |
| Time Complexity  | $O(n)$ | One pass for prefix + one pass for postfix     |
| Space Complexity | $O(1)$ | Output array doesn’t count towards extra space |

#### Comparison with Other Approaches

| Approach         | Time     | Space    | Notes                              |
| ---------------- | -------- | -------- | ---------------------------------- |
| Division-based   | $O(n)$   | $O(1)$   | Not allowed in problem constraints |
| Prefix + Postfix | **O(n)** | **O(1)** | Optimal; handles zeros correctly   |

---

---

## 17. Longest Consecutive Sequence

[Leetcode Problem URL](https://leetcode.com/problems/longest-consecutive-sequence/)

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in `O(n)` time.

```bash
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
```

```bash
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
```

```bash
Example 3:

Input: nums = [1,0,1,2]
Output: 3
```

### Explanation

To solve the problem of finding the longest consecutive sequence in an unsorted array, we can use a **set** to achieve an average time complexity of O(n). The key idea is to leverage the properties of sets for fast lookups and to iterate through the numbers only once.

#### (True) Approach Explanation

1. Why this Approach?

   We used a **hash set** to achieve `O(n)` time complexity. The idea is to only start counting sequences from numbers that are the **start** of a sequence (i.e., `n-1` is not in the array), which guarantees that we only scan each sequence once.

2. Problem-Solving Pattern

   - **Hashing / Set-based Lookup**
   - **Greedy / Linear Scanning**
   - Efficient use of hash sets for `O(1)` average-time lookups

3. Why It’s Efficient and Elegant

   - The **naive approach** would be to sort the array (`O(n log n)`) and then find the sequence — but the question explicitly requires `O(n)`.
   - By using a set, we reduce duplicate checks and unnecessary work — each element is visited **once**, and each sequence is processed **only from its smallest element**.

#### Step-by-Step Walkthrough

1. Let's use the example:

   ```python
   nums = [100, 4, 200, 1, 3, 2]
   ```

2. Step 0: Initialize

   ```python
   numSet = {100, 4, 200, 1, 3, 2}
   longest = 0
   ```

   | Iteration | Current `n` | Is `n-1` in Set? | Start New Sequence? | Sequence Count (`length`) | Current `longest` |
   | --------- | ----------- | ---------------- | ------------------- | ------------------------- | ----------------- |
   | 1         | 100         | 99 (False)       | (True) Yes          | 1                         | 1                 |
   | 2         | 4           | 3 (True)         | (False) No          | -                         | 1                 |
   | 3         | 200         | 199 (False)      | (True) Yes          | 1                         | 1                 |
   | 4         | 1           | 0 (False)        | (True) Yes          | \[1,2,3,4] → 4            | 4                 |
   | 5         | 3           | 2 (True)         | (False) No          | -                         | 4                 |
   | 6         | 2           | 1 (True)         | (False) No          | -                         | 4                 |

3. Final `longest = 4`

#### Explanation of Key Logic

1. **Convert the list to a set** for `O(1)` lookups.
2. **Only start counting** from numbers that are **not** part of a longer sequence (i.e., `n-1` is not in the set).
3. Use a **while loop** to count how many consecutive numbers exist starting from `n`.
4. Track the **maximum sequence length** found so far.

#### Time and Space Complexity Analysis

| Metric           | Complexity | Explanation                                                   |
| ---------------- | ---------- | ------------------------------------------------------------- |
| Time Complexity  | $O(n)$     | Each element is visited once; set lookups are O(1) on average |
| Space Complexity | $O(n)$     | `numSet` stores all elements once                             |
| Auxiliary Space  | $O(1)$     | Only a few variables are used for counting                    |

#### Summary

- This solution is optimal and satisfies the `O(n)` constraint.
- Utilizes **hash sets** to detect the start of a sequence and avoid redundant work.
- Handles edge cases like duplicates and scattered values efficiently.

---

---

## 18. 3Sum

[Leetcode Problem URL](https://leetcode.com/problems/3sum/)

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

```bash
Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
```

```bash
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

```bash
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

### Explanation

This problem is a classic example of finding triplets in an array that sum to zero. The most efficient way to solve this problem is by using a combination of sorting and the two-pointer technique.

#### Approach Explanation

1. Why this Approach?

   The naive brute-force approach would require checking all triplets in `O(n³)` time. That’s inefficient for large inputs.

   Instead, this approach:

   - Sorts the array.
   - Uses a **fixed pointer** and a **two-pointer technique** to efficiently find pairs that sum to the negative of the fixed element.

   This reduces time complexity to **O(n²)**.

2. Problem-Solving Pattern Used

   - **Sorting**
   - **Two-Pointer Technique**
   - **Duplicate Skipping Strategy**

3. Why It’s Efficient

   - Sorting helps with efficient scanning and duplicate elimination.
   - Two-pointer technique reduces nested loop combinations.
   - Only valid, non-repeating triplets are added to the result.

#### Step-by-Step Walkthrough

1. We'll take the example:

   ```python
   nums = [-1, 0, 1, 2, -1, -4]
   ```

2. After sorting:

   ```
   nums = [-4, -1, -1, 0, 1, 2]
   ```

3. We iterate `i` through the list, fixing one number `a = nums[i]`, and use two pointers `l` and `r` to find two other numbers such that `a + nums[l] + nums[r] == 0`.

   | i   | a   | l   | nums\[l] | r   | nums\[r]                 | Sum                | Action                                   | Result                     |
   | --- | --- | --- | -------- | --- | ------------------------ | ------------------ | ---------------------------------------- | -------------------------- |
   | 0   | -4  | 1   | -1       | 5   | 2                        | -4 + (-1) + 2 = -3 | Sum < 0 → increment `l`                  | —                          |
   | 0   | -4  | 2   | -1       | 5   | 2                        | -4 + (-1) + 2 = -3 | Sum < 0 → increment `l`                  | —                          |
   | 0   | -4  | 3   | 0        | 5   | 2                        | -4 + 0 + 2 = -2    | Sum < 0 → increment `l`                  | —                          |
   | 0   | -4  | 4   | 1        | 5   | 2                        | -4 + 1 + 2 = -1    | Sum < 0 → increment `l`                  | —                          |
   | 1   | -1  | 2   | -1       | 5   | 2                        | -1 + (-1) + 2 = 0  | Found triplet! Move `l`, skip duplicates | \[\[-1, -1, 2]]            |
   | 1   | -1  | 3   | 0        | 4   | 1                        | -1 + 0 + 1 = 0     | Found triplet! Move `l`, skip duplicates | \[\[-1, -1, 2], \[-1,0,1]] |
   | 2   | -1  | —   | —        | —   | Duplicate `-1`, skip     | —                  | —                                        |                            |
   | 3   | 0   | 4   | 1        | 5   | 2                        | 0 + 1 + 2 = 3      | Sum > 0 → decrement `r`                  | —                          |
   | 4   | 1   | —   | —        | —   | Positive `a`, break loop | —                  | —                                        |                            |

4. Final Output

   ```python
   [[-1, -1, 2], [-1, 0, 1]]
   ```

#### Intermediate Details Explained

- **Sorted array** simplifies duplicate handling and allows binary-like search.
- **Two-pointer approach** is used inside a loop fixing one element each time.
- **Skip conditions** help remove duplicates from the result.
- **Early stopping**: If the fixed number `a > 0`, we know the sum can't be 0, so we break.

#### Time and Space Complexity

| Metric               | Complexity | Explanation                                                              |
| -------------------- | ---------- | ------------------------------------------------------------------------ |
| **Time Complexity**  | $O(n²)$    | Outer loop runs `n` times, and inner two-pointer loop runs in `O(n)`     |
| **Space Complexity** | $O(1)$     | We don’t use extra space (ignoring output list which is required anyway) |

> Note: Sorting takes O(n log n), but the dominant term is the nested loop (O(n²)).

---

---

## 19. Container With Most Water

[LeetCode Problem URL](https://leetcode.com/problems/container-with-most-water/)

You are given an integer array `height` of length `n`. There are n vertical lines drawn such that the two endpoints of the `ith` line are (i, 0) and (`i, height[i]`).

Find two lines that together with the `x-axis` form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

![IMG](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```bash
Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

```bash
Example 2:

Input: height = [1,1]
Output: 1
```

### Explanation

#### Approach Explanation

1. Why This Approach?

   The brute-force solution checks every possible pair of lines to find the maximum area, which is inefficient for large inputs.

   To solve this optimally, we use the **Two Pointer Technique**, which enables us to solve the problem in linear time. This is both efficient and elegant, avoiding unnecessary computations.

2. Pattern Used

   - **Two Pointer Technique**
   - The left and right pointers start at both ends of the array and move toward each other, shrinking the width and choosing the direction based on the shorter height to maximize area potential.

3. Why This Is Efficient

   - It avoids nested loops (as in brute-force).
   - It guarantees every potential widest container is evaluated with at least one pointer moved.
   - Reduces time complexity from $O(n²)$ to $O(n)$, which is optimal for this problem.

#### Step-by-Step Walkthrough

1. Input:

   ```python
   height = [1,8,6,2,5,4,8,3,7]
   ```

2. Initialization:

   - `left = 0`, `right = 8`, `res = 0`

3. Iterations:

   1. `left = 0`, `right = 8`: min(1,7)=1 → area = 8×1 = 8 → max = 8
      Move left pointer (since height\[0] < height\[8])

   2. `left = 1`, `right = 8`: min(8,7)=7 → area = 7×7 = 49 → max = 49
      Move right pointer (since height\[1] > height\[8])

   3. `left = 1`, `right = 7`: min(8,3)=3 → area = 6×3 = 18 → max = 49
      Move right pointer

   4. `left = 1`, `right = 6`: min(8,8)=8 → area = 5×8 = 40 → max = 49
      Move right pointer

   5. `left = 1`, `right = 5`: min(8,4)=4 → area = 4×4 = 16 → max = 49
      Move right pointer

   6. `left = 1`, `right = 4`: min(8,5)=5 → area = 3×5 = 15 → max = 49
      Move right pointer

   7. `left = 1`, `right = 3`: min(8,2)=2 → area = 2×2 = 4 → max = 49
      Move right pointer

   8. `left = 1`, `right = 2`: min(8,6)=6 → area = 1×6 = 6 → max = 49
      Move right pointer

   9. `left = 1`, `right = 1`: loop ends

4. Final Result:

   ```python
   Maximum area = 49
   ```

#### Time and Space Complexity

| Method                | Time Complexity | Space Complexity | Explanation                     |
| --------------------- | --------------- | ---------------- | ------------------------------- |
| Brute-force           | $O(n²)$         | $O(1)$           | Nested loops to try all pairs   |
| Two-pointer (Optimal) | $O(n)$          | $O(1)$           | Single-pass scan from both ends |

#### Summary

- The brute-force approach checks all pairs, which is inefficient for large inputs.
- The two-pointer approach leverages greedy principles to move the pointer pointing to the smaller height inward, thereby optimizing the area.
- This is a classic and efficient way to solve container problems using the **Two-Pointer Technique**.
- The optimal solution is **linear in time and constant in space**, which is ideal for real-time or large-scale inputs.

---

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

#### Approach Explanation

1. Why This Approach?

   The naive solution would be to **sort the entire array** and return the kᵗʰ largest element. This is simple but not optimal for large datasets, especially when sorting isn't necessary to get just one element.

   A better approach uses a **Min Heap** of size `k` to efficiently track the k largest elements seen so far. This allows us to extract the kᵗʰ largest element without sorting the entire array.

2. Problem-Solving Pattern Used

   - **Heap (Priority Queue)** pattern.
   - This is a classic use-case for a **Min Heap** where we maintain the top `k` largest elements.
   - Python's `heapq` module implements a min-heap by default.

3. Why This Is Efficient and Elegant

   - Instead of sorting `n` elements (which is O(n log n)), we only keep the top `k` elements in the heap.
   - Each insertion and removal operation from the heap takes O(log k) time.
   - Hence, this solution is far more scalable for large arrays.

#### Step-by-Step Walkthrough

1. Let's walk through the example:

   ```python
   nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
   ```

   We use a **min heap** (`heap[]`) to store the largest `k = 4` elements. The smallest among them (at `heap[0]`) will be the 4ᵗʰ largest overall.

1. Iterations:

   1. `num = 3` → heap = \[3]
   2. `num = 2` → heap = \[2, 3]
   3. `num = 3` → heap = \[2, 3, 3]
   4. `num = 1` → heap = \[1, 2, 3, 3]
   5. `num = 2` → heap = \[1, 2, 3, 3, 2] → size > k ⇒ pop smallest ⇒ heap = \[2, 2, 3, 3]
   6. `num = 4` → heap = \[2, 2, 3, 3, 4] ⇒ size > k ⇒ pop ⇒ heap = \[2, 3, 3, 4]
   7. `num = 5` → heap = \[2, 3, 3, 4, 5] ⇒ pop ⇒ heap = \[3, 3, 5, 4]
   8. `num = 5` → heap = \[3, 3, 5, 4, 5] ⇒ pop ⇒ heap = \[3, 4, 5, 5]
   9. `num = 6` → heap = \[3, 4, 5, 5, 6] ⇒ pop ⇒ heap = \[4, 5, 5, 6]

1. Final Heap:

   ```python
   [4, 5, 5, 6]
   ```

   - The smallest of the top 4 elements is `heap[0] = 4`, which is the **4ᵗʰ largest element**.

#### Time and Space Complexity Analysis

| Method                      | Time Complexity  | Space Complexity | Notes                                                          |
| --------------------------- | ---------------- | ---------------- | -------------------------------------------------------------- |
| Sorting                     | $O(n \ log \ n)$ | $O(1)$ or $O(n)$ | Built-in sort; space depends on language's sort implementation |
| Min Heap (Optimal Approach) | $O(n \ log \ k)$ | $O(k)$           | Maintains a heap of size `k` throughout the traversal of array |

#### Summary

- The Min Heap approach efficiently solves the problem without sorting the entire array.
- It works well even when the input is large and only a small portion of the result is needed (the kᵗʰ largest).
- Clean and effective, this method is widely used in top-k problems, streaming data, and real-time analytics.

---

---

## 23. Transform to Even Product

[Problem from Languify Interview Platform](https://interview.languify.in/)

Consider an integer array `A` that includes `N` integers.

You are allowed to perform a specific operation on this array `A`, which involves selecting any number of elements from the array `A` and altering their values to whatever you choose.

The initial Product of the elements in the array `A` is `ODD`, and your task is to determine the total number of unique operations (modulo $10^9 + 7$) that can be conducted to change the product of the array to `EVEN`.

Two operations are considered distinct if there is `atleast one` element not chosen in the other operation.

```bash
Problem Constraints:
1 <= N <= 105
1 <= A[i] <= 106
The initial product of array `A` is guaranteed to be odd
```

```bash
Input Format:
A single integer array `A`.
```

```bash
Output Format:
Return a single integer, the number of unique operations to transform the product into an even number, modulo $10^9 + 7$.
```

```bash
Example 1:

Input: A = [1, 3]
Output: 3

Explanation:
- We can perform a maximum of three operations:
- Operation 1: Choosing the element at index 0 and changing its value to 2, resulting in A = [2,3] with a Product = 6
- Operation 2: Choosing the element at index 1 and changing its value to 10, resulting in A = [1,10] with a Product = 10
- Operation 3: Choosing both elements at index 0 and 1 and changing their values to 2, resulting in A = [2,2] with a Product = 4
- No additional operations can be performed on this array.
```

```bash
Example 2:

Input 2: A = [3]
Output: 1

Explanation:
- We can perform a maximum of one operation:
- Operation 1: Choosing the element at index 0 and changing its value to 20, resulting in A = [20] with a Product = 20
```

### Explanation

If the initial product is **odd**, then **all elements in the array must be odd** (because any even number would make the product even).

To make the product **even**, we need **at least one even number** in the array after the operation.

Thus, the goal is to **select any non-empty subset** of the array and change **at least one** number to an **even number**.

#### Key Observations

- Every **non-empty subset** of the array where **at least one element is changed** can potentially make the product even.
- Total number of **non-empty subsets** of an `n`-element array is `2^n - 1`.
- If we change any subset of elements, and **at least one becomes even**, the resulting product will be even.

- So, all `2^n - 1` non-empty subsets of the array **can potentially be transformed to have at least one even**.

- Hence, the answer is:

  ```
  Total ways = (2^n - 1) % MOD
  ```

#### Example Walkthrough

1. Take the last example:

   ```python
   A = [1, 3, 5, 7, 9]
   ```

2. Step 1: Confirm Product is Odd

   - All elements are odd:

   - `1 * 3 * 5 * 7 * 9 = 945` → odd

3. Step 2: Calculate Total Non-empty Subsets

   - Array length `n = 5`
   - Total non-empty subsets = `2^n - 1 = 2^5 - 1 = 32 - 1 = 31`
   - So, **31 distinct operations** can be performed to make the product even.

4. Explanation of a few sample operations:

   | Subset Indices Changed | Modified Elements    | Modified Array   | Product | Is Even |
   | ---------------------- | -------------------- | ---------------- | ------- | ------- |
   | \[0]                   | A\[0] = 2            | \[2, 3, 5, 7, 9] | 1890    | Yes     |
   | \[1, 3]                | A\[1] = 4, A\[3] = 6 | \[1, 4, 5, 6, 9] | 1080    | Yes     |
   | \[0, 1, 2, 3, 4]       | All changed to even  | \[2, 2, 2, 2, 2] | 32      | Yes     |
   | \[2, 4]                | A\[2] = 6, A\[4] = 8 | \[1, 3, 6, 7, 8] | Even    | Yes     |

   - All of these are distinct because they involve different subsets.

5. Final Answer

   ```python
   return 31
   ```

#### Time and Space Complexity

| Metric           | Complexity | Explanation                                                                             |
| ---------------- | ---------- | --------------------------------------------------------------------------------------- |
| Time Complexity  | $O(1)$     | Single computation: `pow(2, n, mod)` is done in constant time using fast exponentiation |
| Space Complexity | $O(1)$     | Constant extra space used regardless of input size                                      |

#### Why This Approach is Efficient

- **Mathematical Insight** avoids the need to enumerate subsets.
- Avoids brute-force approach of generating all subsets (which is exponential).
- **Fast Modular Exponentiation** computes `2^n % mod` efficiently in O(log n) time.
- Handles large constraints efficiently (`n ≤ 10^5`).

---

---

## 24. Reverse String

[Leetcode Problem URL](https://leetcode.com/problems/reverse-string/)

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.

```bash
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

```bash
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

### Explanation

**Approach: Two-Pointer Technique**

To reverse an array **in-place**, we use the **two-pointer technique**:

- Start one pointer (`p`) at the beginning of the array.
- Start another pointer (`q`) at the end of the array.
- Swap the characters at `p` and `q`.
- Move `p` forward and `q` backward.
- Repeat until both pointers meet or cross.

This guarantees that every element is moved to its correct reversed position **without using any extra space**.

#### Step-by-Step Walkthrough

1. Let’s walkthrough this using:

   ```python
   s = ["H", "a", "n", "n", "a", "h"]
   ```

2. Initial state:

   ```
   p = 0, q = 5
   s = ["H", "a", "n", "n", "a", "h"]
   ```

   | Iteration | p   | q   | s\[p] | s\[q] | Action                           | Array After Swap                       |
   | --------- | --- | --- | ----- | ----- | -------------------------------- | -------------------------------------- |
   | 1         | 0   | 5   | "H"   | "h"   | Swap s\[0] and s\[5]             | \["h", "a", "n", "n", "a", "H"]        |
   | 2         | 1   | 4   | "a"   | "a"   | Swap s\[1] and s\[4] (no change) | \["h", "a", "n", "n", "a", "H"]        |
   | 3         | 2   | 3   | "n"   | "n"   | Swap s\[2] and s\[3] (no change) | \["h", "a", "n", "n", "a", "H"]        |
   | 4         | 3   | 2   | —     | —     | p > q → Loop ends                | Final: \["h", "a", "n", "n", "a", "H"] |

#### Time and Space Complexity

| Complexity       | Value  | Explanation                                              |
| ---------------- | ------ | -------------------------------------------------------- |
| Time Complexity  | $O(n)$ | Each character is swapped at most once                   |
| Space Complexity | $O(1)$ | No extra memory used beyond a few pointers and temp vars |

#### Why This Approach?

- The **two-pointer technique** is optimal when we need to **swap elements symmetrically** from the ends.
- It’s ideal when we’re constrained by **in-place** and **O(1) space**.
- Avoids creation of new arrays or use of built-in reversing functions.

#### What Pattern Should I Look For?

This problem is part of the **Two-Pointer In-Place Swap Pattern**.
Look for this pattern when:

- You're reversing elements
- Rotating arrays
- Partitioning elements (like in QuickSort, Dutch National Flag, etc.)
- In-place transformation is required

---

---

## 25. Maximum Number of Words Found in Sentences

[Leetcode Problem URL](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/)

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings `sentences`, where each `sentences[i]` represents a single `sentence`.

Return the maximum number of words that appear in a single sentence.

```bash
Example 1:

Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
Output: 6
Explanation:
- The first sentence, "alice and bob love leetcode", has 5 words in total.
- The second sentence, "i think so too", has 4 words in total.
- The third sentence, "this is great thanks very much", has 6 words in total.
Thus, the maximum number of words in a single sentence comes from the third sentence, which has 6 words.
```

```bash
Example 2:

Input: sentences = ["please wait", "continue to fight", "continue to win"]
Output: 3
Explanation: It is possible that multiple sentences contain the same number of words.
In this example, the second and third sentences (underlined) have the same number of words.
```

### Explanation

**Approach Used: Pythonic Split and Count**

- Each sentence is a string of words separated by spaces.
- To count the words in each sentence, we can use Python’s `str.split()` method which splits the sentence at each space and returns a list of words.
- The length of this list gives us the number of words.
- Track the maximum word count encountered while iterating through all sentences.

#### Step-by-Step Walkthrough

1. Let’s walk through the example:

   ```python
   sentences = [
      "alice and bob love leetcode",
      "i think so too",
      "this is great thanks very much"
   ]
   ```

1. Initial State:

   ```
   res = 0
   ```

   | Iteration | sentence                         | sentence.split()                                   | Word Count | Updated res |
   | --------- | -------------------------------- | -------------------------------------------------- | ---------- | ----------- |
   | 1         | "alice and bob love leetcode"    | \['alice', 'and', 'bob', 'love', 'leetcode']       | 5          | 5           |
   | 2         | "i think so too"                 | \['i', 'think', 'so', 'too']                       | 4          | 5           |
   | 3         | "this is great thanks very much" | \['this', 'is', 'great', 'thanks', 'very', 'much'] | 6          | **6**       |

1. Final Result:

   ```python
   return res  → 6
   ```

#### Why This Approach?

- `str.split()` efficiently handles word extraction in Python.
- Simple, clean, and readable one-pass loop.
- We avoid manual space counting (compared to brute force character-by-character iteration).

#### Time and Space Complexity

| Complexity       | Value         | Justification                                            |
| ---------------- | ------------- | -------------------------------------------------------- |
| Time Complexity  | $O(n $\*$ m)$ | Where `n` is number of sentences and `m` is avg length   |
| Space Complexity | $O(1)$        | We use only constant space (`res`), split allocates temp |

> Note: If you consider `split()` space internally, it uses O(m) temporarily, but result is not stored globally.

#### Pattern Recognition

This problem falls under:

- **String Manipulation**
- **Counting**
- **Maximum Pattern**
- **In-place Linear Scan**

Look for problems that involve measuring something across multiple strings (e.g., longest/shortest word, most vowels, longest sentence) — this maximum accumulation pattern is frequently useful.

---

---

## 26. Move Zeroes

[LeetCode Problem URL](https://leetcode.com/problems/move-zeroes/)

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

```bash
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

```bash
Example 2:

Input: nums = [0]
Output: [0]
```

### Explanation

#### Approach Explanation

1. **Overview**

   This solution uses a **two-pointer** or **in-place overwrite** strategy to maintain the relative ordering of non-zero elements and move all zeroes to the end.

2. **Why This Approach Was Chosen**

   - **In-place requirement:** The problem specifically asks not to use extra space for another array. Hence, an in-place technique is needed.
   - **Order preservation:** Unlike some greedy or swap-based techniques that may reorder elements, this approach **preserves the relative order** of all non-zero elements.
   - **Efficiency:** The approach ensures only a single pass to shift non-zeroes, and a second short pass to fill trailing zeros. This ensures **O(n)** time complexity with minimal operations.

3. **Underlying Pattern**

   This is a classic example of the **Two-Pointer Pattern**:

   - One pointer (`i`) iterates through the array to explore elements.
   - Another pointer (`non_zero_pos`) tracks the position to place the next non-zero value.

#### Step-by-Step Walkthrough

1. Let us walk through the example:

   ```python
   Input: nums = [0, 1, 0, 3, 12]
   ```

2. Initialization:

   - `non_zero_pos = 0`
     This will point to the index where the next non-zero value should be placed.

3. First Loop: Shift Non-Zero Elements to the Front

   | Iteration | i   | nums\[i] | Action                            | nums               | non_zero_pos |
   | --------- | --- | -------- | --------------------------------- | ------------------ | ------------ |
   | 0         | 0   | 0        | Skip (since nums\[0] is 0)        | \[0, 1, 0, 3, 12]  | 0            |
   | 1         | 1   | 1        | nums\[0] = 1; `non_zero_pos` → 1  | \[1, 1, 0, 3, 12]  | 1            |
   | 2         | 2   | 0        | Skip                              | \[1, 1, 0, 3, 12]  | 1            |
   | 3         | 3   | 3        | nums\[1] = 3; `non_zero_pos` → 2  | \[1, 3, 0, 3, 12]  | 2            |
   | 4         | 4   | 12       | nums\[2] = 12; `non_zero_pos` → 3 | \[1, 3, 12, 3, 12] | 3            |

   Now, non-zero values have been pushed forward:
   Intermediate array: `[1, 3, 12, 3, 12]`

4. Second Loop: Fill Remaining Positions with Zeroes

   Start filling from index `non_zero_pos = 3` till the end.

   | Iteration | i   | Action       | nums               |
   | --------- | --- | ------------ | ------------------ |
   | 0         | 3   | nums\[3] = 0 | \[1, 3, 12, 0, 12] |
   | 1         | 4   | nums\[4] = 0 | \[1, 3, 12, 0, 0]  |

   Final Output: `[1, 3, 12, 0, 0]`

#### Time and Space Complexity

1. **Time Complexity: O(n)**

   - First pass (moving non-zeroes): O(n)
   - Second pass (filling zeroes): O(n)
   - Overall: **O(n)** where `n` is the number of elements in the input array.

2. **Space Complexity: O(1)**

   - The entire operation is performed **in-place**, using only constant extra variables (`non_zero_pos` and `i`).
   - No additional space is allocated based on input size.

### Strengths of This Solution:

- Fully in-place and maintains relative order.
- Efficient in both time and space.
- Simple to understand and implement.

#### When to Use This Pattern:

- Problems that require modifying an array **in-place**.
- When order of certain elements needs to be preserved while filtering or shifting.
- When we want to separate or push specific elements (like `0`s here) to the start or end of an array.

---

---

## 27. Sort Array By Parity

[Leetcode Problem URL](https://leetcode.com/problems/sort-array-by-parity/)

Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

```bash
Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```

```bash
Example 2:

Input: nums = [0]
Output: [0]
```

### Explanation

The problem requires rearranging an array so that all **even numbers appear before odd numbers**, maintaining **no specific relative order**. To solve this, two methods are considered:

- **Brute Force Approach**: Use additional space to build a result array.
- **In-Place Two-Pointer Approach**: Modify the array directly using the two-pointer technique.

#### Why This Approach Was Chosen

The in-place **two-pointer approach** was chosen for the final solution because:

- It satisfies the in-place constraint (no extra array used).
- It reduces space complexity from O(n) to **O(1)**.
- It is more **efficient and elegant** than building a new array using two separate loops.
- It avoids unnecessary memory allocation and copying.

#### Problem-Solving Pattern

This approach follows the **Two-Pointer Pattern**, which is commonly used when modifying or partitioning arrays in-place based on a condition.

- One pointer (`left`) moves forward from the start.
- Another pointer (`right`) moves backward from the end.
- When necessary, values are **swapped** to ensure even numbers go to the front and odd numbers go to the back.

#### Step-by-Step Walkthrough

1. Input:

   ```python
   nums = [3, 1, 2, 4]
   ```

2. Initial State:

   - `left = 0`, pointing to `nums[0] = 3`
   - `right = 3`, pointing to `nums[3] = 4`

3. Iteration 1:

   - `nums[left] = 3` → odd
   - `nums[right] = 4` → even
   - Swap `nums[left]` and `nums[right]` → `nums = [4, 1, 2, 3]`
   - Increment `left → 1`, Decrement `right → 2`

4. Iteration 2:

   - `nums[left] = 1` → odd
   - `nums[right] = 2` → even
   - Swap `nums[left]` and `nums[right]` → `nums = [4, 2, 1, 3]`
   - Increment `left → 2`, Decrement `right → 1`

5. Exit Condition:

- `left >= right` (2 ≥ 1), loop ends.

1. Final Output:

   ```python
   [4, 2, 1, 3]
   ```

   Any order that places all even numbers before odd numbers is valid. Therefore, this output is accepted.

#### Time and Space Complexity Analysis

1. Time Complexity: **O(n)**

- Each element is visited at most once.
- Swapping is a constant time operation.

> **Total Time = O(n)**, where `n` is the length of the array.

---

2. Space Complexity: **O(1)**

- No additional space is used except for a few pointers.
- The input array is modified in-place.

> **Total Space = O(1)** constant space.

#### Strengths of the Two-Pointer In-Place Approach:

- Efficient: O(n) time, O(1) space.
- No auxiliary array is needed.
- Easy to implement and understand.
- Well-suited for partitioning problems.

#### When to Use This Pattern:

- When the problem involves rearranging elements based on a condition (e.g., even vs. odd).
- When in-place modification is required or optimal.
- When order of elements is not important, only grouping by condition.

---

---

## 28. Remove Duplicates from Sorted Array

[Leetcode Problem URL](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of nums contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

**Custom Judge:**

The judge will test your solution with the following code:

```bash
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be accepted.

```bash
Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

```bash
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

### Explanation

#### Approach Explanation

1. Why This Approach Was Chosen

   This problem is best tackled using a **two-pointer** approach that processes the array in a **single pass** while modifying it in-place. This pattern is optimal because:

   - It respects the in-place constraint.
   - It avoids unnecessary shifting or auxiliary data structures.
   - It allows direct overwriting of duplicates with the next distinct values.

2. Applied Pattern

   - **Two-Pointer Technique**:

   - `prev` pointer keeps track of the position of the **last unique element**.
   - `next` pointer scans through the array, identifying **new unique elements**.

This pattern is frequently used in array transformation problems where you need to "move" or "filter" values efficiently in-place.

3. How This Is More Efficient

   - **Brute force** solutions may require building new arrays or using sets.
   - This solution avoids any additional space while operating in linear time.
   - Each element is visited exactly once, making the approach both efficient and elegant.

### Step-by-Step Walkthrough

1. Input:

   ```python
   nums = [0,0,1,1,1,2,2,3,3,4]
   ```

2. Initial State:

   - `prev = 0`, `next = 1`

3. Iteration-wise Trace:

   | Iteration | `next` Index | `nums[next]` | `nums[prev]` | Action                        | Updated `nums`         | `prev` |
   | --------- | ------------ | ------------ | ------------ | ----------------------------- | ---------------------- | ------ |
   | 1         | 1            | 0            | 0            | Duplicate, skip               | \[0,0,1,1,1,2,2,3,3,4] | 0      |
   | 2         | 2            | 1            | 0            | New unique → move to `prev+1` | \[0,1,1,1,1,2,2,3,3,4] | 1      |
   | 3         | 3            | 1            | 1            | Duplicate, skip               | \[0,1,1,1,1,2,2,3,3,4] | 1      |
   | 4         | 4            | 1            | 1            | Duplicate, skip               | \[0,1,1,1,1,2,2,3,3,4] | 1      |
   | 5         | 5            | 2            | 1            | New unique → move to `prev+1` | \[0,1,2,1,1,2,2,3,3,4] | 2      |
   | 6         | 6            | 2            | 2            | Duplicate, skip               | \[0,1,2,1,1,2,2,3,3,4] | 2      |
   | 7         | 7            | 3            | 2            | New unique → move to `prev+1` | \[0,1,2,3,1,2,2,3,3,4] | 3      |
   | 8         | 8            | 3            | 3            | Duplicate, skip               | \[0,1,2,3,1,2,2,3,3,4] | 3      |
   | 9         | 9            | 4            | 3            | New unique → move to `prev+1` | \[0,1,2,3,4,2,2,3,3,4] | 4      |

4. Final State:

   - `prev = 4`, so total unique elements = `prev + 1 = 5`
   - `nums` becomes: `[0, 1, 2, 3, 4, _, _, _, _, _]`

5. Return Value:

   ```python
   return 5
   ```

### Time and Space Complexity

| Complexity | Value  | Explanation                                         |
| ---------- | ------ | --------------------------------------------------- |
| Time       | $O(n)$ | The array is traversed once.                        |
| Space      | $O(1)$ | No extra space is used; in-place modification only. |

#### Summary

- **Pattern**: Two-pointer (in-place overwrite).
- **Efficiency**: Optimal space and linear time.
- **Mutates input array** to store unique values at the start.

#### Use-Cases for This Pattern

- Removing duplicates in sorted arrays.
- In-place filtering of elements based on conditions.
- Partitioning or compressing data in fixed memory.

---

---

## 29. Remove Element

[Leetcode Problem URL](https://leetcode.com/problems/remove-element/)

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

**Custom Judge:**

The judge will test your solution with the following code:

```bash
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be accepted.

```bash
Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

```bash
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

### Explanation

1. Why This Approach Was Chosen

   The requirement is to modify the array in-place without using extra space, while filtering out a specific value. A **two-pointer technique** provides the cleanest and most optimal way to achieve this by:

   - Keeping track of the position where the next non-`val` element should be placed.
   - Skipping the values that need to be removed.
   - Ensuring we never use extra memory.

2. Problem-Solving Pattern

   This solution follows the **Two-Pointer Technique**, specifically the **fast-slow pointer** or **overwrite pattern**:

   - One pointer (`next`) scans through the array.
   - The other pointer (`cur`) tracks the position to place the next valid value.

   This is a common pattern used in problems like:

   - Removing duplicates
   - Moving zeros
   - Filtering elements in place

3. Why This Is Efficient

   Compared to brute-force approaches that may shift elements or use new lists:

   - This method **minimizes writes**.
   - It maintains **O(1) space** and **linear time**.
   - It works in-place and is suitable even for large arrays.

#### Step-by-Step Walkthrough

1. Input:

   ```python
   nums = [0,1,2,2,3,0,4,2], val = 2
   ```

2. Initial State:

   - `cur = 0` (position to place next valid element)

3. Iteration-wise Trace:

   | Iteration | `next` | `nums[next]` | Action Taken           | Updated `nums`     | `cur` |
   | --------- | ------ | ------------ | ---------------------- | ------------------ | ----- |
   | 0         | 0      | 0            | Valid → place at `cur` | \[0,1,2,2,3,0,4,2] | 1     |
   | 1         | 1      | 1            | Valid → place at `cur` | \[0,1,2,2,3,0,4,2] | 2     |
   | 2         | 2      | 2            | Skip (matches `val`)   | \[0,1,2,2,3,0,4,2] | 2     |
   | 3         | 3      | 2            | Skip                   | \[0,1,2,2,3,0,4,2] | 2     |
   | 4         | 4      | 3            | Valid → place at `cur` | \[0,1,3,2,3,0,4,2] | 3     |
   | 5         | 5      | 0            | Valid → place at `cur` | \[0,1,3,0,3,0,4,2] | 4     |
   | 6         | 6      | 4            | Valid → place at `cur` | \[0,1,3,0,4,0,4,2] | 5     |
   | 7         | 7      | 2            | Skip                   | \[0,1,3,0,4,0,4,2] | 5     |

4. Final Result:

   - Modified `nums`: `[0, 1, 3, 0, 4, _, _, _]`
   - Return value: `5` (count of valid elements)

#### Time and Space Complexity

| Complexity | Value  | Explanation                                   |
| ---------- | ------ | --------------------------------------------- |
| Time       | $O(n)$ | Every element is visited exactly once.        |
| Space      | $O(1)$ | No extra data structures used; in-place only. |

#### Summary

- **Pattern**: Two-pointer overwrite.
- **Efficiency**: Best possible for in-place modification with O(1) space.
- **Simplicity**: Clear and easy to implement.

This method can be generalized for many in-place filtering or transformation problems, making it an essential technique in array manipulation.

---

---

## 30. Find Second Largest Element

You have been given an array/list 'ARR' of integers. Your task is to find the second largest element present in the 'ARR'.

Note:

1. Duplicate elements may be present.
2. If no such element is present return -1.

```bash
Example:
Input: Given a sequence of five numbers 2, 4, 5, 6, 8.
Output:  6
Explanation:
In the given sequence of numbers, number 8 is the largest element, followed by number 6 which is the second-largest element. Hence we return number 6 which is the second-largest element in the sequence.
```

### Explanation

#### Approach Explanation

1. Why This Approach Was Chosen

   The problem requires finding the second-largest element in an unsorted array **without using extra space or sorting**. A **single-pass traversal** is optimal because it avoids the overhead of sorting (`O(n log n)`) and is memory efficient.

2. Problem-Solving Pattern

   This approach is based on a **Greedy + Linear Scan** pattern:

   - **Greedy**: At each step, we keep track of the best (largest) and second-best (second largest) values seen so far.
   - **Linear Scan**: We only make one pass over the array, checking each number once.

#### Step-by-Step Walkthrough

1. Input:

   ```python
   nums = [7, 3, 9, 2, 8]
   ```

1. Initial State:

- `first = -inf` (tracks the largest value seen)
- `second = -inf` (tracks the second largest)

1. Iteration-wise Trace:

   | Iteration | `num` | Condition                             | `first` | `second` |
   | --------- | ----- | ------------------------------------- | ------- | -------- |
   | 1         | 7     | 7 > -inf → update `first`             | 7       | -inf     |
   | 2         | 3     | 3 < 7 → update `second` to 3          | 7       | 3        |
   | 3         | 9     | 9 > 7 → `second = first`, `first = 9` | 9       | 7        |
   | 4         | 2     | 2 < 7 → no update                     | 9       | 7        |
   | 5         | 8     | 8 < 9 and > 7 → update `second = 8`   | 9       | 8        |

1. Final Result:

   - `first = 9`
   - `second = 8`

1. Output:

   ```python
   return second  # → 8
   ```

#### Alternative (Brute Force Approach)

Sorting the array in descending order and picking the first distinct element that is less than the maximum.
**Drawback**: Requires extra time (`O(n log n)`) and potentially extra space.

#### Time and Space Complexity

| Metric           | Complexity | Explanation                                                          |
| ---------------- | ---------- | -------------------------------------------------------------------- |
| Time Complexity  | $O(n)$     | Single loop through the array to find the largest and second largest |
| Space Complexity | $O(1)$     | No additional data structures used                                   |

#### Summary

- Efficient single-pass solution.
- No extra space used.
- Covers edge cases like duplicates and very small arrays.
- A must-know pattern for problems involving **top-k** elements.

---

---

## 31. Find Minimum and Maximum

Given an array, the task is to find the maximum and the minimum element of the array using the minimum number of comparisons.

```bash
Examples:

Input: arr[] = {3, 5, 4, 1, 9}
Output:
Minimum element is: 1
Maximum element is: 9
```

```bash
Input: arr[] = {22, 14, 8, 17, 35, 3}
Output:
Minimum element is: 3
Maximum element is: 35
```

### Explanation

#### Approach Explanation

1. **Chosen Strategy**

   - The solution uses a **single linear traversal** to simultaneously track both the minimum and maximum values in the array.
   - At each iteration, we compare the current number with the current `min_val` and `max_val`, updating them as necessary.

2. **Why This Approach?**

   - The approach is straightforward and efficient for this problem.
   - Instead of sorting the array or doing multiple passes (which would be inefficient), we find both values in one traversal using only **2 comparisons per element**.

3. **Problem-Solving Pattern**

   - This approach follows the **greedy pattern** and also leverages the **iterative traversal** technique.
   - It greedily updates the current best-known minimum and maximum as it scans the array from left to right.

4. **Efficiency and Elegance**

   - **Efficiency**: This method performs exactly `2(n-1)` comparisons in the worst case (where `n` is the length of the array).
   - **Elegance**: It's simple, readable, and does not rely on auxiliary data structures.

#### Step-by-Step Walkthrough

1. Let’s walk through the code using the input:

   ```python
   nums = [5, 3, 9, 2, 8]
   ```

2. Initial Setup

   - `min_val = +∞`
   - `max_val = -∞`

3. Iteration Breakdown

   | Iteration | Current `n` | Comparison with `max_val` | Update `max_val`? | Comparison with `min_val` | Update `min_val`? |
   | --------- | ----------- | ------------------------- | ----------------- | ------------------------- | ----------------- |
   | 1         | 5           | 5 > -∞ → true             | max_val = 5       | 5 < ∞ → true              | min_val = 5       |
   | 2         | 3           | 3 > 5 → false             | no                | 3 < 5 → true              | min_val = 3       |
   | 3         | 9           | 9 > 5 → true              | max_val = 9       | 9 < 3 → false             | no                |
   | 4         | 2           | 2 > 9 → false             | no                | 2 < 3 → true              | min_val = 2       |
   | 5         | 8           | 8 > 9 → false             | no                | 8 < 2 → false             | no                |

4. Final Output

   - After all iterations:

   - `min_val = 2`
   - `max_val = 9`

   - Output: `"Maximum is 9, and minimum is 2"`

#### Time and Space Complexity Analysis

| Complexity Type  | Value    | Explanation                                                                  |
| ---------------- | -------- | ---------------------------------------------------------------------------- |
| Time Complexity  | **O(n)** | We traverse the array once, making 2 comparisons per element (except first). |
| Space Complexity | **O(1)** | Constant extra space is used regardless of input size.                       |

#### Summary

- This implementation finds both the minimum and maximum in a **single pass** through the array.
- It is both time-efficient and space-efficient, using a simple greedy strategy.
- No auxiliary space or complex logic is needed, making it ideal for real-world applications where performance and clarity are equally important.

---

---

## 32. Majority Element

[LeetCode Problem URL](https://leetcode.com/problems/majority-element/)

Given an array nums of size `n`, return the majority element.

The majority element is the element that appears more than ⌊`n / 2`⌋ times. You may assume that the majority element always exists in the array.

```bash
Example 1:

Input: nums = [3,2,3]
Output: 3
```

```bash
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

### Explanation

#### Approach Explanation

1. Why This Approach?

   The chosen approach uses a **frequency counting technique** with the help of a hash map (dictionary) to track the occurrence of each element in the list. This allows us to quickly identify the number of times each number appears and determine the element that occurs more than `n // 2` times.

   This method is chosen because:

   - It is simple and effective.
   - It ensures linear time complexity.
   - It leverages hashing, which is commonly used in frequency-based problems.

2. Problem-Solving Pattern Used

   - **Hash Map (Dictionary) Counting**: Each element is used as a key in the dictionary and its frequency is updated as the list is traversed.
   - **Greedy Element Selection**: We keep track of the maximum frequency seen so far and select the corresponding element as the current candidate for the majority.

3. Efficiency and Elegance

   While more advanced solutions like the **Boyer-Moore Voting Algorithm** exist with `O(1)` space, this counting approach is:

   - **Intuitive and beginner-friendly**.
   - **Easy to debug and extend** for variations (e.g., top-k frequent elements).
   - Still runs in **O(n)** time, making it efficient for most use cases.

#### Step-by-Step Walkthrough

1. Input:

   ```python
   nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]
   ```

2. Step 1: Count Frequency of Each Element

3. We iterate through the array and build a frequency map (`count`):

   | Step | Element | count dictionary   |
   | ---- | ------- | ------------------ |
   | 1    | 3       | {3: 1}             |
   | 2    | 3       | {3: 2}             |
   | 3    | 4       | {3: 2, 4: 1}       |
   | 4    | 2       | {3: 2, 4: 1, 2: 1} |
   | 5    | 4       | {3: 2, 4: 2, 2: 1} |
   | 6    | 4       | {3: 2, 4: 3, 2: 1} |
   | 7    | 2       | {3: 2, 4: 3, 2: 2} |
   | 8    | 4       | {3: 2, 4: 4, 2: 2} |
   | 9    | 4       | {3: 2, 4: 5, 2: 2} |

4. Step 2: Find the Element with the Highest Frequency

5. We iterate over the `count` dictionary:

   - `3` → count = 2 → max_count = 2, res = 3
   - `4` → count = 5 → max_count = 5, res = 4
   - `2` → count = 2 → no update

6. **Final result**: `4`, which appears 5 times in a list of size 9 (> 9/2 = 4.5)

#### Time and Space Complexity Analysis

| Metric               | Complexity | Explanation                                                                   |
| -------------------- | ---------- | ----------------------------------------------------------------------------- |
| **Time Complexity**  | $O(n)$     | Single pass to build the frequency map + another pass to find max = 2 \* O(n) |
| **Space Complexity** | $O(n)$     | At worst, all elements are distinct, so dictionary stores `n` entries         |

#### Summary

- The implemented solution uses **hashing (dictionary)** to count element frequencies.
- It ensures **linear time complexity** and is easy to implement.
- Ideal for interviews and early-stage problem solving.
- For better space optimization, consider **Boyer-Moore Voting Algorithm**.

---

---

## 33. Rotate Array

[LeetCode Problem URL](https://leetcode.com/problems/rotate-array/)

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

```bash
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

```bash
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```

### Explanation

#### Approach Explanation

1. Why This Approach?

   To rotate the array efficiently **in-place without using extra space**, we used a **three-step reversal algorithm**.

   Instead of rotating one element at a time (which would be inefficient for large arrays), this approach leverages the fact that rotating an array to the right by `k` steps is equivalent to:

   > 1. Reversing the entire array
   > 2. Reversing the first `k` elements
   > 3. Reversing the remaining `n-k` elements

2. Problem-Solving Pattern Used

   - **Two-pointer technique**: For reversing segments of the array in-place.
   - **Array manipulation and reversal**: Breaking the array into parts and manipulating them by reversing in-place.

3. Why This Approach is Efficient and Elegant

   - It rotates the array **in O(n)** time.
   - It requires **only constant O(1)** extra space.
   - The logic is clean and works regardless of array size or rotation count.
   - Avoids unnecessary rotations by doing `k = k % n` (important when `k > n`).

#### Step-by-Step Walkthrough

1. Let’s walk through the code with the example:

   ```python
   nums = [1, 2, 3, 4, 5, 6, 7]
   k = 3
   ```

1. Step 0: Normalize `k`

   ```python
   k %= n  # k = 3 % 7 = 3
   ```

1. Step 1: Reverse the entire array

   ```python
   Before: [1, 2, 3, 4, 5, 6, 7]
   After full reverse: [7, 6, 5, 4, 3, 2, 1]
   ```

1. Step 2: Reverse the first `k` elements

   ```python
   Before: [7, 6, 5, 4, 3, 2, 1]
   After reversing first 3: [5, 6, 7, 4, 3, 2, 1]
   ```

1. Step 3: Reverse the remaining `n-k` elements

   ```python
   Before: [5, 6, 7, 4, 3, 2, 1]
   After reversing last 4: [5, 6, 7, 1, 2, 3, 4]
   ```

1. Final Output:

   ```python
   [5, 6, 7, 1, 2, 3, 4]
   ```

#### Time and Space Complexity Analysis

| Metric               | Complexity | Explanation                                                  |
| -------------------- | ---------- | ------------------------------------------------------------ |
| **Time Complexity**  | $O(n)$     | Three full reversals of the array or its parts               |
| **Space Complexity** | $O(1)$     | All operations are done in-place; no additional space needed |

#### Summary

- The implemented solution uses the **reversal algorithm**, which is the most optimal approach for in-place array rotation.
- It avoids excessive shifting or use of extra arrays.
- The logic is clean, and the implementation is intuitive with good use of pointers or Python slicing.
- This approach is recommended for both **interviews** and **real-world performance-critical applications**.

---

---

## 34. Two Sum II - Input Array Is Sorted

[LeetCode Problem URL](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length `2`.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

```bash
Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

```bash
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```

```bash
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
```

### Explanation

This problem can be efficiently solved using the **two-pointer technique** due to the sorted nature of the input array. The goal is to find two indices such that their corresponding values sum up to a given target.

#### Approach Explanation

1. Why this Approach?

   We chose the **two-pointer approach** because the array is sorted. This allows us to **scan from both ends** towards the center efficiently and find the correct pair in **linear time** without using any extra space like hash maps.

2. Pattern Used

   - **Two-Pointer Technique**
   - **Greedy (move pointer based on condition)**
   - Takes advantage of **sorted property** of the input array

3. Why It’s Efficient

   - **No need to use extra space** (e.g., hash maps)
   - **Linear time complexity** O(n), better than brute force O(n²)
   - Simple and easy to implement

#### Step-by-Step Walkthrough

1. Let's walk through the following example:

   ```python
   numbers = [2, 7, 11, 15]
   target = 9
   ```

2. Initial pointers:

   - `l = 0` → points to 2
   - `r = 3` → points to 15

   | Step | l   | numbers\[l] | r   | numbers\[r] | curSum = numbers\[l] + numbers\[r] | Action                  |
   | ---- | --- | ----------- | --- | ----------- | ---------------------------------- | ----------------------- |
   | 1    | 0   | 2           | 3   | 15          | 17                                 | curSum > target → r--   |
   | 2    | 0   | 2           | 2   | 11          | 13                                 | curSum > target → r--   |
   | 3    | 0   | 2           | 1   | 7           | 9                                  | curSum == target → True |

3. Return `[l+1, r+1] = [1, 2]`

#### How It Works (Logic Breakdown)

1. **Start with two pointers**:

   - `l` at the beginning
   - `r` at the end

2. **Repeat until pointers meet**:

   - Calculate `curSum = numbers[l] + numbers[r]`
   - If `curSum > target`, move `r` left (reduce the sum)
   - If `curSum < target`, move `l` right (increase the sum)
   - If `curSum == target`, return `[l+1, r+1]` as indices are 1-based

3. **Why move pointers like this?**

   - The array is sorted. So:

     - Decreasing `r` → moves to smaller numbers
     - Increasing `l` → moves to larger numbers

#### Time and Space Complexity

| Metric               | Complexity | Explanation                                                   |
| -------------------- | ---------- | ------------------------------------------------------------- |
| **Time Complexity**  | $O(n)$     | Each pointer moves at most `n` steps — total linear traversal |
| **Space Complexity** | $O(1)$     | No extra data structures used — only two pointers maintained  |

---

---
