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

#### Approach: Subtract Smaller Before Larger

We iterate over the Roman numeral string and compare **current value with previous value**:

- If **current > previous**, it means a subtractive pattern (`IV`, `IX`, etc.), so we **subtract twice the previous** because it was already added once.
- Otherwise, we just **add current** to total.

#### Step-by-Step Walkthrough (Example: `"MCMXCIV"`)

Let's walk through the input `s = "MCMXCIV"`:

| Iteration | Char | curr | prev | Condition          | Action                    | total |
| --------- | ---- | ---- | ---- | ------------------ | ------------------------- | ----- |
| 0         | M    | 1000 | 0    | 1000 > 0 (True)    | total += 1000 - 0         | 1000  |
| 1         | C    | 100  | 1000 | 100 < 1000 (False) | total += 100              | 1100  |
| 2         | M    | 1000 | 100  | 1000 > 100 (True)  | total += 1000 - 2×100=800 | 1900  |
| 3         | X    | 10   | 1000 | 10 < 1000 (False)  | total += 10               | 1910  |
| 4         | C    | 100  | 10   | 100 > 10 (True)    | total += 100 - 2×10=80    | 1990  |
| 5         | I    | 1    | 100  | 1 < 100 (False)    | total += 1                | 1991  |
| 6         | V    | 5    | 1    | 5 > 1 (True)       | total += 5 - 2×1 = 3      | 1994  |

**Final Output:** `1994`

#### Time and Space Complexity

| Metric           | Value    | Explanation                                            |
| ---------------- | -------- | ------------------------------------------------------ |
| Time Complexity  | **O(n)** | Single pass over string `s`                            |
| Space Complexity | **O(1)** | Only constant extra space for dictionary and variables |

#### Why This Approach Works

- We avoid using multiple conditionals for specific substrings (`"IV"`, `"CM"`, etc.).
- Instead, we generalize the rule: _If a smaller numeral comes before a larger one, subtract it twice_ (since we already added it once).
- This leads to a **clean, readable**, and **efficient** $O(n)$ solution.

#### Pattern Recognition for Similar Problems

This pattern can be used in problems involving:

- **Symbol-to-value mappings**
- **Comparing adjacent elements** (current vs. previous/next)
- Situations where **implicit rules** (like subtraction when a smaller comes before a larger) affect logic

Look for:

- Mapping structures (`dict`)
- Iteration with state tracking (`prev`)
- Conditional logic involving previous and current values

---

---
