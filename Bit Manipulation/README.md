# Bit Manipulation

## 01. Number of 1 Bits

[Leetcode Problem URL](https://leetcode.com/problems/number-of-1-bits/)

Given a positive integer `n`, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

```bash
Example 1:

Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.
```

```bash
Example 2:

Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.
```

```bash
Example 3:

Input: n = 2147483645
Output: 30
Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.
```

### Explanation

I've solved this problem using two methods:

1. **Method 1**: Modulo and Division

   - We repeatedly divide `n` by `2` and add `1` to the result each time we encounter an odd number (i.e., `n % 2 == 1`, which means the least significant bit is `1`).

   - Code

     ```python
     def hammingWeight_method1(self, n: int) -> int:
         res = 0
         while n:
             res += n % 2
             n = n // 2
         return res
     ```

   - Step-by-Step Walkthrough (n = 11)

     1. Binary representation of 11 is: `1011`

        | Iteration |   n | n % 2 | res | Updated n |
        | --------: | --: | ----: | --: | --------: |
        |         1 |  11 |     1 |   1 |         5 |
        |         2 |   5 |     1 |   2 |         2 |
        |         3 |   2 |     0 |   2 |         1 |
        |         4 |   1 |     1 |   3 |         0 |

     2. Final result: `res = 3`

2. **Method 2**: Brian Kernighan’s Algorithm (Optimized Bit Manipulation)

   - This method subtracts `1` from `n` and performs `n = n & (n-1)` in each iteration. This clears the **rightmost set bit**. We increment `res` for every operation until `n` becomes `0`.

   - Code

     ```python
     def hammingWeight_method2(self, n: int) -> int:
         res = 0
         while n:
             n &= (n - 1)
             res += 1
         return res
     ```

   - Step-by-Step Walkthrough (n = 11)

     1. Binary representation of 11 is: `1011`

        | Iteration | n (binary) | n-1 (binary) | n & (n-1) result | res |
        | --------- | ---------- | ------------ | ---------------- | --- |
        | 1         | 1011 (11)  | 1010 (10)    | 1010 (10)        | 1   |
        | 2         | 1010 (10)  | 1001 (9)     | 1000 (8)         | 2   |
        | 3         | 1000 (8)   | 0111 (7)     | 0000 (0)         | 3   |

     2. Final result: `res = 3`

#### Why These Approaches?

1. **Method 1**: Simple and Easy to Understand

   - This method mimics converting a number to binary and counting the `1`s.
   - It is intuitive and works well for learning the concept of bitwise operations.
   - However, it processes **all bits** even if most of them are zero.

2. Method 2: Efficient and Optimized

   - Brian Kernighan’s method is significantly faster for sparse bit representations.
   - It only loops for the number of set bits.
   - Ideal for large integers with fewer set bits.

#### Time and Space Complexity

| Method                   | Time Complexity | Space Complexity | Notes                                                                  |
| ------------------------ | --------------- | ---------------- | ---------------------------------------------------------------------- |
| Modulo & Division        | O(1)            | O(1)             | Maximum 32 iterations (since `n` is a 32-bit integer).                 |
| Brian Kernighan's Method | O(1)            | O(1)             | At most 32 iterations; faster in practice when `n` has fewer set bits. |

---

---

## 02. Counting Bits

[Leetcode Problem URL](https://leetcode.com/problems/number-of-1-bits/)

Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` `(0 <= i <= n)`, `ans[i]` is the number of `1`'s in the binary representation of `i`.

```bash
Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
```

```bash
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
```

### Explanation

#### Method Used: **Dynamic Programming + Bit Offset Pattern**

#### Why This Approach?

1. **Efficiency**: Instead of calculating set bits from scratch for every number, I've used a previously computed result to compute the current result in constant time.
2. **Optimal Substructure**: If we know the number of 1's in a number `i`, then we can use that to compute the result of a number derived from `i` using powers of 2.
3. **Avoids Repeated Computation**: Reduces redundancy by reusing answers we’ve already computed.

#### Key Insight Behind the Approach

For any number `i`:

- Let `offset` be the largest power of 2 less than or equal to `i`.
- Then:
  `countBits[i] = 1 + countBits[i - offset]`
  Why? Because:

  - `offset` has exactly one set bit.
  - `i - offset` has already been computed and stored.

#### Step-by-Step Explanation

1. Initialization

   - We define an array `dp` of size `n + 1` initialized to all `0s`.
   - The variable `offset` is used to keep track of the current power of two.
   - Start with `offset = 1`.

#### Example Walkthrough: `n = 5`

We want to compute the number of `1` bits in binary representation of all numbers from `0` to `5`.

1. Initialization:

   ```python
   dp = [0, 0, 0, 0, 0, 0]  # size = 6
   offset = 1
   ```

2. Iteration 1: `i = 1`

   - `offset * 2 = 2 != i` → no change in offset
   - `dp[1] = 1 + dp[1 - 1] = 1 + dp[0] = 1`

     ```python
     dp = [0, 1, 0, 0, 0, 0]
     ```

3. Iteration 2: `i = 2`

   - `offset * 2 = 2 == i` → update `offset = 2`
   - `dp[2] = 1 + dp[2 - 2] = 1 + dp[0] = 1`

     ```python
     dp = [0, 1, 1, 0, 0, 0]
     ```

4. Iteration 3: `i = 3`

   - `offset * 2 = 4 != i`
   - `dp[3] = 1 + dp[3 - 2] = 1 + dp[1] = 2`

     ```python
     dp = [0, 1, 1, 2, 0, 0]
     ```

5. Iteration 4: `i = 4`

   - `offset * 2 = 4 == i` → update `offset = 4`
   - `dp[4] = 1 + dp[4 - 4] = 1 + dp[0] = 1`

     ```python
     dp = [0, 1, 1, 2, 1, 0]
     ```

6. Iteration 5: `i = 5`

   - `offset * 2 = 8 != i`
   - `dp[5] = 1 + dp[5 - 4] = 1 + dp[1] = 2`

     ```python
     dp = [0, 1, 1, 2, 1, 2]
     ```

7. Final Output

   ```python
   [0, 1, 1, 2, 1, 2]
   ```

#### Time and Space Complexity

| Method                      | Time Complexity | Space Complexity | Notes                                                        |
| --------------------------- | --------------- | ---------------- | ------------------------------------------------------------ |
| DP with Offset Optimization | $O(n)$          | $O(n)$           | Each element is computed once using previously known values. |

#### Why This is Efficient

1. **Avoids Bitwise Operations Per Number**: Traditional methods might require `O(log i)` operations per `i` to count bits.
2. **Uses Precomputed Results**: Every new result builds directly on a smaller result with a single additional `1` bit.
3. **Linear Time**: Every number is processed exactly once in the loop.
4. **Scalable**: Can handle large values of `n` efficiently up to the constraint limits.

---

---

## 03. Reverse Bits

[Leetcode Problem URL](https://leetcode.com/problems/reverse-bits/)

Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.

In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in **Example 2** above, the input represents the signed integer `-3` and the output represents the signed integer `-1073741825`.

```bash
Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
```

```bash
Example 2:

Input: n = 11111111111111111111111111111101
Output:   3221225471 (10111111111111111111111111111111)
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
```

### Explanation

We need to reverse the bits of a number. That is, bit at position 0 becomes bit at position 31, bit at position 1 becomes bit at position 30, and so on.

To achieve this, we follow these steps:

1. Initialize result `res = 0`
2. Loop for all 32 bits `i = 0` to `31`:

   - Extract the `i-th` bit from `n` using: `(n >> i) & 1`
   - Place that bit in the `(31 - i)`-th position in `res`: `res = res | (bit << (31 - i))`

3. Return the final `res`

#### Step-by-Step Bit Manipulation Walkthrough (Example 1)

1. Let’s dry-run the solution for:

   ```python
   n = 43261596
   # Binary: 00000010100101000001111010011100
   ```

2. We initialize:

   ```
   res = 0
   ```

3. We loop from i = 0 to 31:

   | Iteration (i) | Extracted Bit `(n >> i) & 1` | New Bit Position in `res` (31 - i) | `res` (in binary)                |
   | ------------- | ---------------------------- | ---------------------------------- | -------------------------------- |
   | 0             | 0                            | 31                                 | 00000000000000000000000000000000 |
   | 1             | 0                            | 30                                 | 00000000000000000000000000000000 |
   | 2             | 1                            | 29                                 | 00100000000000000000000000000000 |
   | 3             | 1                            | 28                                 | 00110000000000000000000000000000 |
   | 4             | 1                            | 27                                 | 00111000000000000000000000000000 |
   | 5             | 0                            | 26                                 | 00111000000000000000000000000000 |
   | 6             | 0                            | 25                                 | 00111000000000000000000000000000 |
   | 7             | 1                            | 24                                 | 00111001000000000000000000000000 |
   | 8             | 0                            | 23                                 | 00111001000000000000000000000000 |
   | 9             | 1                            | 22                                 | 00111001010000000000000000000000 |
   | 10            | 0                            | 21                                 | 00111001010000000000000000000000 |
   | 11            | 1                            | 20                                 | 00111001010100000000000000000000 |
   | 12            | 0                            | 19                                 | 00111001010100000000000000000000 |
   | 13            | 0                            | 18                                 | 00111001010100000000000000000000 |
   | 14            | 1                            | 17                                 | 00111001010101000000000000000000 |
   | 15            | 0                            | 16                                 | 00111001010101000000000000000000 |
   | 16            | 0                            | 15                                 | 00111001010101000000000000000000 |
   | 17            | 0                            | 14                                 | 00111001010101000000000000000000 |
   | 18            | 0                            | 13                                 | 00111001010101000000000000000000 |
   | 19            | 1                            | 12                                 | 00111001010101000100000000000000 |
   | 20            | 0                            | 11                                 | 00111001010101000100000000000000 |
   | 21            | 1                            | 10                                 | 00111001010101000101000000000000 |
   | 22            | 0                            | 9                                  | 00111001010101000101000000000000 |
   | 23            | 0                            | 8                                  | 00111001010101000101000000000000 |
   | 24            | 0                            | 7                                  | 00111001010101000101000000000000 |
   | 25            | 0                            | 6                                  | 00111001010101000101000000000000 |
   | 26            | 0                            | 5                                  | 00111001010101000101000000000000 |
   | 27            | 0                            | 4                                  | 00111001010101000101000000000000 |
   | 28            | 0                            | 3                                  | 00111001010101000101000000000000 |
   | 29            | 0                            | 2                                  | 00111001010101000101000000000000 |
   | 30            | 0                            | 1                                  | 00111001010101000101000000000000 |
   | 31            | 0                            | 0                                  | 00111001010101000101000000000000 |

4. Final binary value: `00111001011110000010100101000000` Decimal value: `964176192`

5. This matches the expected output.

#### Time and Space Complexity

| Metric           | Value          | Explanation                                        |
| ---------------- | -------------- | -------------------------------------------------- |
| Time Complexity  | $O(32) → O(1)$ | Always runs for 32 iterations regardless of input  |
| Space Complexity | $O(1)$         | No extra space used except constant-size variables |

#### Why This Approach?

- Bit manipulation is the most **efficient and direct way** to reverse binary digits.
- Other approaches (e.g., converting to a string, reversing, and parsing) are **less performant** and use **extra space**.
- This approach guarantees **constant time and space**, which is optimal for fixed 32-bit integer problems.

#### Key Learnings

- Use `bit = (n >> i) & 1` to extract the `i-th` bit from a number.
- Use `res = res | (bit << (31 - i))` to place the bit at its reversed position.
- Think in terms of **bit positions** rather than number values when working with bit-level problems.

---

---

## 04. Missing Number

[Leetcode Problem URL](https://leetcode.com/problems/missing-number/)

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

```bash
Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
```

```bash
Example 2:

Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
```

```bash
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
```

### Explanation

I've implemented **two efficient approaches** to solve this problem:

1. **Approach 1: Mathematical Sum Formula**

   - The sum of first `n` natural numbers:

   $$
   \text{expected\_sum} = \frac{n \cdot (n + 1)}{2}
   $$

   - Subtract the actual sum of elements in the array from the expected sum:

   $$
   \text{missing\_number} = \text{expected\_sum} - \text{actual\_sum}
   $$

   - But I've used an optimized way:

     $$
     res = n + (0 - nums[0]) + (1 - nums[1]) + \dots + (n-1 - nums[n-1])
     $$

2. **Approach 2: Bit Manipulation (Using XOR)**

   - XOR of a number with itself is 0: `x ^ x = 0`
   - XOR of a number with 0 is the number itself: `x ^ 0 = x`
   - XOR all numbers from 0 to n with all elements in the array:

     $$
     \text{missing} = (0 \oplus 1 \oplus 2 \dots \oplus n) \oplus (\text{nums[0]} \oplus \text{nums[1]} \oplus \dots)
     $$

   - All matching numbers cancel out, leaving only the missing number.

#### Step-by-Step Example Walkthrough

1. We’ll use **Example 3**:

   ```python
   nums = [9,6,4,2,3,5,7,0,1]
   Expected Output: 8
   ```

2. **Walkthrough for Method 1 (Mathematical)**

   - Initial:

     ```
     res = len(nums) = 9
     ```

     | Iteration (i) | nums\[i] | i - nums\[i] | res updated    |
     | ------------- | -------- | ------------ | -------------- |
     | 0             | 9        | 0 - 9 = -9   | 9 + (-9) = 0   |
     | 1             | 6        | 1 - 6 = -5   | 0 + (-5) = -5  |
     | 2             | 4        | 2 - 4 = -2   | -5 + (-2) = -7 |
     | 3             | 2        | 3 - 2 = 1    | -7 + 1 = -6    |
     | 4             | 3        | 4 - 3 = 1    | -6 + 1 = -5    |
     | 5             | 5        | 5 - 5 = 0    | -5 + 0 = -5    |
     | 6             | 7        | 6 - 7 = -1   | -5 + (-1) = -6 |
     | 7             | 0        | 7 - 0 = 7    | -6 + 7 = 1     |
     | 8             | 1        | 8 - 1 = 7    | 1 + 7 = 8      |

   - **Final Answer: 8**

3. **Walkthrough for Method 2 (Bit Manipulation using XOR)**

   - Initial:

     ```
     n = 9
     xorr = 9
     ```

     | Iteration (i) | nums\[i] | i ^ nums\[i] | xorr (updated) |
     | ------------- | -------- | ------------ | -------------- |
     | 0             | 9        | 0 ^ 9 = 9    | 9 ^ 9 = 0      |
     | 1             | 6        | 1 ^ 6 = 7    | 0 ^ 7 = 7      |
     | 2             | 4        | 2 ^ 4 = 6    | 7 ^ 6 = 1      |
     | 3             | 2        | 3 ^ 2 = 1    | 1 ^ 1 = 0      |
     | 4             | 3        | 4 ^ 3 = 7    | 0 ^ 7 = 7      |
     | 5             | 5        | 5 ^ 5 = 0    | 7 ^ 0 = 7      |
     | 6             | 7        | 6 ^ 7 = 1    | 7 ^ 1 = 6      |
     | 7             | 0        | 7 ^ 0 = 7    | 6 ^ 7 = 1      |
     | 8             | 1        | 8 ^ 1 = 9    | 1 ^ 9 = 8      |

   - **Final Answer: 8**

#### Time & Space Complexity Analysis

| Approach       | Time Complexity | Space Complexity | Explanation                             |
| -------------- | --------------- | ---------------- | --------------------------------------- |
| Method 1 (Sum) | $O(n)$          | $O(1)$           | Single loop of size `n`, constant space |
| Method 2 (XOR) | $O(n)$          | $O(1)$           | Single loop with XORs, constant space   |

#### Why These Approaches Are Efficient

1. **Method 1**:

   - Avoids sorting or extra memory
   - Constant-time arithmetic inside loop
   - No need for a full sum formula if prone to overflow

2. **Method 2**:

   - XOR operation is extremely fast and lightweight
   - No risk of integer overflow (which can happen with sum formula)
   - Cancels out duplicates naturally, finding the missing number efficiently

---

---
