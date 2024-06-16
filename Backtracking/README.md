# Data-Structures And Algorithms

### 01. Combination Sum

[Leetcode Problem URL](https://leetcode.com/problems/combination-sum/description/)

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

```bash
Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
```

```bash
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
```

```bash
Example 3:

Input: candidates = [2], target = 1
Output: []
```

**Explanation**

#### 1. Initialize the Result List

- **Purpose**: To store all the unique combinations that sum up to the target.
- **Action**: Create an empty list `res` to store the result combinations.

#### 2. Depth-First Search (DFS) Function

- **Purpose**: To explore all possible combinations of the candidates that sum up to the target.
- **Action**:
  - Define a nested helper function `dfs` that takes three parameters:
    - `i`: the current index in the candidates list.
    - `cur`: the current combination of numbers being considered.
    - `total`: the current sum of the numbers in the combination.

#### 3. Base Cases in DFS

- **Purpose**: To determine when to stop the recursion.
- **Action**:
  - **Combination Found**: If `total` equals `target`, add a copy of `cur` to the result list `res` and return.
  - **Exceeded Limits**: If `i` is out of bounds (greater than or equal to the length of candidates) or `total` exceeds `target`, return to backtrack.

#### 4. Recursion in DFS

- **Purpose**: To explore the inclusion and exclusion of each candidate number.
- **Action**:
  - **Include the Current Candidate**:
    - Append the current candidate (candidates[i]) to `cur`.
    - Recursively call `dfs` with the same index `i` (since the same number can be used multiple times) and update the `total` by adding the current candidate's value.
  - **Exclude the Current Candidate**:
    - Remove the last number added to `cur` to backtrack.
    - Recursively call `dfs` with the next index `i + 1` to explore the next candidate.

#### 5. Call DFS from the Main Function

- **Purpose**: To initiate the recursive exploration.
- **Action**: Start the DFS with the initial index `0`, an empty list `cur`, and a `total` of `0`.

#### 6. Return the Result List

- **Purpose**: To provide the final list of combinations that sum up to the target.
- **Action**: Return the result list `res` containing all valid combinations.

#### Example Usage

- Demonstrates the usage of the `combinationSum` function by creating an instance of the `Solution` class.
- Calls the `combinationSum` function with different sets of candidates and targets.
- Prints the results to verify the correct combinations are found.

#### Efficiency

- The time complexity of the solution is $O(2^t)$, where `t` is the target value. This accounts for the exponential number of possible combinations that can be formed with the given candidates.

### 02. Word Search

[Leetcode Problem URL](https://leetcode.com/problems/word-search/description/)

Given an `m` x `n` grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

![example 1](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)

```bash
Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
```

![example 2](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)

```bash
Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
```

![example 3](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)

```bash
Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

**Explanation**

The problem can be solved using Depth-First Search (DFS) with backtracking. The idea is to start from each cell in the grid and explore all possible paths to check if the word can be formed.

#### Steps

Sure! Here's a detailed Explanation of the solution for the Word Search problem, step by step, along with an analysis of its efficiency.

### Problem Summary

Given an `m` x `n` grid of characters (`board`) and a string (`word`), determine if the word can be constructed from letters of sequentially adjacent cells in the grid. Adjacent cells can be horizontally or vertically neighboring, and the same letter cell may not be used more than once.

### Approach

The problem can be solved using Depth-First Search (DFS) with backtracking. The idea is to start from each cell in the grid and explore all possible paths to check if the word can be formed.

### Steps

1. **Initialize Variables:**

   - `rows` and `cols` store the dimensions of the board.
   - `path` is a set to keep track of visited cells during the DFS to avoid reusing the same cell.

2. **Define the DFS Function:**

   - The `dfs` function takes the current cell position `(row, col)` and the current index `i` of the word we are matching.
   - Base Case: If `i` equals the length of the word, it means we have successfully matched all characters in the word, so we return `True`.
   - Boundary and Validity Check: If the current cell is out of bounds, or the character at the current cell does not match the current character of the word, or the cell has already been visited, return `False`.
   - Mark the current cell as visited by adding it to `path`.
   - Recursively call `dfs` for the neighboring cells (down, up, right, left).
   - Unmark the current cell by removing it from `path` before returning from the function.

3. **Start DFS from Each Cell:**

   - Iterate through each cell in the grid.
   - If `dfs` returns `True` for any starting cell, return `True` immediately as the word exists in the grid.

4. **Return False if Word Not Found:**
   - If none of the cells lead to the formation of the word, return `False`.

#### Explanation with Examples

**Example 1:**

- **Input:** `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`, `word = "ABCCED"`
- **Output:** `True`
- **Explanation:** The path "ABCCED" can be formed from the board starting from cell (0, 0) and following the path right → right → down → left → down.

**Example 2:**

- **Input:** `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`, `word = "SEE"`
- **Output:** `True`
- **Explanation:** The path "SEE" can be formed from the board starting from cell (2, 1) and following the path right → right.

**Example 3:**

- **Input:** `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`, `word = "ABCB"`
- **Output:** `False`
- **Explanation:** There is no path in the board that forms the word "ABCB" without reusing a cell.

#### Efficiency Analysis

- **Time Complexity:**

  - The worst-case time complexity is $(O(m \times n \times 4^L))$, where `m` is the number of rows, `n` is the number of columns, and `L` is the length of the word.
  - This is because in the worst case, each cell initiates a DFS that explores all 4 possible directions up to the length of the word.

- **Space Complexity:**
  - The space complexity is $(O(L))$, where `L` is the length of the word.
  - This space is used by the recursion stack and the `path` set to keep track of visited cells.

This solution effectively combines DFS with backtracking to explore all possible paths in the grid, ensuring that the word is found if it exists.
