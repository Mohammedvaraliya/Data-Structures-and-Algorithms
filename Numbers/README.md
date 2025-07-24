# Numbers Data-Structures and Algorithms

## 01. Product of Two Numbers

    Product of Two Numbers
    Given two numbers, find their product using recursion.

    Example:
            x = 5
            y = 4

    x * y = 20

    using recursion:
    addition of x with y times
    It means:
            x = 5
            y = 4

    5 + 5 + 5 + 5 = 20

---

---

## 02. Numbers: Convert Integer To Binary

    Numbers: Convert Integer To Binary Number
    The algorithm works by repeatedly doubling a variable power until it is greater than the integer n.
    It then divides power by 2 to get the largest power of 2 less than n.
    This value of power is used to determine which digits in the binary representation should be set to 1.

    The algorithm then repeatedly divides power by 2 and checks if the current value of power is less than or equal to n.
    If it is, the algorithm subtracts power from n and adds a "1" to the binary representation.
    If it is not, the algorithm adds a "0" to the binary representation.
    This process continues until power becomes 0, at which point the binary representation is complete.

    Example:

                n = 10
                power = 1
                result = ""

        Everytime double the power varibale until the n is greater
        power = 2
        power = 4
        power = 8

        check if the number is less than or equal to n
        if yes
        add "1" to the result string
        otherwise add "0"

                        int :    8   4   2    1
                        result:  1   0   1    0

        final binary string is : "1010" of integer 10

---

---

## 03. Numbers: Convert Binary To Integer

        Numbers: Convert Binary To Integer
        Initialize a variable result to 0.
        This will be used to store the integer representation of the binary number.

        Initialize a variable power to 1.
        This will be used to keep track of the current power of 2.

        Initialize a variable i to the length of the binary number minus 1.
        This will be used as an index to iterate through the binary number from least significant digit to most significant digit.

        While i is greater than or equal to 0, do the following:

                If the i-th digit of the binary number is 1, add power to result.
                Multiply power by 2.
                Decrement i by 1.
                Return result as the integer representation of the binary number.

        Example:

                bunary_number = "1010"

                result = 0
                power = 1
                i = len(binary_number) - 1
            i.e i = 4 - 1
                i = 3

                While i is greater than or equal to 0, do the following:

                ----->  if the number at index bunary_number[i] is 1 so:
                                add the value of power to result
                                i.e result = 0 + 1
                                    result = 1

                        And make the power double:
                        i.e power = 1*1
                            power = 2
                        and decrement the value of i so we get all the indexes
                        i = 3 - 1
                        i = 2

                ----->  Now check again

                        if the number at index bunary_number[i] is 1 so:
                                add the value of power to result
                                i.e result = 1 + 2
                                    result = 3

                        And make the power double:
                        i.e power = 2*2
                            power = 4
                        and decrement the value of i so we get all the indexes
                        i = 2 - 1
                        i = 1

                ----->  Now check again

                        if the number at index bunary_number[i] is 0 so:

                        make the power double:
                        i.e power = 4*2
                            power = 8
                        and decrement the value of i so we get all the indexes
                        i = 1 - 1
                        i = 0

                ----->  Now check again

                        if the number at index bunary_number[i] is 1 so:
                                add the value of power to result
                                i.e result = 3 + 8
                                    result = 11


                return reseult
                The integer of binary number 1011 is 11

---

---

## 04. Roman to Integer

