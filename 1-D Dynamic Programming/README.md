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

4. **Clarification on Odd and Even Length Palindromes**:

   - Odd-Length Palindromes:
     - We start with the same index for both left and right, i.e., `left = i` and `right = i`.
     - For example, starting at index 0, we would have `left = 0` and `right = 0`.
     - As we expand, we decrement left by 1 and increment right by 1, creating palindromes of length 3, 5, 7, and so on.
   - Even-Length Palindromes:
     - We start with adjacent indices for `left` and `right`, i.e., `left = i` and `right = i + 1`.
     - For example, starting at index 0, we would have `left = 0` and `right = 1`.
     - As we expand, we decrement left by 1 and increment right by 1, creating palindromes of length 2, 4, 6, 8, and so on.

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

### 05. Palindromic Substrings

[Leetcode Problem URL](https://leetcode.com/problems/longest-palindromic-substring/description/)

Given a string `s`, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

````bash
Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".


```bash
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
````

**Explanation**

To solve the problem of counting palindromic substrings, I've used a two-pointer approach to expand around the center.

1. **Approach**:

   - For each character in the string, consider it as the center of a potential palindrome.
   - Expand outwards from the center and count all palindromes.
   - We need to consider both odd-length and even-length palindromes.

2. **Helper Function**:

   - We create a helper function `countPalindrome` that takes two pointers `left` and `right`, and expands outwards as long as the characters at these pointers are the same.
   - It returns the count of palindromic substrings found during the expansion.

3. **Main Function**:

   - Initialize a variable `res` to store the total count of palindromic substrings.
   - Iterate through each character in the string:
     - For each character, use it as the center for an odd-length palindrome and an even-length palindrome by calling `countPalindrome`.
     - Add the counts returned by `countPalindrome` to `res`.

4. **Clarification on Odd and Even Length Palindromes**:

   - **Odd-Length Palindromes**:
     - We start with the same index for both left and right, i.e., `left = i` and `right = i`.
     - For example, starting at index 0, we would have `left = 0` and `right = 0`.
     - As we expand, we decrement `left` by 1 and increment `right` by 1, creating palindromes of length 1, 3, 5, and so on.
   - **Even-Length Palindromes**:
     - We start with adjacent indices for left and right, i.e., `left = i` and `right = i + 1`.
     - For example, starting at index 0, we would have `left = 0` and `right = 1`.
     - As we expand, we decrement `left` by 1 and increment `right` by 1, creating palindromes of length 2, 4, 6, and so on.

#### Example Walkthrough

Let's walk through the example `s = "aaa"` step by step:

1. **Initialization**:

   - `res = 0`

2. **Iteration**:

   - For `i = 0` (Character 'a'):

     - Check odd-length palindrome centered at 'a':
       - `left = 0`, `right = 0`, count = 1 (palindrome: `"a"`)
     - Check even-length palindrome centered between 'a' and 'a':
       - `left = 0`, `right = 1`, count = 1 (palindrome: `"aa"`)
     - Update `res` to `2`

   - For `i = 1` (Character 'a'):

     - Check odd-length palindrome centered at 'a':
       - `left = 1`, `right = 1`, count = 1 (palindrome: `"a"`)
       - `left = 0`, `right = 2`, count = 1 (palindrome: `"aaa"`)
     - Check even-length palindrome centered between 'a' and 'a':
       - `left = 1`, `right = 2`, count = 1 (palindrome: `"aa"`)
     - Update `res` to `5`

   - For `i = 2` (Character 'a'):
     - Check odd-length palindrome centered at 'a':
       - `left = 2`, `right = 2`, count = 1 (palindrome: `"a"`)
     - Check even-length palindrome centered after 'a': No valid palindrome
     - Update `res` to `6`

#### Efficiency Analysis

- **Time Complexity**: $O(n^2)$, where `n` is the length of the string. We expand around each center in the string, and in the worst case, each expansion can take up to `n` steps.
- **Space Complexity**: $O(1)$, since we only use a constant amount of additional space for variables.

### 06. Decode Ways

[Leetcode Problem URL](https://leetcode.com/problems/decode-ways/description/)

A string consisting of uppercase english characters can be encoded to a number using the following mapping:

```bash
'A' -> "1"
'B' -> "2"
...
'Y' -> "25"
'Z' -> "26"
```

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes (`"2"` and `"5"` vs `"25"`).

For example, `"11106"` can be decoded into:

- `"AAJF"` with the grouping `(1, 1, 10, 6)`
- `"KJF"` with the grouping `(11, 10, 6)`
- The grouping `(1, 11, 06)` is invalid because `"06"` is not a valid code (only `"6"` is valid).

Note: there may be strings that are impossible to decode.

Given a string `s` containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return `0`.

The test cases are generated so that the answer fits in a 32-bit integer.

```bash
Example 1:

Input: s = "12"
Output: 2
Explanation:
"12" could be decoded as "AB" (1 2) or "L" (12).
```

```bash
Example 2:

Input: s = "226"
Output: 3
Explanation:
"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

```bash
Example 3:

Input: s = "06"
Output: 0
Explanation:
"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.
```

**Explanation**

To solve the problem of counting the number of ways to decode the string, I've used a dynamic programming with memoization.

1. **Approach**:

   - We will use a recursive approach with memoization to avoid recalculating results for the same subproblems.
   - The recursive function `dfs(i)` will compute the number of ways to decode the substring starting from index `i`.

2. **Base Case**:

   - If the current index `i` is at the end of the string (`i == len(s)`), we have found a valid decoding, so we return 1.

3. **Memoization**:

   - Use a dictionary `dp` to store the results of subproblems. Initialize `dp[len(s)] = 1` because there is one way to decode an empty substring.

4. **Recursive Cases**:

   - If the character at index `i` is '0', it cannot be decoded, so we return 0.
   - Otherwise, compute the result for the single digit decode (`dfs(i + 1)`).
   - If the next two characters form a valid two-digit number (between 10 and 26), add the result of decoding the two digits (`dfs(i + 2)`).

5. **Return the Result**:
   - The result of `dfs(0)` will give the number of ways to decode the entire string `s`.

#### Example Walkthrough: `s = "226"`

1. **Initialization**:

   - We initialize the memoization dictionary `dp` to store results of subproblems. Start with `dp = { len(s): 1 }` which is `dp = { 3: 1 }` since the length of `s` is 3.
   - This means that if we are at the end of the string, there is exactly one way to decode an empty substring.

2. **Recursive Calls**:

   - **Start at index `i = 0`**:

     - `s[0] = '2'`, which is not '0'.
     - Compute `dfs(1)` (decoding the substring starting from index 1).

       - **At index `i = 1`**:

         - `s[1] = '2'`, which is not '0'.
         - Compute `dfs(2)` (decoding the substring starting from index 2).

           - **At index `i = 2`**:

             - `s[2] = '6'`, which is not '0'.
             - Compute `dfs(3)` (decoding the substring starting from index 3).

               - **At index `i = 3`**:
                 - We have reached the end of the string, so return 1 (base case).

             - Back to `i = 2`:

               - `res = 1` (number of ways to decode substring from index 2 is 1, i.e., "6").
               - Store the result in the dictionary: `dp[2] = 1`.

             - Check if `s[1:3]` (i.e., "26") is a valid two-digit decode:

               - It is valid (between 10 and 26).
               - Compute `dfs(3)` again:
                 - **At index `i = 3`**:
                   - We have reached the end of the string, so return 1 (base case).

             - Back to `i = 2`:
               - Add the result: `res += 1` (now `res = 2`).

           - Store the result in the dictionary: `dp[1] = 2`.

         - Back to `i = 0`:

           - `res = 2` (number of ways to decode substring from index 1 is 2).

         - Check if `s[0:2]` (i.e., "22") is a valid two-digit decode:

           - It is valid (between 10 and 26).
           - Compute `dfs(2)` again:
             - **At index `i = 2`**:
               - Retrieve the result from the dictionary: `dp[2] = 1`.

         - Back to `i = 0`:
           - Add the result: `res += 1` (now `res = 3`).

       - Store the result in the dictionary: `dp[0] = 3`.

3. **Final Result**:
   - `dp[0] = 3`, so the number of ways to decode the string "226" is 3.

#### Efficiency Analysis

- **Time Complexity**: $O(n)$, where `n` is the length of the string. We process each character at most once due to memoization.
- **Space Complexity**: $O(n)$, due to the recursion stack and the dictionary `dp` storing the results of subproblems.

### 07. Coin Change

[Leetcode Problem URL](https://leetcode.com/problems/coin-change/description/)

You are given an integer array `coins` representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.

```bash
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
```

```bash
Example 2:

Input: coins = [2], amount = 3
Output: -1
Explanation: The target amount is 3, but it is not possible to achieve this amount with the available coin denomination of 2. Using only the coin of 2 would result in a total of 4, which does not match the required amount of 3. Therefore, the function should return -1.
```

```bash
Example 3:

Input: coins = [1], amount = 0
Output: 0
```

**Explanation**

The idea is to build a solution for the amount from `0` up to the target `amount` by using previously computed results.

1. **Approach**:

   - We create an array `dp` where `dp[i]` represents the fewest number of coins needed to make up the amount `i`.
   - Initialize `dp` with a value greater than the possible amount (`amount + 1`), because the maximum number of coins needed to make up `amount` cannot exceed `amount` (when using the coin `1` only).
   - Set `dp[0]` to `0` because no coins are needed to make the amount `0`.

2. **Dynamic Programming Transition**:

   - For each amount `a` from `1` to `amount`, and for each coin `c` in `coins`:
     - If the current amount `a` is greater than or equal to the coin value `c`, update `dp[a]` to the minimum of its current value or `dp[a - c] + 1`.
     - This ensures that we are using the fewest number of coins needed to make up the amount `a`.

3. **Result**:
   - If `dp[amount]` is still greater than `amount`, it means that it is not possible to make up the amount using the given coins, so return `-1`.
   - Otherwise, return `dp[amount]` as the fewest number of coins needed to make up the amount.

#### Example Walkthrough

Let's walk through the example `coins = [1,2,5]`, `amount = 11` step by step:

1. **Initialization**:

   - `dp = [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]` (since `amount + 1 = 12`)
   - Set `dp[0]` to `0` because zero coins are needed to make the amount `0`.

2. **Filling DP Array**:

   - For `a = 1`:
     - Using coin `1`: `dp[1] = min(dp[1], 1 + dp[0]) = 1` -> `dp = [0, 1, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]`
   - For `a = 2`:
     - Using coin `1`: `dp[2] = min(dp[2], 1 + dp[1]) = 2`
     - Using coin `2`: `dp[2] = min(dp[2], 1 + dp[0]) = 1` -> `dp = [0, 1, 1, 12, 12, 12, 12, 12, 12, 12, 12, 12]`
   - For `a = 3`:
     - Using coin `1`: `dp[3] = min(dp[3], 1 + dp[2]) = 2`
     - Using coin `2`: `dp[3] = min(dp[3], 1 + dp[1]) = 2` -> `dp = [0, 1, 1, 2, 12, 12, 12, 12, 12, 12, 12, 12]`
   - Continue filling the array until `a = 11`:
     - `dp[11] = min(dp[11], 1 + dp[10]) = 3` (using coin `5` twice and coin `1` once)

3. **Result**:
   - The final `dp` array is `[0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]`.
   - The minimum number of coins to make `11` is `3` (`5 + 5 + 1`).

#### Efficiency Analysis

- **Time Complexity**: $O(n \cdot m)$, where `n` is the amount and `m` is the number of coins. This is because for each amount from `1` to `n`, we check all `m` coins.
- **Space Complexity**: $O(n)$, where `n` is the amount. We use an array `dp` of size `n + 1`.

### 08. Maximum Product Subarray

[Leetcode Problem URL](https://leetcode.com/problems/maximum-product-subarray/description/)

Given an integer array `nums`, find a subarray that has the largest product, and return the product.

A subarray is a contiguous non-empty sequence of elements within an array.

The test cases are generated so that the answer will fit in a 32-bit integer.

```bash
Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

```bash
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

**Explanation**

The problem is to find the maximum product of a subarray in the given array `nums`. Due to the possibility of negative numbers and zero, the problem requires careful handling of the product calculations.

1. **Initialization**:

   - We start by initializing the result `res` to the maximum value in the array to handle the edge case where the array might have only one negative number or zero.
   - We also initialize two variables `curMin` and `curMax` to `1`. These will store the minimum and maximum product of the subarray ending at the current position.

2. **Iterate Through the Array**:

   - For each element `n` in `nums`:
     - If `n` is `0`, reset `curMin` and `curMax` to `1` because any subarray that includes `0` will have a product of `0`. Continue to the next element.
     - Calculate the temporary maximum product `tmp` by multiplying `n` with `curMax`.
     - Update `curMax` to the maximum of:
       - `n` multiplied by `curMax` (extending the current maximum product subarray),
       - `n` multiplied by `curMin` (if the current minimum product subarray multiplied by a negative number `n` results in a larger product),
       - `n` itself (starting a new subarray).
     - Update `curMin` to the minimum of:
       - `tmp` (temporary maximum product),
       - `n` multiplied by `curMin` (extending the current minimum product subarray),
       - `n` itself (starting a new subarray).
     - Update the result `res` to the maximum of `res` and `curMax`.

3. **Result**:

   - The maximum product of a subarray is stored in `res`.

#### Example Walkthrough

Let's walk through the example `nums = [2,3,-2,4]` step by step:

1. **Initialization**:

   - `res = max(nums) = 4`
   - `curMin = 1`
   - `curMax = 1`

2. **Iteration**:

   - For `n = 2`:
     - `tmp = 2 * 1 = 2`
     - `curMax = max(2 * 1, 2 * 1, 2) = 2`
     - `curMin = min(2, 2 * 1, 2) = 2`
     - `res = max(4, 2) = 4`
   - For `n = 3`:
     - `tmp = 3 * 2 = 6`
     - `curMax = max(3 * 2, 3 * 2, 3) = 6`
     - `curMin = min(6, 3 * 2, 3) = 3`
     - `res = max(4, 6) = 6`
   - For `n = -2`:
     - `tmp = -2 * 6 = -12`
     - `curMax = max(-2 * 6, -2 * 3, -2) = -2`
     - `curMin = min(-12, -2 * 3, -2) = -12`
     - `res = max(6, -2) = 6`
   - For `n = 4`:
     - `tmp = 4 * -2 = -8`
     - `curMax = max(4 * -2, 4 * -12, 4) = 4`
     - `curMin = min(-8, 4 * -12, 4) = -48`
     - `res = max(6, 4) = 6`

3. **Result**:

   - The final `res` is `6`, which is the maximum product of a subarray in `nums`.

#### Efficiency Analysis

- **Time Complexity**: $O(n)$, where `n` is the length of the array `nums`. We iterate through the array once.
- **Space Complexity**: $O(1)$, constant space. We use only a few variables (`curMin`, `curMax`, and `res`) regardless of the input size.

### 09. Word Break

[Leetcode Problem URL](https://leetcode.com/problems/word-break/description/)

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

```bash
Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

```bash
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
```

```bash
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
```

**Explanation**
