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

- `one = 1`: This represents the number of ways to reach the zero'th step.
- `two = 1`: This represents the number of ways to reach the first step.

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

### 02. House Robber

[Leetcode Problem URL](https://leetcode.com/problems/house-robber/description/)

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

You are given an integer array `nums` where `nums[i]` represents the amount of money the `i`th house has. The houses are arranged in a straight line, i.e. the `i`th house is the neighbor of the `(i-1)`th and `(i+1)`th house.

Return the maximum amount of money you can rob without alerting the police.

```bash
Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

```bash
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
```

**Explanation**

1. **Approach**:

   - Use two variables, `rob1` and `rob2`, to keep track of the maximum amount of money that can be robbed up to the previous house and the house before the previous house, respectively.
   - Iterate through each house and determine whether to rob the current house or skip it.

2. **Dynamic Programming Transition**:
   - For each house `i`, we have two choices:
     1. Rob the current house and add its money to `rob1` (the amount robbed up to the house before the previous house).
     2. Skip the current house and carry forward `rob2` (the amount robbed up to the previous house).
   - Update `rob2` to be the maximum of these two choices.

#### Example Walkthrough

Let's walk through the example `nums = [2,7,9,3,1]` step by step:

1. **Initialization**:

   - `rob1 = 0`, `rob2 = 0`

2. **House 1 (Amount = 2)**:

   - `newRob = max(2 + 0, 0) = 2`
   - Update `rob1 = rob2 = 0`
   - Update `rob2 = newRob = 2`

3. **House 2 (Amount = 7)**:

   - `newRob = max(7 + 0, 2) = 7`
   - Update `rob1 = rob2 = 2`
   - Update `rob2 = newRob = 7`

4. **House 3 (Amount = 9)**:

   - `newRob = max(9 + 2, 7) = 11`
   - Update `rob1 = rob2 = 7`
   - Update `rob2 = newRob = 11`

5. **House 4 (Amount = 3)**:

   - `newRob = max(3 + 7, 11) = 11`
   - Update `rob1 = rob2 = 11`
   - Update `rob2 = newRob = 11`

6. **House 5 (Amount = 1)**:
   - `newRob = max(1 + 11, 11) = 12`
   - Update `rob1 = rob2 = 11`
   - Update `rob2 = newRob = 12`

#### Final Result

The maximum amount of money that can be robbed without alerting the police is `12`.

#### Efficiency Analysis

- **Time Complexity**: $O(n)$, where `n` is the number of houses. We iterate through the list of houses once.
- **Space Complexity**: $O(1)$, as we only use a constant amount of space for `rob1` and `rob2`.

### 03. House Robber II

[Leetcode Problem URL](https://leetcode.com/problems/house-robber-ii/description/)

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

You are given an integer array `nums` where `nums[i]` represents the amount of money the `i`th house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

Return the maximum amount of money you can rob without alerting the police.

```bash
Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
```

```bash
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

```bash
Example 3:

Input: nums = [1,2,3]
Output: 3
```

**Explanation**

The problem is an extension of the "House Robber I" problem with an additional constraint that the houses are arranged in a circle. This means we cannot rob both the first and last houses simultaneously.

1. **Approach**:
   - I've split the problem into two subproblems:
     1. Rob houses from the first house to the second-last house.
     2. Rob houses from the second house to the last house.
   - The reason I've split the problem this way is to avoid the situation where both the first and last houses are robbed.
   - The final solution is the maximum of these two subproblems.

#### Example Walkthrough

Let's walk through the example `nums = [2, 3, 2]` step by step:

1. **Initialization**:

   - We need to consider two cases:
     - Case 1: Rob houses from the first house to the second-last house: `nums[:-1] = [2, 3]`
     - Case 2: Rob houses from the second house to the last house: `nums[1:] = [3, 2]`

2. **Case 1 (`nums = [2, 3]`)**:

   - Initialize `rob1 = 0`, `rob2 = 0`
   - House 1 (Amount = 2):
     - `newRob = max(0 + 2, 0) = 2`
     - Update `rob1 = 0`, `rob2 = 2`
   - House 2 (Amount = 3):
     - `newRob = max(0 + 3, 2) = 3`
     - Update `rob1 = 2`, `rob2 = 3`
   - Maximum for this case: `3`

3. **Case 2 (`nums = [3, 2]`)**:
   - Initialize `rob1 = 0`, `rob2 = 0`
   - House 1 (Amount = 3):
     - `newRob = max(0 + 3, 0) = 3`
     - Update `rob1 = 0`, `rob2 = 3`
   - House 2 (Amount = 2):
     - `newRob = max(0 + 2, 3) = 3`
     - Update `rob1 = 3`, `rob2 = 3`
   - Maximum for this case: `3`

#### Final Result

The maximum amount of money that can be robbed without alerting the police is the maximum of the two cases: `max(3, 3) = 3`.

#### Efficiency Analysis

- **Time Complexity**: $O(n)$, where `n` is the number of houses. We iterate through the list of houses twice (once for each subproblem).
- **Space Complexity**: $O(1)$, as we only use a constant amount of space for `rob1` and `rob2`.

### 04. Longest Palindromic Substring

[Leetcode Problem URL](https://leetcode.com/problems/longest-palindromic-substring/description/)

Given a string `s`, return the longest substring of `s` that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.

```bash
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

```bash
Example 2:

Input: s = "cbbd"
Output: "bb"
```

**Explanation**

To solve the problem of finding the longest palindromic substring, I've used a two-pointer approach to expand around the center.

1. **Approach**:

   - For each character in the string, consider it as the center of a potential palindrome.
   - Expand outwards from the center and check for the longest palindrome.
   - We need to consider both odd-length and even-length palindromes.

2. **Helper Function**:

   - We create a helper function `checkPalindrome` that takes two pointers `left` and `right`, and expands outwards as long as the characters at these pointers are the same.
   - When the characters at `left` and `right` are no longer the same, the function returns the substring between `left + 1` and `right`.

3. **Main Function**:

   - Initialize an empty string `resString` to store the longest palindrome found.
   - Iterate through each character in the string:
     - For each character, use it as the center for an odd-length palindrome and an even-length palindrome by calling `checkPalindrome`.
     - Update `resString` if a longer palindrome is found.

#### Example Walkthrough

Let's walk through the example `s = "babad"` step by step:

1. **Initialization**:

   - `resString = ""`

2. **Iteration**:

   - For `i = 0` (Character 'b'):

     - Check odd-length palindrome centered at 'b': `"b"`
     - Check even-length palindrome centered between 'b' and 'a': `""`
     - Update `resString` to `"b"`

   - For `i = 1` (Character 'a'):

     - Check odd-length palindrome centered at 'a': `"bab"`
     - Check even-length palindrome centered between 'a' and 'b': `""`
     - Update `resString` to `"bab"`

   - For `i = 2` (Character 'b'):

     - Check odd-length palindrome centered at 'b': `"aba"`
     - Check even-length palindrome centered between 'b' and 'a': `""`
     - `resString` remains `"bab"`

   - For `i = 3` (Character 'a'):

     - Check odd-length palindrome centered at 'a': `"a"`
     - Check even-length palindrome centered between 'a' and 'd': `""`
     - `resString` remains `"bab"`

   - For `i = 4` (Character 'd'):
     - Check odd-length palindrome centered at 'd': `"d"`
     - Check even-length palindrome centered after 'd': `""`
     - `resString` remains `"bab"`

#### Efficiency Analysis

- **Time Complexity**: $O(n^2)$, where `n` is the length of the string. We expand around each center in the string, and in the worst case, each expansion can take up to `n` steps.
- **Space Complexity**: $O(1)$, since we only use a constant amount of additional space for variables.
