# Binary search Data-Structures and Algorithms

## 01. Binary search

    Binary search
    Binary Search is a searching algorithm for finding an element's position in a sorted array.

    In this approach, the element is always searched in the middle of a portion of an array.

    Binary search can be implemented only on a sorted list of items. If the elements are not sorted already,
    we need to sort them first.

    Example:
    Let us take the following sorted array and we need to search element 6.

                    [2,	5,	6,	8,	10,	11,	13,	15,	16]

                Low=0   <-- index number
                High=8  <-- index number
                Mid=4   <-- index number

                    [2,	5,	6,	8,	10,	11,	13,	15,	16]

                6 < 10, therefore take the first half.

                High=Mid-1

                Low=0
                High=3
                Mid=1

                    [2,	5,	6,	8,	10,	11,	13,	15,	16]

                6==6, an element found

                Hence the element 6 is found at index 2.

---

---

## 02. Binary Search: Find Closest Number

    Binary Search: Find Closest Number
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

## 03. Binary Search: Find Fixed Point

    Binary Search: Find Fixed Point
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

## 04. Binary Search: Find Bitonic Peak

    Binary Search: Find Bitonic Peak
    Define a bitonic sequence as a sequence of integers such that:
        x_1 <= ... <= x_k >= ... >= x_n-1 for some k, 0 <= k < n.

    For example:
        1, 2, 3, 4, 5, 4, 3, 2, 1

    is a bitcoin sequence. write a program to find the largest element in
    such a sequence. In the above example, the program should return "5".

    we assume that such a peak element exists.

---

---

