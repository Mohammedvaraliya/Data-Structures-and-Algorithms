# Circular Linked List Data-Structures and Algorithms

## 01. Circular Linked Lists -- Append and Prepend

    Circular Linked List append and prepend method
    Append - Add the Node from end of list
    Prepend - Add the Node from front of the list

---

---

## 02. Circular Linked Lists -- Remove Node

    Circular Linked Lists -- Remove Node
    It will remove the Node from the list

---

---

## 03. Circular Linked Lists -- Split List

    Circular Linked Lists -- Split List
    It will split the Circular Linked List into two Circular Linked List

---

---

## 04. Circular Linked Lists -- Josephus Problem

    Circular Linked Lists -- Josephus Problem
    Josephus problem will remove every node from the given Circular Linked List of the given step until only one Node left in the list

    Example:

    Circular Linked List :
                            1
                            2
                            3
                            4
                            5
                            6

    step = 2

    so the step start from head of the list

    2 is Node where step meet
    remove : 2

    4 is Node where step meet
    remove : 4

    6 is Node where step meet
    remove : 6

    since, it is cicular linked list it will circular again and remove the step Node until only one Node left

    3 is Node where step meet
    remove : 3

    Only one Node left : which is 5

---

---

## 05. Circular Linked Lists -- Is Circular Linked List

    Circular Linked Lists -- Is Circular Linked List

    It will check the list which is given is circular or not

    we can check this by giving Singly and Doubly linked list to verify Circular Linked List

---

---

## 06. Circular Linked Lists -- Linked List Cycle

[Leetcode Problem URL](https://leetcode.com/problems/linked-list-cycle/)

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. Note that `pos` is not passed as a parameter.

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

```bash
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

```bash
Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

```bash
Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

### Explanation

This problem requires detecting whether a linked list has a cycle. A cycle occurs when a node's `next` pointer points back to a previous node, creating a loop.

#### Approach Explanation

1. Why This Approach?

   We detect the cycle using **Floyd’s Tortoise and Hare Algorithm** (a two-pointer technique). This method is both efficient and elegant — it doesn't require extra space like hash sets and detects cycles in `O(n)` time with `O(1)` space.

1. Problem-Solving Pattern

   - **Two Pointer (Fast and Slow Pointers)** — a classic approach used for cycle detection in linked lists.
   - **Hashing (Method 2)** — an alternative approach that uses extra space but is easier to understand for beginners.

#### Step-by-Step Walkthrough

1. We will walk through **Floyd's Cycle Detection Algorithm** using the input:

   ```python
   Input: [3, 2, 0, -4], pos = 1
   ```

1. This means the list looks like:

   `3 → 2 → 0 → -4` and `-4.next = 2` (cycle starts at node 2).

1. Iteration Table

   | Step | Slow Pointer | Fast Pointer | Notes                                    |
   | ---- | ------------ | ------------ | ---------------------------------------- |
   | 0    | 3 (head)     | 3 (head)     | Both pointers start at head              |
   | 1    | 2            | 0            | slow = slow\.next, fast = fast.next.next |
   | 2    | 0            | 2            | moving further                           |
   | 3    | -4           | -4           | Both meet → Cycle detected               |

1. When `slow == fast`, a cycle is confirmed.

#### Time and Space Complexity Analysis

| Method              | Time Complexity | Space Complexity | Explanation                     |
| ------------------- | --------------- | ---------------- | ------------------------------- |
| Two Pointer (Floyd) | $O(n)$          | $O(1)$           | Fast and slow pointer traversal |
| Hashing             | $O(n)$          | $O(n)$           | Store each node in a set        |

#### Summary

- **Best Practice:** Use Floyd’s algorithm for efficient constant space solution.
- **Alternative:** Hashing can be useful when clarity is more important than optimal space.

---

---

## 07. Circular Linked Lists -- Linked List Cycle II

[LeetCode Problem URL](https://leetcode.com/problems/linked-list-cycle-ii/)

Given the `head` of a linked list, return the node where the cycle begins. If there is no cycle, return `null`.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to (0-indexed). It is `-1` if there is no cycle. Note that `pos` is not passed as a parameter.

Do not modify the linked list.

![img1](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

```bash
Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```

![img2](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

```bash
Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

![img3](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)

```bash
Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.
```

### Explanation

This problem requires us to detect the starting node of a cycle in a linked list, if it exists. The solution must efficiently identify the cycle without modifying the list or using extra space.

#### Approach Explanation

1. Why This Approach

   Iv'e used **Floyd’s Cycle Detection Algorithm (also called the Tortoise and Hare algorithm)**. It efficiently detects the presence of a cycle and determines its starting node with:

   - O(n) time complexity
   - O(1) space complexity
   - No modifications to the linked list structure

2. Pattern Used

   - **Fast and Slow Pointer Technique (Two-Pointer Technique)**

   This is a classic technique for detecting cycles in linked structures.

3. How This Approach Works

   Floyd’s Cycle Detection Algorithm works in two phases:

   - **Phase 1:** Detect whether a cycle exists using two pointers: `slow` (moves 1 step) and `fast` (moves 2 steps). If a cycle exists, they will meet inside the cycle.
   - **Phase 2:** Once a cycle is detected, place one pointer (`p`) at the head and move both `p` and `slow` one step at a time. They will meet at the **starting point of the cycle**.

   > After they meet in the loop, starting one pointer from head and one from the meeting point — both moving 1 step at a time — will always meet at the start of the cycle.

#### Step-by-Step Walkthrough (with Example)

1. Let's use the input: `head = [3, 2, 0, -4]`, with `pos = 1`. That means the tail connects back to the node with value `2`.

2. Linked List Structure (Cycle Exists)

   ```
   3 -> 2 -> 0 -> -4
       ↑         ↓
       ← ← ← ← ←
   ```

3. Step-by-Step Execution Table

   | Step | `slow` value | `fast` value | Phase                              |
   | ---- | ------------ | ------------ | ---------------------------------- |
   | 1    | 3            | 3            | Init                               |
   | 2    | 2            | 0            | Moving                             |
   | 3    | 0            | 2            | Moving                             |
   | 4    | -4           | -4           | **Meeting Point** (Cycle Detected) |

4. We now place `p = head = 3`, and move both `p` and `slow` one step at a time.

   | Step | `p` value | `slow` value | Comment           |
   | ---- | --------- | ------------ | ----------------- |
   | 1    | 3         | -4           |                   |
   | 2    | 2         | 2            | Cycle begins here |

#### Time and Space Complexity

| Complexity Type  | Value  | Explanation                                    |
| ---------------- | ------ | ---------------------------------------------- |
| Time Complexity  | $O(n)$ | Each pointer traverses the list at most twice. |
| Space Complexity | $O(1)$ | No extra space is used except pointers.        |

---

---
