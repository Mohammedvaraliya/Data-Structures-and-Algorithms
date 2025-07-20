# Singly Liked List Data-Structures and Algorithms

## 01. Singly Linked Lists -- Reverse

[Leetcode Problem URL](https://leetcode.com/problems/reverse-linked-list/)

```bash
Singly Linked Lists -- Reverse
It will reversed the Singly Linked List

Example:
        "A"
        "B"
        "C"
        "D"
        "E"

reversed_list :
                "E"
                "D"
                "C"
                "B"
                "A"

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
```

---

---

## 02. Singly Linked Lists -- Merge Two Sorted Lists

[LeetCode Problem URL](https://leetcode.com/problems/merge-two-sorted-lists/?envType=problem-list-v2&envId=linked-list)

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

![img1](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```bash
Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

```bash
Example 2:

Input: list1 = [], list2 = []
Output: []
```

```bash
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
```

### Explanation

This problem requires merging two sorted linked lists into a single sorted linked list. The key is to traverse both lists simultaneously, comparing their current nodes and appending the smaller one to the result list.

#### Approach Explanation

1. Why This Approach?

   To solve the problem efficiently, we use the **Two-Pointer technique** to traverse both sorted lists simultaneously and compare their current nodes. This allows us to **merge the lists in a single pass**, avoiding unnecessary overhead.

   This approach **preserves the sorted order** and works in **linear time**, making it ideal for large linked lists.

2. Problem-Solving Pattern

   - **Two Pointers**
   - **Greedy Merge**
   - **Linked List Manipulation**

   This is a classic merge operation, similar to the one used in the merge step of **Merge Sort**.

3. Efficiency and Elegance

   Compared to brute-force approaches that might collect values into arrays and sort them later, this solution:

   - **Does not require extra storage for values**
   - **Avoids additional sorting**
   - **Maintains constant space (excluding output)**

   We achieve an elegant and efficient solution by directly manipulating the `next` pointers of the nodes.

#### Step-by-Step Walkthrough

1. Let’s walk through the merging of the following two sorted linked lists:

   ```
   list1 = [1 -> 2 -> 4]
   list2 = [1 -> 3 -> 4]
   ```

2. Initialization

   - We create a `dummy` node to act as the starting point of our merged list.
   - We use a `tail` pointer to build the result list by attaching nodes to it.

3. Iterative Merging

   | Step | list1.val | list2.val | Action         | Merged List So Far    |
   | ---- | --------- | --------- | -------------- | --------------------- |
   | 1    | 1         | 1         | list2 appended | 1                     |
   | 2    | 1         | 3         | list1 appended | 1 → 1                 |
   | 3    | 2         | 3         | list1 appended | 1 → 1 → 2             |
   | 4    | 4         | 3         | list2 appended | 1 → 1 → 2 → 3         |
   | 5    | 4         | 4         | list2 appended | 1 → 1 → 2 → 3 → 4     |
   | 6    | 4         | None      | list1 appended | 1 → 1 → 2 → 3 → 4 → 4 |

4. At the end of the loop, we return `dummy.next` which points to the head of the merged list.

#### Time and Space Complexity

| Metric    | Complexity | Explanation                                                                 |
| --------- | ---------- | --------------------------------------------------------------------------- |
| **Time**  | $O(n + m)$ | We traverse each of the two input lists once, where `n` and `m` are lengths |
| **Space** | $O(1)$     | We perform merging in-place (excluding output list nodes already given)     |

> The solution only creates one dummy node. All other nodes are reused from the input lists.

#### Summary

- We used a **greedy** and **in-place two-pointer** strategy to merge two sorted linked lists.
- The solution is efficient, clean, and leverages standard linked list operations.
- Time complexity is **O(n + m)** and space complexity is **O(1)**, making it optimal.
- This pattern is highly reusable for other merging and comparison problems involving lists or arrays.

---

---

## 03. Singly Linked Lists -- Reorder List

[Leetcode Problem URL](https://leetcode.com/problems/reorder-list/)

```bash
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

---

---

## 04. Singly Linked Lists -- Remove Nth Node From End of List

[Leetcode Problem URL](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

```bash
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
```

---

---

## 05. Singly Linked Lists -- Linked List Cycle

[Leetcode Problem URL](https://leetcode.com/problems/linked-list-cycle/)

```bash
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```

---

---

## 06. Singly Linked Lists -- Merge k Sorted Lists

[Leetcode Problem URL](https://leetcode.com/problems/merge-k-sorted-lists/)

```bash
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
```

---

---