## 05. Binary Search: Find First Entry in List with Duplicates

    Binary Search: Find First Entry in List with Duplicates
    writing a function that takes an array of sorted integers and a key and returns the index of the first
    occurrence of that key from the array.

    Example:
        Index:      0   1   2   3    4    5    6    7    8    9
        Array:   [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
        Target:  108

        Returns index 3 since 108 appear for the first time at index 3.

---

---

## 06. Binary Search: Python's Bisect Method

    Binary Search: Python's Bisect Method

    Bisect:
        -"Built-in" binary search method in Python.
        -Can be used to search for an element in a sorted list.

---

---

## 07. Binary Search: Integer Square Root

    Binary Search: Integer Square Root
    write a function that takes a non-negative integer and returns the largest integer whose square is less
    than or equal to the integer given:

    Example:

        Assume input is integer 300.

        Then the expected output of the function should be 17 since 17 squared is 289 which is strictly less than 300. Note that 18 squared is 324 which is strictly greater than 300, so the number 17 is the correct response.

---

---

## 08. Binary Search: Cyclically Shifted Array

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

## 09. Binary Search: Find Index Of All Occurances

```bash
Binary Search: Find Index Of All Occurances
Now since the list is sorted,

It can do left and right scan from the initial index to find all occurances of a given element.

Example:
A sortedd array

                data = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
                target = 15

Here, we have the target element 15
so, we have to find how many 15 are there in data list

index number starts from 0

Three 15 are there in the data list at respective index number

                Indices of occurences of number 15 are [5, 6, 7]
```

---

---

## 10. Binary Search: Search in Rotated Sorted Array

[Leetcode Problem URL](https://leetcode.com/problems/search-in-rotated-sorted-array/)

You are given an integer array `nums` sorted in ascending order, but possibly **rotated at an unknown pivot index `k`** such that:

```
Original Sorted Array:    [0, 1, 2, 4, 5, 6, 7]
After Rotation at index 3: [4, 5, 6, 7, 0, 1, 2]
```

Given a rotated sorted array `nums` and an integer `target`, return the **index** of `target` if it is in `nums`, or `-1` if it is not.

**You must solve it in O(log n) time complexity.**

Constraints

- All elements in the array are **distinct**
- Time complexity must be **O(log n)**

Input Format

- `nums`: list of integers (rotated sorted array)
- `target`: integer to be searched

Output Format

- Return the **index** of the `target` in `nums`, or `-1` if it is not present

```bash
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

```bash
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

```bash
Example 3:

Input: nums = [1], target = 0
Output: -1
```

### Explanation

Since the array is **sorted but rotated**, a normal binary search won't work directly. However, at least one half (left or right) of the array will **always remain sorted**.

#### Key Insight:

At each iteration:

- Either the **left half** (`nums[l]` to `nums[mid]`) is sorted
- Or the **right half** (`nums[mid]` to `nums[r]`) is sorted

By checking which half is sorted, and whether the target falls within the sorted range, we can **adjust our search range** accordingly.

#### Algorithm Steps

1. Initialize two pointers `l = 0` and `r = len(nums) - 1`
2. While `l <= r`:

   - Calculate `mid = (l + r) // 2`
   - If `nums[mid] == target`, return `mid`
   - Check if **left portion is sorted**:

     - If `nums[l] <= nums[mid]`:

       - If `target` lies within `[nums[l], nums[mid]]`, search left: `r = mid - 1`
       - Else, search right: `l = mid + 1`

   - Else (**right portion is sorted**):

     - If `target` lies within `[nums[mid], nums[r]]`, search right: `l = mid + 1`
     - Else, search left: `r = mid - 1`

3. If not found, return `-1`

### Example Walkthrough

1. Example

   ```python
   Input: nums = [4,5,6,7,0,1,2], target = 0
   ```

2. Initial State:

   ```
   l = 0, r = 6
   ```

3. Iteration 1:

   ```
   mid = (0 + 6) // 2 = 3
   nums[mid] = 7
   nums[l] = 4 → nums[l] <= nums[mid] → Left half [4,5,6,7] is sorted

   target = 0 not in [4,7] → search right
   l = mid + 1 = 4
   ```

4. Iteration 2:

   ```
   l = 4, r = 6
   mid = (4 + 6) // 2 = 5
   nums[mid] = 1
   nums[l] = 0 → nums[l] <= nums[mid] → Left half [0,1] is sorted

   target = 0 ∈ [0,1] → search left
   r = mid - 1 = 4
   ```

5. Iteration 3:

   ```
   l = 4, r = 4
   mid = (4 + 4) // 2 = 4
   nums[mid] = 0 == target → return 4
   ```

#### Time and Space Complexity

| Metric           | Complexity | Justification                                  |
| ---------------- | ---------- | ---------------------------------------------- |
| Time Complexity  | O(log n)   | Binary search over a modified condition        |
| Space Complexity | O(1)       | Constant space usage, no recursion or extra DS |

#### Why This Approach?

- **Brute-force** (linear search): O(n) — unacceptable for large input
- **Normal binary search** fails because of rotation
- **Modified binary search** leverages the fact that one half of the array is always sorted, reducing the search space **logarithmically**

This makes the solution optimal and meets the required time complexity of `O(log n)`.

---

---

## 10. Binary Search: Search in Rotated Sorted Array

[Problem from Languify Interview Platform](https://interview.languify.in/)

Given a sorted array `A` with a size of `N`, determine the number of elements that are less than or equal to `B`.

NOTE: The expected time complexity is `O(log N)`.

```bash
Example 1:

A = [1, 3, 4, 4, 6]
B = 4
Output:
4
```

```bash
Example 2:

A = [1, 2, 5, 5]
B = 3
Output:
2
```

### Explanation

#### Intuition

Since the array is **sorted**, this problem reduces to a **variant of binary search**. We need to find the **rightmost index** where the element is less than or equal to `B`. The number of such elements will be the **index** itself when `0-based indexing` is used — or more precisely, the **count** of all elements ≤ `B`.

#### Approach

I've used a **binary search** to efficiently find the number of elements in `A` that are ≤ `B`:

- Maintain two pointers: `left = 0` and `right = len(A)`
- Run a loop while `left < right`
- Calculate the middle index `mid = (left + right) // 2`
- If `A[mid] <= B`, move the `left` boundary rightward (`left = mid + 1`)
- Else, move the `right` boundary leftward (`right = mid`)
- The final value of `left` will be the number of elements ≤ `B`

#### Example Walkthrough

1. Let's take the **second example**:

   ```python
   A = [1, 2, 5, 5]
   B = 3
   ```

   - We want to find how many elements in A are less than or equal to 3.

2. Initial State:

   ```
   left = 0
   right = 4  (length of A)
   ```

3. Iteration 1:

   ```
   mid = (0 + 4) // 2 = 2
   A[mid] = 5 > 3 → Move right
   right = mid = 2
   ```

4. Iteration 2:

   ```
   mid = (0 + 2) // 2 = 1
   A[mid] = 2 ≤ 3 → Move left
   left = mid + 1 = 2
   ```

   - Now `left == right == 2` → Exit loop.

5. Final Output:

   ```
   Result = 2 → elements [1, 2] are ≤ 3
   ```

#### Time and Space Complexity

| Metric           | Complexity   | Justification                                               |
| ---------------- | ------------ | ----------------------------------------------------------- |
| Time Complexity  | **O(log N)** | Binary search narrows the search space in logarithmic steps |
| Space Complexity | **O(1)**     | Constant space used; no auxiliary data structures involved  |

#### Why This Approach?

- **Sorted Array + Counting Problem** → Naturally suited for **binary search**
- **Optimal Time Complexity**: Brute-force would require O(N), but binary search reduces it to O(log N)
- **Final Answer = Index of first number > B**, which is exactly what binary search finds

---

---
