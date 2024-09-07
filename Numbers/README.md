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

## 04. Roman to Integer

[Leetcode Problem URL](https://leetcode.com/problems/roman-to-integer/)

```bash
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol Value
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

---
