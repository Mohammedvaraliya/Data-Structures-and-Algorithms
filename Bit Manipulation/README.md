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