[LeetCode Problem URL](https://leetcode.com/problems/roman-to-integer/)

Roman numerals are represented by seven symbols:

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are written from **largest to smallest** from **left to right**. However, when a **smaller value precedes a larger one**, it is **subtracted**. For example:

- `IV = 4` → `5 - 1`
- `IX = 9` → `10 - 1`
- `XL = 40`, `XC = 90`
- `CD = 400`, `CM = 900`

Given a string `s` representing a Roman numeral, return its corresponding **integer value**.

```bash
Example 1:
Input: s = "III"
Output: 3
Explanation: III = 1 + 1 + 1 = 3
```

```bash
Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3 → 50 + 5 + 3 = 58
```

```bash
Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90, IV = 4 → 1000 + 900 + 90 + 4 = 1994
```

### Explanation

This problem can be solved using a **greedy algorithm** by iterating through the string and applying the rules of Roman numeral subtraction directly.

We solve this problem using **two different approaches**, both based on **greedy traversal** patterns.

1. **Method 1: Left-to-Right Traversal with Previous Comparison**

   1. Logic

      - We iterate over the string from **left to right**.
      - At each step, compare the current symbol's value with the **previous** symbol's value:

      - If **current ≤ previous** → Add it normally.
      - If **current > previous** → This indicates a **subtractive combination** (e.g., IV, IX).

      - We subtract `2 * prev` because:

      - The previous value was **already added once**.
      - We need to subtract **both that previous addition** and the **actual difference**.

   2. Why This Works

      This logic directly **handles subtractive patterns** inline without the need for substring detection.

   3. Pattern Used

      This uses a **greedy** traversal pattern with **comparative state tracking** (`prev`).

1. **Method 2: Right-to-Left Traversal with Reversal Logic**

   1. Logic

      - We traverse the string **from right to left**.
      - At each step, compare the **current value** with the **last processed (previous) value**:

      - If current < previous → subtract it.
      - Else → add it.

   2. Why This Works

      Roman numeral subtraction only happens when **a smaller value precedes a larger one**. Reversing the traversal simplifies the detection of this pattern.

   3. Pattern Used

      Also a **greedy** approach, optimized by **reverse traversal**.

#### Step-by-Step Walkthroughs

1. Example 1: `"MCM"` using Method 1 for understanding why `curr - 2 * prev` is used.

   ```text
   Input: "MCM"
   Expected Output: 1900
   ```

2. Roman Breakdown:

   | Index | Char | Value | Prev | Current > Prev? | Action                          | Total |
   | ----- | ---- | ----- | ---- | --------------- | ------------------------------- | ----- |
   | 0     | M    | 1000  | 0    | Yes             | total += 1000                   | 1000  |
   | 1     | C    | 100   | 1000 | No              | total += 100                    | 1100  |
   | 2     | M    | 1000  | 100  | Yes             | total += (1000 - 2 × 100) = 800 | 1900  |

3. Why `curr - 2 * prev`?

   - When we added `C`, we added +100.
   - But now we see `M` (1000) after `C` (100), which means it's a subtractive pair (`CM = 900`).
   - So we **remove the 100 added before** and instead **add 900 (1000 - 100)**.
   - That's effectively `total += 1000 - 2 * 100 = 800` to **correct** the previously added 100.

4. Example 2: `"MCMXCIV"` using Method 1

   ```text
   Input: "MCMXCIV"
   Expected Output: 1994
   ```

5. Roman Breakdown:

   | Index | Char | Value | Prev | Condition  | Calculation                     | Total |
   | ----- | ---- | ----- | ---- | ---------- | ------------------------------- | ----- |
   | 0     | M    | 1000  | 0    | 1000 > 0   | total += 1000                   | 1000  |
   | 1     | C    | 100   | 1000 | 100 < 1000 | total += 100                    | 1100  |
   | 2     | M    | 1000  | 100  | 1000 > 100 | total += (1000 - 2 × 100) = 800 | 1900  |
   | 3     | X    | 10    | 1000 | 10 < 1000  | total += 10                     | 1910  |
   | 4     | C    | 100   | 10   | 100 > 10   | total += (100 - 2 × 10) = 80    | 1990  |
   | 5     | I    | 1     | 100  | 1 < 100    | total += 1                      | 1991  |
   | 6     | V    | 5     | 1    | 5 > 1      | total += (5 - 2 × 1) = 3        | 1994  |

6. Example 3: `"MCMXCIV"` using Method 2 (Right to Left)

   - Start from `'V'` and go backwards:

   | Index | Char | Value | Prev_Value | Condition  | Action        | Total |
   | ----- | ---- | ----- | ---------- | ---------- | ------------- | ----- |
   | 6     | V    | 5     | 0          | 5 ≥ 0      | total += 5    | 5     |
   | 5     | I    | 1     | 5          | 1 < 5      | total -= 1    | 4     |
   | 4     | C    | 100   | 1          | 100 ≥ 1    | total += 100  | 104   |
   | 3     | X    | 10    | 100        | 10 < 100   | total -= 10   | 94    |
   | 2     | M    | 1000  | 10         | 1000 ≥ 10  | total += 1000 | 1094  |
   | 1     | C    | 100   | 1000       | 100 < 1000 | total -= 100  | 994   |
   | 0     | M    | 1000  | 100        | 1000 ≥ 100 | total += 1000 | 1994  |

#### Time and Space Complexity

| Method   | Time Complexity | Explanation                    | Space Complexity | Explanation                                 |
| -------- | --------------- | ------------------------------ | ---------------- | ------------------------------------------- |
| Method 1 | $O(n)$          | Single pass from left to right | O(1)             | Only a fixed map and few variables are used |
| Method 2 | $O(n)$          | Single pass from right to left | O(1)             | Only a fixed map and few variables are used |

> `n` = length of the input string `s`

---

---

## 05. Integer to Roman

[LeetCode Problem URL](https://leetcode.com/problems/integer-to-roman/)

Seven different symbols represent Roman numerals with the following values:

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

- If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
- If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
- Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
  Given an integer, convert it to a Roman numeral.

```bash
Example 1:

Input: num = 3749

Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
```

```bash
Example 2:

Input: num = 58

Output: "LVIII"

Explanation:

50 = L
 8 = VIII
```

```bash
Example 3:

Input: num = 1994

Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 =   XC
   4 = IV
```

### Explanation

This problem can be solved using a **greedy algorithm** by always subtracting the **largest possible Roman value** from the number until it becomes zero.

1. Why This Approach?

   This problem can be solved using a **greedy strategy** by always subtracting the **largest possible Roman value** from the number until it becomes zero.

2. Problem-Solving Pattern

   - **Greedy Algorithm**: At each step, pick the largest Roman symbol that does not exceed the current number.
   - No dynamic programming, recursion, or advanced data structures are needed.
   - Iterative reduction using pre-defined mapping of integer values to symbols.

3. Efficiency and Elegance

   - Simple to implement.
   - Covers both regular and subtractive Roman numeral rules.
   - Ensures minimal and correct Roman numeral output without trial-and-error.

#### Step-by-Step Walkthrough

1.  Let’s walk through the example:

2.  **Input:** `num = 3749`
3.  **Goal:** Convert to Roman numeral

4.  We use the ordered list:

    ```python
    value_symbols = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
        (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    ```

5.  Now let's trace how the algorithm processes `num = 3749`:

    | Iteration | Value | Symbol | Count | Subtracted | Result     | Remaining Num |
    | --------- | ----- | ------ | ----- | ---------- | ---------- | ------------- |
    | 1         | 1000  | M      | 3     | 3000       | MMM        | 749           |
    | 2         | 500   | D      | 1     | 500        | MMMD       | 249           |
    | 3         | 100   | C      | 2     | 200        | MMMDCC     | 49            |
    | 4         | 40    | XL     | 1     | 40         | MMMDCCXL   | 9             |
    | 5         | 9     | IX     | 1     | 9          | MMMDCCXLIX | 0             |

6.  **Final Output:** `MMMDCCXLIX`

#### Time and Space Complexity

| Metric               | Complexity | Explanation                                                              |
| -------------------- | ---------- | ------------------------------------------------------------------------ |
| **Time Complexity**  | $O(1)$     | The number of iterations is bounded by a constant (13 symbols in total). |
| **Space Complexity** | $O(1)$     | Only a few variables and a result list of bounded size are used.         |

#### Summary

- The greedy algorithm fits naturally for Roman numeral conversion.
- By starting from the highest value symbol and working downward, we ensure both correctness and efficiency.
- The code is compact, readable, and logically complete.
- This problem demonstrates effective use of mapping, iteration, and string construction.

---

---
