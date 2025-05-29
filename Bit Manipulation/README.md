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
