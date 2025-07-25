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

## 07. Singly Linked Lists -- Remove Duplicates from Sorted List

[LeetCode Problem URL](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/?envType=problem-list-v2&envId=linked-list)

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

![img1](https://assets.leetcode.com/uploads/2021/01/04/list1.jpg)

```bash
Example 1:

Input: head = [1,1,2]
Output: [1,2]
```

![img2](https://assets.leetcode.com/uploads/2021/01/04/list2.jpg)

```bash
Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]
```

### Explanation

This problem requires removing duplicates from a sorted linked list. Since the list is already sorted, duplicates will always be adjacent, allowing us to efficiently remove them in a single pass.

#### Approach Explanation

1. Why This Approach?

   We chose a **single-pass traversal** approach since the linked list is already **sorted in non-decreasing order**. This key observation allows us to **simply compare adjacent nodes** to detect and remove duplicates in **O(n)** time without needing additional memory.

2. Problem-Solving Pattern

   - **Two-Pointer Technique** (Current and Next Pointer)
   - **Linked List Traversal**
   - **Greedy Filtering** (removing duplicates as soon as they are found)

   This pattern avoids extra data structures like hash sets or arrays and solves the problem in-place.

3. Efficiency and Elegance

   Compared to methods that involve converting the list to a Python list or using sets, our approach is:

   - **In-place**: No extra memory usage.
   - **Efficient**: Just one iteration over the list.
   - **Clean**: No complex conditionals or auxiliary operations.

#### Step-by-Step Walkthrough

1. Let’s walk through this input step-by-step:

   ```
   Input: [1 → 1 → 2 → 3 → 3]
   ```

   - Initialize a pointer `head` to the start of the list.
   - Traverse as long as both `head` and `head.next` are not null.
   - At each step:

   - If `head.val == head.next.val`, skip the next node by updating the `next` pointer.
   - Otherwise, move the `head` pointer forward.

1. Iteration Breakdown

   | Step | Current `head.val` | `head.next.val` | Action                | Linked List State |
   | ---- | ------------------ | --------------- | --------------------- | ----------------- |
   | 1    | 1                  | 1               | Duplicate → skip next | 1 → 2 → 3 → 3     |
   | 2    | 1                  | 2               | Move to next          | 1 → 2 → 3 → 3     |
   | 3    | 2                  | 3               | Move to next          | 1 → 2 → 3 → 3     |
   | 4    | 3                  | 3               | Duplicate → skip next | 1 → 2 → 3         |

   The pointer stops when `head.next` becomes `None`.

1. Final Output

   ```
   Updated List: [1 → 2 → 3]
   ```

#### Time and Space Complexity

| Metric    | Complexity | Explanation                                                       |
| --------- | ---------- | ----------------------------------------------------------------- |
| **Time**  | $O(n)$     | We traverse the entire linked list once.                          |
| **Space** | $O(1)$     | No additional data structures used; operations are done in-place. |

#### Summary

- This is an **in-place solution** that removes duplicates from a **sorted linked list**.
- By **comparing adjacent nodes**, we efficiently eliminate duplicates in **O(n)** time and **O(1)** space.
- This solution demonstrates a clean and minimalistic use of linked list traversal without auxiliary space or complexity.

---

---

## 08. Singly Linked Lists -- Delete Node in a Linked List

[LeetCode Problem URL](https://leetcode.com/problems/delete-node-in-a-linked-list/?envType=problem-list-v2&envId=linked-list)

There is a singly-linked list `head` and we want to delete a node `node` in it.

You are given the node to be deleted `node`. You will not be given access to the first node of `head`.

All the values of the linked list are unique, and it is guaranteed that the given node `node` is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

- The value of the given node should not exist in the linked list.
- The number of nodes in the linked list should decrease by one.
- All the values before `node` should be in the same order.
- All the values after `node` should be in the same order.

Custom testing:

- For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
- We will build the linked list and pass the node to your function.
- The output will be the entire list after calling your function.

![Image 1](https://assets.leetcode.com/uploads/2020/09/01/node1.jpg)

```bash
Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
```

![Image 2](https://assets.leetcode.com/uploads/2020/09/01/node2.jpg)

```bash
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
```

### Explanation

This problem requires us to delete a node from a singly linked list without having access to the head of the list. The key constraint is that we cannot traverse the list from the head, and we are guaranteed that the node to be deleted is not the last node.

#### Approach Explanation

1. Why This Approach?

   Since we don't have access to the **previous node** or the **head pointer**, we cannot simply traverse from the beginning and update links in the usual way.

   To delete the given `node`, we instead:

   - **Copy the value from the next node** into the current node.
   - **Bypass the next node** by adjusting pointers.

   This clever technique transforms the **current node into the next node**, effectively "deleting" the one we want.

2. Problem-Solving Pattern

   - **Pointer Manipulation**
   - **In-place Node Overwrite**
   - A variant of the **two-pointer technique**, although limited due to access restrictions.

   This solution is optimal given the constraints, using constant time and space, and no traversal from head.

3. Efficiency and Elegance

   This approach is elegant because:

   - It avoids traversal.
   - No extra memory is used.
   - It meets all constraints.
   - The node is deleted **logically**, not physically.

#### Step-by-Step Walkthrough

1. Let’s consider this linked list:

   ```
   Initial List: [1 → 2 → 3 → 4 → 5]
   Node to delete: 3
   ```

2. We are given a **direct reference to node `3`**, but **no access to head**.

3. Algorithm:

   ```python
   node.val = node.next.val
   node.next = node.next.next
   ```

4. Iteration Breakdown

   | Step | Operation                               | Resulting List           | Explanation                     |
   | ---- | --------------------------------------- | ------------------------ | ------------------------------- |
   | 1    | Copy `node.next.val` → `node.val`       | \[1 → 2 → **4** → 4 → 5] | Value of node `3` becomes `4`   |
   | 2    | Skip next: `node.next = node.next.next` | \[1 → 2 → 4 → 5]         | The original `4` is now skipped |

   Node `3` (now with value `4`) has replaced the next node and linked to the node after it.

5. Final Output

   ```
   Updated List: [1 → 2 → 4 → 5]
   ```

   The original `3` is logically deleted.

#### Time and Space Complexity

| Metric               | Complexity | Explanation                                                      |
| -------------------- | ---------- | ---------------------------------------------------------------- |
| **Time Complexity**  | $O(1)$     | Only local pointer and value manipulation is used; no traversal. |
| **Space Complexity** | $O(1)$     | No additional space is required beyond a few pointers.           |

#### Summary

- This solution handles deletion without head access, by **overwriting the given node**.
- It works **only when the node to delete is not the last node**.
- Offers **constant time and space complexity**.
- Elegant and efficient under given constraints.

---

---

## 09. Singly Linked Lists -- Odd Even Linked List

[LeetCode Problem URL](https://leetcode.com/problems/odd-even-linked-list/)

Given the `head` of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in `O(1)` extra space complexity and `O(n)` time complexity.

![Img1](https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg)

```bash
Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
```

![Img2](https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg)

```bash
Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
```

### Explanation

This problem requires us to rearrange a singly linked list such that all nodes at odd indices come before nodes at even indices, while maintaining the relative order of nodes in each group. The challenge is to do this in-place with constant space complexity.

#### Approach Explanation

1. Why This Approach?

   To rearrange the list while maintaining relative ordering of odd and even nodes, we traverse the list only once while maintaining two pointers:

   - One for the odd-indexed nodes.
   - One for the even-indexed nodes.

   This allows us to **relink the nodes in-place** using a single traversal and constant space.

2. Problem-Solving Pattern

   - **Pattern Used**: Two Pointers (Odd-Even separation)
   - **Type**: Linked List pointer manipulation
   - **Goal**: Partition the list into odd and even sequences while preserving relative order.

#### Step-by-Step Walkthrough

1. Example: Input `head = [1, 2, 3, 4, 5]`

2. Initial Structure:

   ```
   Index:  1   2   3   4   5
   Node:   1 → 2 → 3 → 4 → 5
   ```

3. **Initialization**:

   - `odd = head` → points to 1
   - `even = head.next` → points to 2
   - `even_head = even` → stores the start of even list (needed later)

4. **Iteration 1**:

   - `odd.next = even.next` → 1's next becomes 3
   - `odd = odd.next` → move odd to 3
   - `even.next = odd.next` → 2's next becomes 4
   - `even = even.next` → move even to 4

5. **List so far**:

   ```
   Odd List: 1 → 3
   Even List: 2 → 4
   Remaining: 5
   ```

6. **Iteration 2**:

   - `odd.next = even.next` → 3's next becomes 5
   - `odd = odd.next` → move odd to 5
   - `even.next = odd.next` → 4’s next is now None (end)
   - `even = even.next` → even becomes None (loop ends)

7. **Final Merge**:

   - `odd.next = even_head` → connect odd list to start of even list

8. **Result**:

   ```
   1 → 3 → 5 → 2 → 4
   ```

#### Time and Space Complexity Analysis

| Metric           | Value  | Explanation                                                            |
| ---------------- | ------ | ---------------------------------------------------------------------- |
| Time Complexity  | $O(n)$ | Single traversal of the entire list (each node visited once).          |
| Space Complexity | $O(1)$ | No extra space used other than a few pointers; list modified in-place. |

#### Summary

- This approach achieves **in-place rearrangement** by separating odd and even indexed nodes with constant space.
- No values are changed—only pointer manipulation is used.

---

---
