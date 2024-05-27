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

**Explaination**

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

### Example Usage

- Demonstrates the usage of the `combinationSum` function by creating an instance of the `Solution` class.
- Calls the `combinationSum` function with different sets of candidates and targets.
- Prints the results to verify the correct combinations are found.

### Efficiency

- The time complexity of the solution is $O(2^t)$, where `t` is the target value. This accounts for the exponential number of possible combinations that can be formed with the given candidates.
