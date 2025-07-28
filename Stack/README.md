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

---

## 03. Valid Parentheses

[Leetcode Problem URL](https://leetcode.com/problems/valid-parentheses/)

Given a string `s` containing just the characters '`(`', '`)`', '`{`', '`}`', '`[`' and '`]`', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

```bash
Example 1:

Input: s = "()"
Output: true
```

```bash
Example 2:

Input: s = "()[]{}"
Output: true
```

```bash
Example 3:

Input: s = "(]"
Output: false
```

```bash
Example 4:

Input: s = "([])"
Output: true
```

### Explanation

#### Approach Explanation

1.  Why This Approach?

    This is a **classic stack-based problem** where we track opening brackets and match them with closing ones using **Last-In-First-Out (LIFO)** behavior. A stack is the most appropriate data structure for such pattern-based validations where **matching and ordering both matter**.

2.  Problem-Solving Pattern Used

    - **Stack** (LIFO)
    - Sometimes grouped under **greedy** or **simulation** patterns, because we simulate bracket closing in real time using stack operations.

3.  Efficiency of This Approach

    - **Optimal use of space**: We only store unmatched opening brackets.
    - **Early exit**: We return `False` as soon as a mismatch is found, avoiding unnecessary computation.
    - **Clean and readable**: The algorithm is concise and intuitive once the pattern is understood.

#### Step-by-Step Walkthrough

1. Let's walk through a complete example using the second approach (`is_paren_balanced_2nd_approach`) as it is more concise and efficient.

2. Input:

   ```python
   s = "({[]})"
   ```

3. Initial Setup:

   ```python
   stack = []
   matching = {')': '(', '}': '{', ']': '['}
   ```

4. Iteration-wise Breakdown:

   | Index | Character | Action                    | Stack             |
   | ----- | --------- | ------------------------- | ----------------- |
   | 0     | '('       | Open bracket → push       | \['(']            |
   | 1     | '{'       | Open bracket → push       | \['(', '{']       |
   | 2     | '\['      | Open bracket → push       | \['(', '{', '\['] |
   | 3     | ']'       | Closing → match with '\[' | \['(', '{']       |
   | 4     | '}'       | Closing → match with '{'  | \['(']            |
   | 5     | ')'       | Closing → match with '('  | \[]               |

5. Final Check:

   - Stack is empty → ✅ All brackets matched correctly.
   - Return `True`

6. Algorithm

   - If a character is a closing bracket:

   - Check if the last item in the stack matches.
   - If yes, pop the top item.
   - If not, return False.

   - If it’s an opening bracket, push it onto the stack.
   - At the end, if the stack is empty, return True.

#### Time and Space Complexity

| Metric               | Complexity | Explanation                                                                         |
| -------------------- | ---------- | ----------------------------------------------------------------------------------- |
| **Time Complexity**  | $O(n)$     | We traverse the input string once (`n` = number of characters in `s`).              |
| **Space Complexity** | $O(n)$     | In the worst case (e.g., all opening brackets), the stack holds all `n` characters. |

#### Summary

- The use of a **stack** makes this problem straightforward and efficient.
- Handles nesting and mixed types of brackets.
- The second approach is highly efficient in practice due to reduced object overhead compared to a custom class-based stack.

---

---

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

---

## 06. The Stack data Structure : Score of Parentheses

[LeetCode Problem URL](https://leetcode.com/problems/score-of-parentheses/)

Given a balanced parentheses string `s`, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

- `"()"` has score `1`.
- `AB` has score `A + B`, where `A` and `B` are balanced parentheses strings.
- `(A)` has score `2 * A`, where `A` is a balanced parentheses string.

```bash
Example 1:

Input: s = "()"
Output: 1
```

```bash
Example 2:

Input: s = "(())"
Output: 2
```

```bash
Example 3:

Input: s = "()()"
Output: 2
```

#### Explanation

This problem requires us to compute the score of a balanced parentheses string based on specific rules. The challenge is to handle nested structures and ensure that scores are aggregated correctly.

#### Approach Explanation

1. Why This Approach?

   This solution uses a **stack** to simulate the structure of the parentheses. The stack helps:

   - Keep track of nested structures.
   - Aggregate scores from child expressions efficiently.
   - Ensure linear time traversal without recursion or complicated parsing.

2. Pattern Used

   - **Stack-Based Parsing**
   - This is not traditional parsing, but a simulation technique based on the nesting of parentheses using a **LIFO** structure.

3. Why It’s Efficient

   Compared to building expression trees or recursion (which may lead to stack overflow or redundant computation), this approach:

   - Requires **only one pass** through the string.
   - Uses **constant time operations** per character.
   - Requires only **O(n)** space at most.

#### Step-by-Step Walkthrough (With Table)

1. Let’s use the string: `s = "()(())"`

1. Simulation Table

   | Step | Character | Stack Before | Operation                                  | Stack After |
   | ---- | --------- | ------------ | ------------------------------------------ | ----------- |
   | 1    | `(`       | `[0]`        | Push `0` (new frame)                       | `[0, 0]`    |
   | 2    | `)`       | `[0, 0]`     | Pop `0`, max(2×0, 1) = 1 → add to previous | `[1]`       |
   | 3    | `(`       | `[1]`        | Push `0`                                   | `[1, 0]`    |
   | 4    | `(`       | `[1, 0]`     | Push `0`                                   | `[1, 0, 0]` |
   | 5    | `)`       | `[1, 0, 0]`  | Pop `0`, max(2×0, 1) = 1 → add to previous | `[1, 1]`    |
   | 6    | `)`       | `[1, 1]`     | Pop `1`, max(2×1, 1) = 2 → add to previous | `[3]`       |

1. **Final Score = 3**

#### Key Decision Logic:

- If top is `0`, then it's a simple `()`, and we push `1`.
- If not, it's a nested structure. Multiply the accumulated score by 2.
- The `max(2 * inner_score, 1)` handles both cases:
  - For `()`, it returns `1`.
  - For nested structures, it doubles the score.

#### Time and Space Complexity

| Complexity Type | Value  | Explanation                                                 |
| --------------- | ------ | ----------------------------------------------------------- |
| Time            | $O(n)$ | We process each character in the input string exactly once. |
| Space           | $O(n)$ | Stack can grow to size proportional to input depth (n).     |

#### Summary

- This is a **stack-based parsing simulation** problem.
- The score accumulates based on structure nesting.
- `max(2 * inner_score, 1)` elegantly handles both basic and nested cases.

---

---
