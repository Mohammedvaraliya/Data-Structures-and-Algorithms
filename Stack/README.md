# Stack Data-Structures and Algorithms

## 01. The Stack data Structure

    Stack Data Structure
    Stack is FILO(First In Last Out) or LIFO(Last In First Out) Data structure

       | D |
       | C |
       | B |
       | A |
       -----

    Example:
    This is stack

            |   |
            -----

    When you push() an element 'A' to stack
    stack will look like

                        | A |
                        -----

    Now if you push() some more elements, it will place one above one
    final stack:

                | D |
                | C |
                | B |
                | A |
                -----

    When you pop() the element from stack, it will pop() from top of the stack or the recent pushed element

                | C |
                | B |
                | A |
                -----

---

## 02. The Stack data Structure : Understanding Stack

    The Stack data Structure : Understanding Stack
    deque is using Doubly Linked List data structure to store the element.

    Stack is FILO(First In Last Out) or LIFO(Last In First Out) Data structure

       | D |
       | C |
       | B |
       | A |
       -----

    Example:
    This is stack

            |   |
            -----

    When you push() an element 'A' to stack
    stack will look like

                        | A |
                        -----

    Now if you push() some more elements, it will place one above one
    final stack:

                | D |
                | C |
                | B |
                | A |
                -----

    When you pop() the element from stack, it will pop() from top of the stack or the recent pushed element

                | C |
                | B |
                | A |
                -----

---

## 03. Determine if parenthesis are balanced

[Leetcode Problem URL](https://leetcode.com/problems/valid-parentheses/)

```bash
Determine if parenthesis are balanced
Use a stack to check whether or not a string has
balanced usage of parenthesis.

Example:
    (), ()(), (({{[]}})) <== Balanced.
    ((),  {{{)}], [][]]] <== Not Balanced.

Balanced Example: {[]}

Non-Balanced Example: (()

Non-Balanced Example: ]]

Problem Statement :
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
```

## 04. Convert integer to binary

    Convert integer to binary
    Use a stack data structure to convert integer values to binary.

    Example : 242

    242 / 2 = 121 -> 0    # 0 is a remainder as number is even
    121 / 2 = 60  -> 1    # 1 is a remainder as number is odd
    60 / 2  = 30  -> 0    # 0 is a remainder as number is even
    30 / 2  = 15  -> 0    # 0 is a remainder as number is even
    15 / 2  = 7   -> 1    # 1 is a remainder as number is odd
    7 / 2   = 3   -> 1    # 1 is a remainder as number is odd
    3 / 2   = 1   -> 1    # 1 is a remainder as number is odd
    1 / 2   = 0   -> 1    # 1 is a remainder as number is odd

    11110010 is the binary number of integer 242

---

## 05. The Stack data Structure : Reverse String

    The Stack data Structure : Reverse String
    It will return the reverse string from given string.

    Example:
            str = "You can do it."
        output:
                .ti od nac uoY

    First push() all the characters from str to stack.

    declare an empty string variable

    Now, pop() characters one by one and add it to an empty string variable

    return empty string variable

---
