# 1-D Dynamic Programming Data-Structures and Algorithms

### 01. Climbing Stairs

[Leetcode Problem URL](https://leetcode.com/problems/climbing-stairs/description/)

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

```bash
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

```bash
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

**Explanation**

The number of ways to reach the nth step is the sum of the number of ways to reach the (n-1)th step and the (n-2)th step. This is because we can either take a single step from (n-1) to n or a double step from (n-2) to n.

This approach resembles the Fibonacci sequence where each number is the sum of the two preceding ones.

1. **Base Cases**:

   - If `n` is 1, there's only one way to climb the staircase: taking a single step.
   - If `n` is 2, there are two ways to climb the staircase: (1 step + 1 step) or (2 steps).

2. **Initialization**:

   - We initialize two variables, `one` and `two`, both set to 1. These represent the number of ways to reach the first step and the second step, respectively.

3. **Iterative Calculation**:

   - We use a loop to iterate from the 3rd step up to the nth step.
   - In each iteration, we update the `one` and `two` variables. `one` is updated to the sum of `one` and `two` (the number of ways to reach the current step), and `two` is updated to the old value of `one`.

4. **Result**:
   - After completing the loop, `one` contains the number of distinct ways to climb to the nth step.

#### Example Walkthrough with \( n = 5 \)

We need to find the number of distinct ways to climb a staircase with 5 steps, where each step can be either 1 step or 2 steps at a time.

##### Initialization

We start with two variables:

- `one = 1`: This represents the number of ways to reach the first step.
- `two = 1`: This represents the number of ways to reach the second step.

##### Iterative Calculation

We will use a loop to update these variables until we reach the 5th step.

1. **Step 3**:

   - **Current state**: `one = 1`, `two = 1`
   - **Calculation**: `one = one + two` (number of ways to reach the 2nd step)
   - `one = 1 + 1 = 2`
   - **Update**: `two` is now the old value of `one`
   - `two = 1`
   - **New state**: `one = 2`, `two = 1`

2. **Step 4**:

   - **Current state**: `one = 2`, `two = 1`
   - **Calculation**: `one = one + two` (number of ways to reach the 3rd step)
   - `one = 2 + 1 = 3`
   - **Update**: `two` is now the old value of `one`
   - `two = 2`
   - **New state**: `one = 3`, `two = 2`

3. **Step 5**:

   - **Current state**: `one = 3`, `two = 2`
   - **Calculation**: `one = one + two` (number of ways to reach the 4th step)
   - `one = 3 + 2 = 5`
   - **Update**: `two` is now the old value of `one`
   - `two = 3`
   - **New state**: `one = 5`, `two = 3`

4. **Step 6**:
   - **Current state**: `one = 5`, `two = 3`
   - **Calculation**: `one = one + two` (number of ways to reach the 5th step)
   - `one = 5 + 3 = 8`
   - **Update**: `two` is now the old value of `one`
   - `two = 5`
   - **New state**: `one = 8`, `two = 5`

##### Result

After the loop completes, the variable `one` contains the number of distinct ways to reach the 5th step, which is 8.

#### Efficiency Analysis

**Time Complexity**:

- The time complexity is $O(n)$ because we use a single loop that runs from 1 to $n-1$.

**Space Complexity**:

- The space complexity is $O(1)$ because we only use a fixed amount of space (two variables, `one` and `two`), regardless of the input size $n$.
