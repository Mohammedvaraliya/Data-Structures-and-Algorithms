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

## 08. Arrays: Arbitrary Precision Increment

    Given:
        An array of non-negative digits that represent a decimal integer.

    Problem:
        Add one to the integer. Assume the solution still works even if implemented in a language with finite-precision arithmetic.

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
