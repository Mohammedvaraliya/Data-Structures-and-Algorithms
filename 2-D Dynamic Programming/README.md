# 2-D Dynamic Programming Data-Structures and Algorithms

## 01. Unique Paths

[Leetcode Problem URL](https://leetcode.com/problems/unique-paths/description/)

There is a robot on an `m x n` grid. The robot is initially located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to the bottom-right corner (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to `2 * 109`.

![Example-1](https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png)

```bash
Example 1:

Input: m = 3, n = 7
Output: 28
```

```bash
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
```

### Explanation

To solve this problem, I've used dynamic programming (DP). The idea is to break down the problem into smaller subproblems and solve them. We create a DP array where each element `dp[i][j]` represents the number of unique paths to reach the cell `(i, j)` from the top-left corner.

You're right. The initialization should indeed refer to the last row, given that the solution is implemented in a bottom-up way. Let's correct that and provide the detailed explanation accordingly.

#### Detailed Steps

1. **Initialization**:

   - Initialize a 1D DP array `row` of size `n` with all elements set to 1. This array represents the number of ways to reach each cell in the last row, which is always 1 because there is only one way to move right to reach any cell in the last row.

2. **Filling the DP Table**:

   - Iterate over the rows of the grid starting from the second last row up to the first row.
   - For each row, create a new DP array `newRow` of size `n` initialized to 1.
   - Iterate over the columns of the current row from right to left. For each cell `(i, j)`, update `newRow[j]` to be the sum of `newRow[j+1]` (number of ways to reach the cell to the right) and `row[j]` (number of ways to reach the cell below).
   - Update `row` to be `newRow` after processing each row.

3. **Result**:

   - The answer is found in `row[0]`, which represents the number of unique paths to reach the bottom-right corner from the top-left corner.

#### Example Walkthrough

Let's walk through the example `m = 3`, `n = 7`:

1. **Initialization**:

   - `row = [1, 1, 1, 1, 1, 1, 1]`

2. **Iteration**:

   - For the first row iteration (`i = 1`):
     - `newRow = [1, 1, 1, 1, 1, 1, 1]`
     - For `j = 5` to `0`:
       - `newRow[5] = newRow[6] + row[5] = 1 + 1 = 2`
       - `newRow[4] = newRow[5] + row[4] = 2 + 1 = 3`
       - `newRow[3] = newRow[4] + row[3] = 3 + 1 = 4`
       - `newRow[2] = newRow[3] + row[2] = 4 + 1 = 5`
       - `newRow[1] = newRow[2] + row[1] = 5 + 1 = 6`
       - `newRow[0] = newRow[1] + row[0] = 6 + 1 = 7`
     - Update `row` to `newRow`
   - For the second row iteration (`i = 0`):
     - `newRow = [1, 1, 1, 1, 1, 1, 1]`
     - For `j = 5` to `0`:
       - `newRow[5] = newRow[6] + row[5] = 1 + 2 = 3`
       - `newRow[4] = newRow[5] + row[4] = 3 + 3 = 6`
       - `newRow[3] = newRow[4] + row[3] = 6 + 4 = 10`
       - `newRow[2] = newRow[3] + row[2] = 10 + 5 = 15`
       - `newRow[1] = newRow[2] + row[1] = 15 + 6 = 21`
       - `newRow[0] = newRow[1] + row[0] = 21 + 7 = 28`
     - Update `row` to `newRow`

3. **Result**:

   - The final `row` is `[28, 21, 15, 10, 6, 3, 1]`
   - `row[0]` is `28`, which is the number of unique paths from the top-left to the bottom-right corner.

#### Efficiency Analysis

- **Time Complexity**: $O(m \cdot n)$, where `m` is the number of rows and `n` is the number of columns. We iterate through each cell of the grid once.
- **Space Complexity**: $O(n)$, where `n` is the number of columns. We use a 1D DP array of size `n` to store the number of unique paths.

## 02. Longest Common Subsequence

[Leetcode Problem URL](https://leetcode.com/problems/longest-common-subsequence/description/)

Given two strings `text1` and `text2`, return the length of their longest common subsequence. If there is no common subsequence, return `0`.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

A common subsequence of two strings is a subsequence that is common to both strings.

```bash
Example 1:

   Example matrix
   [[0, 0, 0, 0],
   [0, 0, 0, 0],
   [0, 0, 0, 0],
   [0, 0, 0, 0],
   [0, 0, 0, 0],
   [0, 0, 0, 0]]

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
```

```bash
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
```

```bash
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
```

### Explanation

This problem can be solved using dynamic programming. The idea is to create a 2D table `dp` where `dp[i][j]` represents the length of the longest common subsequence of the substrings `text1[0:i]` and `text2[0:j]`.

1. **DP Table Initialization**:

   - We initialize a 2D list `dp` with dimensions `(len(text1) + 1) x (len(text2) + 1)` filled with 0s. This table will help us store the lengths of LCS for substrings of `text1` and `text2`.
   - The extra row and column are to handle the case when either string is empty, in which case the LCS length is 0.

2. **Filling the DP Table**:

   - We start filling the table from the bottom-right corner.
   - For each pair of indices `i` and `j`, if the characters `text1[i]` and `text2[j]` match, then `dp[i][j]` is `1 + dp[i + 1][j + 1]`, because the current character can be included in the LCS.
   - If the characters don't match, we take the maximum value between `dp[i + 1][j]` and `dp[i][j + 1]`, which represents skipping one of the characters in either `text1` or `text2`.

3. **Result**:
   - After filling the table, the top-left corner `dp[0][0]` contains the length of the longest common subsequence of the two strings.

#### Example Walkthrough

Let's go through the example `"abcde"` and `"ace"` in detail to understand how we can find the length of the longest common subsequence (LCS) step by step.

- **Iteration 1**:

  - Start with `i = 4` and `j = 2` (Comparing `text1[4] = "e"` with `text2[2] = "e"`)
  - The characters match (`"e" == "e"`).
  - Update `dp[4][2] = 1 + dp[5][3] = 1 + 0 = 1`.
  - The updated `dp` table:

    ```
    dp = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0]]
    ```

- **Iteration 2**:

  - We move to `i = 4` and `j = 1` (comparing `text1[4] = "e"` with `text2[1] = "c"`).
  - The characters do not match (`"e" != "c"`), so we cannot include this character in our common subsequence.
  - To decide the value of `dp[4][1]`, we look at the right cell `dp[4][2]` and the cell below `dp[5][1]`.
    - `dp[4][2]` gives us the LCS length if we skip the current character in `text2`.
    - `dp[5][1]` gives us the LCS length if we skip the current character in `text1`.
  - We take the maximum of these two values: `dp[4][1] = max(dp[4][2], dp[5][1]) = max(1, 0) = 1`.
  - This means that up to this point, the maximum LCS length considering these two characters remains 1.
  - The updated `dp` table is:

    ```
    dp = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 1, 1, 0],
          [0, 0, 0, 0]]
    ```

- **Iteration 3**:

  - Move to `i = 4` and `j = 0` (Comparing `text1[4] = "e"` with `text2[0] = "a"`)
  - The characters do not match (`"e" != "a"`).
  - Update `dp[4][0] = max(dp[4][1], dp[5][0]) = max(1, 0) = 1`.
  - The updated `dp` table:

    ```
    dp = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]]
    ```

- **Iteration 4**:

  - Move to `i = 3` and `j = 2` (Comparing `text1[3] = "d"` with `text2[2] = "e"`)
  - The characters do not match (`"d" != "e"`).
  - Update `dp[3][2] = max(dp[3][3], dp[4][2]) = max(0, 1) = 1`.
  - The updated `dp` table:

    ```
    dp = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]]
    ```

- **Iteration 5**:

  - Move to `i = 3` and `j = 1` (Comparing `text1[3] = "d"` with `text2[1] = "c"`)
  - The characters do not match (`"d" != "c"`).
  - Update `dp[3][1] = max(dp[3][2], dp[4][1]) = max(1, 1) = 1`.
  - The updated `dp` table:

    ```
    dp = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 1, 1, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]]
    ```

- **Iteration 6**:

  - Move to `i = 3` and `j = 0` (Comparing `text1[3] = "d"` with `text2[0] = "a"`)
  - The characters do not match (`"d" != "a"`).
  - Update `dp[3][0] = max(dp[3][1], dp[4][0]) = max(1, 1) = 1`.
  - The updated `dp` table:

    ```
    dp = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [1, 1, 1, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]]
    ```

- **Iteration 7**:

  - Move to `i = 2` and `j = 2` (Comparing `text1[2] = "c"` with `text2[2] = "e"`)
  - The characters do not match (`"c" != "e"`).
  - Update `dp[2][2] = max(dp[2][3], dp[3][2]) = max(0, 1) = 1`.
  - The updated `dp` table:

    ```
    dp = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0],
          [1, 1, 1, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]]
    ```

- **Iteration 8**:

  - Move to `i = 2` and `j = 1` (Comparing `text1[2] = "c"` with `text2[1] = "c"`)
  - The characters match (`"c" == "c"`).
  - Update `dp[2][1] = 1 + dp[3][2] = 1 + 1 = 2`.
  - The updated `dp` table:

    ```
    dp = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 2, 1, 0],
          [1, 1, 1, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]]
    ```

- **Iteration 9**:

  - Move to `i = 2` and `j = 0` (Comparing `text1[2] = "c"` with `text2[0] = "a"`)
  - The characters do not match (`"c" != "a"`).
  - Update `dp[2][0] = max(dp[2][1], dp[3][0]) = max(2, 1) = 2`.
  - The updated `dp` table:

    ```
    dp = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [2, 2, 1, 0],
          [1, 1, 1, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]]
    ```

- **Iteration 10**:

  - Move to `i = 1` and `j = 2` (Comparing `text1[1] = "b"` with `text2[2] = "e"`)
  - The characters do not match (`"b" != "e"`).
  - Update `dp[1][2] = max(dp[1][3], dp[2][2]) = max(0, 1) = 1`.
  - The updated `dp` table:

    ```
    dp = [[0, 0, 0, 0],
          [0, 0, 1, 0],
          [2, 2, 1, 0],
          [1, 1, 1, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]]
    ```

- **Iteration 11**:

  - Move to `i = 1` and `j = 1` (Comparing `text1[1] = "b"` with `text2[1] = "c"`)
  - The characters do not match (`"b" != "c"`).
  - Update `dp[1][1] = max(dp[1][2], dp[2][1]) = max(1, 2) = 2`.
  - The updated `dp` table:

    ```
    dp = [[0, 0, 0, 0],
          [0, 2, 1, 0],
          [2, 2, 1, 0],
          [1, 1, 1, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]]
    ```

- **Iteration 12**:

  - Move to `i = 1` and `j = 0` (Comparing `text1[1] = "b"` with `text2[0] = "a"`)
  - The characters do not match (`"b" != "a"`).
  - Update `dp[1][0] = max(dp[1][1], dp[2][0]) = max(2, 2) = 2`.
  - The updated `dp` table:

    ```
    dp = [[0, 0, 0, 0],
          [2, 2, 1, 0],
          [2, 2, 1, 0],
          [1, 1, 1, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]]
    ```

- **Iteration 13**:

  - Move to `i = 0` and `j = 2` (Comparing `text1[0] = "a"` with `text2[2] = "e"`)
  - The characters do not match (`"a" != "e"`).
  - Update `dp[0][2] = max(dp[0][3], dp[1][2]) = max(0, 1) = 1`.
  - The updated `dp` table:

    ```
    dp = [[0, 0, 1, 0],
          [2, 2, 1, 0],
          [2, 2, 1, 0],
          [1, 1, 1, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]]
    ```

- **Iteration 14**:

  - Move to `i = 0` and `j = 1` (Comparing `text1[0] = "a"` with `text2[1] = "c"`)
  - The characters do not match (`"a" != "c"`).
  - Update `dp[0][1] = max(dp[0][2], dp[1][1]) = max(1, 2) = 2`.
  - The updated `dp` table:

    ```
    dp = [[0, 2, 1, 0],
          [2, 2, 1, 0],
          [2, 2, 1, 0],
          [1, 1, 1, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]]
    ```

- **Iteration 15**:

  - Move to `i = 0` and `j = 0` (Comparing `text1[0] = "a"` with `text2[0] = "a"`)
  - The characters match (`"a" == "a"`).
  - Update `dp[0][0] = 1 + dp[1][1] = 1 + 2 = 3`.
  - The final `dp` table:

    ```
    dp = [[3, 2, 1, 0],
          [2, 2, 1, 0],
          [2, 2, 1, 0],
          [1, 1, 1, 0],
          [1, 1, 1, 0],
          [0, 0, 0, 0]]
    ```

##### Result:

- The value at `dp[0][0]` is `3`, which is the length of the longest common subsequence between `text1 = "abcde"` and `text2 = "ace"`.

#### Efficiency Analysis

- **Time Complexity**: $O(m \times n)$, where `m` is the length of `text1` and `n` is the length of `text2`.
  - We need to fill a 2D table of size `m x n`.
- **Space Complexity**: $O(m \times n)$.
  - We use a 2D table to store the lengths of the longest common subsequence for each pair of indices.
