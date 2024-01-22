# Data-Structures And Algorithms

##### Note. The name of function which is same but _ before name is helper function.

### 01. Binary Trees: Traversal Algorithms Pre-order

```bash
Binary Trees: Traversal Algorithms Pre-order

There are three recursive depth-first search traversal algorithms (preorder, inorder, and postorder) and implement those recursively in Python.

Pre-Order Traversal:

                1
            /       \
            2          3
          /   \       /  \  
        4      5    6     7

This technique follows the 'root left right' policy. It means that, first root node is visited after that the left subtree is traversed recursively, and finally, right subtree is recursively traversed. As the root node is traversed before (or pre) the left and right subtree, it is called preorder traversal.

So, in a preorder traversal, each node is visited before both of its subtrees.

                          (root -> left -> right)

so, above preorder traversal output will be : 
                                        1-2-4-5-3-6-7
```

### 02. Binary Trees: Traversal Algorithms In-order

```bash
Binary Trees: Traversal Algorithms In-order

There are three recursive depth-first search traversal algorithms (preorder, inorder, and postorder) and implement those recursively in Python.

In-Order Traversal:

            1
        /       \
        2          3
      /   \       /  \  
    4      5    6     7

This technique follows the 'left root right' policy. It means that first left subtree is visited after that root node is traversed, and finally, the right subtree is traversed. As the root node is traversed between the left and right subtree, it is named inorder traversal.

So, in the inorder traversal, each node is visited in between of its subtrees.

                      (root -> left -> right)

so, above inorder traversal output will be : 
                                    4-2-5-1-6-3-7-
```

### 03. Binary Trees: Traversal Algorithms Post-order

```bash
Binary Trees: Traversal Algorithms Post-order

There are three recursive depth-first search traversal algorithms (preorder, inorder, and postorder) and implement those recursively in Python.

Post-Order Traversal:

                1
            /       \
            2          3
          /   \       /  \  
        4      5    6     7

This technique follows the 'left-right root' policy. It means that the first left subtree of the root node is traversed, after that recursively traverses the right subtree, and finally, the root node is traversed. As the root node is traversed after (or post) the left and right subtree, it is called postorder traversal.

So, in a postorder traversal, each node is visited after both of its subtrees.

                          (left -> right -> root)

so, above postorder traversal output will be : 
                                        4-5-2-6-7-3-1-
```

### 04. Binary Trees: Traversal Algorithms Level-order

```bash
Binary Trees: Traversal Algorithms Level-order

Level-Order Traversal:

                1
            /     \
            2        3
          /  \          
        4    5     

Given a binary tree, the task is to print the level order traversal line by line of the tree

Level Order Traversal is the algorithm to process all nodes of a tree by traversing through depth, first the root, then the child of the root, etc.

In simple word level-order traversal will print the node according to level.

so, above level-order traversal output will be : 
                                        1-2-3-4-5-
```

### 05. Binary Trees: Traversal Algorithms Reverse Level-order

```bash
Binary Trees: Traversal Algorithms Reverse Level-order

Level-Order Traversal:

                1
            /     \
            2        3
          /  \          
        4    5     

Given a binary tree, the task is to print the reverse level order traversal line by line of the tree

The idea is to print the last level first, then the second last level, and so on. Like Level order traversal, every level is printed from left to right.

so, above reverse level-order traversal output will be : 
                                                        4-5-2-3-1-
```

### 06. Binary Trees: Calculating Height of Tree

```bash
Binary Trees: Calculating Height of Tree

It will return the height of the binary tree
                
                (1) 
                  1       
            (1)  /   \ (0)  
                2      3
          (0)  /  \  (0)        
              4     5  

The height of leaf node with data 4 is 0 because there is no child node present
The height of leaf node with data 5 is 0 because there is no child node present
The height of leaf node with data 3 is 0 because there is no child node present

The height of node with data 2 is 1 becase the max between two child node + 1 is the height of node
example:
        1 + max(left_child, right_child)
        1 + max(0, 0)
        1 + 0
        1

The height of node with data 1 is 2 becase the max between two child node + 1 is the height of node
example:
        1 + max(left_child, right_child)
        1 + max(1, 0)
        1 + 1
        1

max will return the maximum number of given 2 numbers

so, the height of this binary tree is: 2
```

### 07. Binary Trees: Calculating Size of Tree

```bash
Binary Trees: Calculating Size of Tree

It will return the size of the binary tree
                
                  1       
                /  \    
                2     3
              /  \           
              4     5  

To calculate the size of the binary tree we use stack data structure to keep record of the nodes 
by push and pop operations.

Example:
            start from root node

            1

            push onto stack

            stack : [1]

            make size 1

            pop from the stack and check if root node have childrens, so push childrens onto the stack.

            stack : [2, 3]

            size = 3

            pop one by one and check if popped node have any children, if yes push, otherwize make size ++

            stack : [4, 5, 3]

            size = 5

            stack : [5, 3]

            stack : [3]

            stack : []

so, the size of this binary tree is: 5
```

### 08. Binary Trees: Invert Binary Tree

[Leetcode Problem URL](https://leetcode.com/problems/invert-binary-tree/)

```bash
Given the root of a binary tree, invert the tree, and return its root.

Input :
                  4
                /   \
               2     7
              / \   / \
             1   3 6    9

Output : 
                  4
                /   \
               7     2
              / \   / \
             9   6 3    1

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
```

### 09. Binary Trees: Maximum Depth of Binary Tree

[Leetcode Problem URL](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

```bash
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

                  3
                 / \
                9   20
                   /  \
                  15   7

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
```

### 10. Binary Trees: Subtree Of Another Tree

[Leetcode Problem URL](https://leetcode.com/problems/subtree-of-another-tree/)

```bash
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
```

#### Example 1:
  ![Alt text](assets/subtree1-tree.jpg)
```bash
Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
```

#### Example 2:
  ![Alt text](assets/subtree2-tree.jpg)
```bash
Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
```

### 11. Binary Trees: Level Order Traversal - BFS

[Leetcode Problem URL](https://leetcode.com/problems/binary-tree-level-order-traversal/)

```bash
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
```

#### Example 1:
  ![Alt text](assets/tree1.jpg)
```bash
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

#### Example 2:
```bash
Input: root = [1]
Output: [[1]]
```

#### Example 3:
```bash
Input: root = []
Output: []
```

### 12. Binary Trees: Construct Binary Tree from Preorder and Inorder Traversal

[Leetcode Problem URL](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

```bash
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the 
inorder traversal of the same tree, construct and return the binary tree.
```

#### Example 1:
  ![Alt text](assets/tree.jpg)
```bash
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

#### Example 2:
```bash
Input: preorder = [-1], inorder = [-1]
Output: [-1]
```

#### Example 3:
```bash
Input: root = []
Output: []
```


### 13. Binary Trees: Construct Binary Tree from Inorder and Postorder Traversal

[Leetcode Problem URL](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

```bash
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder 
is the postorder traversal of the same tree, construct and return the binary tree.
```

#### Example 1:
  ![Alt text](assets/tree.jpg)
```bash
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
```

#### Example 2:
```bash
Input: inorder = [-1], postorder = [-1]
Output: [-1]
```

### 14. Binary Trees: Maximum Path Sum

[Leetcode Problem URL](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

```bash
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
```

#### Example 1:
  ![Alt text](assets/exx1.jpg)
```bash
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
```

#### Example 2:
  ![Alt text](assets/exx2.jpg)
```bash
Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
```
    
