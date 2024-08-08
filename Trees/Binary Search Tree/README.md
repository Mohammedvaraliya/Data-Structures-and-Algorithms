# Binary Search Trees Data-Structures and Algorithms

##### Note. The name of function which is same but \_ before name is helper function.

## 01. Binary Search Trees: Insertion

    Binary Search Trees: Insertion
    It will insert the Node to the Binary Search Tree

    Example:

                  8
                /    \
               3       10
             /   \
            1      6

    insert a Node with data 4
    it will start from root node
    is the data is less than or greater than root node.

    4 < 8 - 4 is less than 8

    move left

    is the data is less than or greater than cur node.

    4 > 3 - 4 is greater than 3

    move right

    is the data is less than or greater than cur node.

    4 < 6 - 4 is less than 6

    move left

    if no node in the left

    simply, insert the node over there

    final Binary Search Tree will be:

                   8
                /    \
               3       10
             /   \
            1      6
                 /
               4

## 02. Binary Search Trees: Searching

    Binary Search Trees: Searching
    It will give result after searching the node throughout the Binary Search Tree.
    either True or False.

    Example:

                   8
                /    \
               3       10
             /   \
            1      6

    Search(6):

    start from the root node.
    is the data is less than or greater than or equal to the root node.

    6 < 8 - 6 is less than 8

    discard the right part of root node cause we know our node will present on the left side.

                  8
                /
               3
             /   \
            1      6

    move left

    is the data is less than or greater than or equal to the cur node.

    6 > 3 - 6 is greater than 6

    discard the left part of cur node cause we know our node will present on the right side.

                  8
                /
               3
                 \
                   6

    move right

    is the data is less than or greater than or equal to the cur node.

    6 == 6 - the data is equal to cur node

    return True

    if we cant find the data equal to node: return False

## 03. Binary Search Trees: Checking the BST Property

    Binary Search Trees: Checking the BST Property
    Specifically, we will be solving the problem of determining whether or not a given tree we are given as input abides by the so-called binary search tree (BST) property.

    The BST property states that every node on the right subtree has to be larger than the current node and every
    node on the left subtree has to be smaller than the current node. Is determines whether a given tree satisfies
    the BST property.

    Example:

    satisfied property tree:

            In-Order Traversal

                    8
                /       \
               3          10
             /   \       /  \
            1      6    9     11

            1
            3
            6
            8
            9
            10
            11

    return True

    unsatisfied property tree:

            In-Order Traversal

                    1
                  /   \
                2       3

            2
            1
            3

    return False

## 04. Binary Search Trees: Using list

    Binary Search Trees: Insertion with the help of list
    Binary Search Tree will build with the help of list

    Example:

            list = [17, 4, 1, 20, 9, 23, 18, 34]

    let make 1st element of the list to root of the list.
    root node : (17)

    Traverse the list from 1st element to last i.e (4 to 34).
    i = If the data is less than root node, try to add the child to the left side
    if the left child already present there, so repeat the step i.
    if the data is less and left child is None, simply add the child over there.

    j = If the data is greater than root node, try to add the child to the right side
    if the right child already present there, so repeat the step j.
    if the data is greater and right child is None, simply add the child over there.

    Final Binary Search Tree will look like:

                                              17
                                            /   \
                                           /     \
                                          4       20
                                         / \     /  \
                                        /   \   /    \
                                       1     9  18    23
                                                       \
                                                        \
                                                        34

    Note: The Left Side of the Binary Search Tree vlaues should be less than the root node value.
          The Right Side of the Binary Search Tree values should be greater than the root node value.

          * For more clarification, please [See the code](./02_binary_search_tree_using_list.py.py)

## 05. Binary Search Trees: Using list - In-Order-Traversal

    In-Order-Traversal

                                              17
                                            /   \
                                           /     \
                                          4       20
                                         / \     /  \
                                        /   \   /    \
                                       1     9  18    23
                                                       \
                                                        \
                                                        34

    In depth-first traversal: in-order is the traversal algorithm which is used to traverse the tree.
    This methods follows the step

    It will first traverse the left sub-tree, then root node, and then right sub tree.

    Start from root node i.e 17.

    finalList = [1, 4, 9, 17, 18, 20, 23, 34]

## 06. Binary Search Trees: Using list - Post-Order-Traversal

    Post-Order-Traversal

                                              17
                                            /   \
                                           /     \
                                          4       20
                                         / \     /  \
                                        /   \   /    \
                                       1     9  18    23
                                                       \
                                                        \
                                                        34

    In depth-first traversal: post-order is the traversal algorithm which is used to traverse the tree.
    This methods follows the step

    It will first traverse the left sub-tree, then right sub-tree, and then root node.

    Start from root node i.e 17.

    finalList = [1, 9, 4, 18, 34, 23, 20, 17]

## 07. Binary Search Trees: Using list - Pre-Order-Traversal

    Pre-Order-Traversal

                                              17
                                            /   \
                                           /     \
                                          4       20
                                         / \     /  \
                                        /   \   /    \
                                       1     9  18    23
                                                       \
                                                        \
                                                        34

    In depth-first traversal: pre-order is the traversal algorithm which is used to traverse the tree.
    This methods follows the step

    It will first traverse the root node, then left sub-tree, and then right sub tree.

    Start from root node i.e 17.

    finalList = [17, 4, 1, 9, 20, 18, 23, 34]

## 08. Binary Search Trees: Using list - Delete Node Method 1

    Binary Search Trees: Using list - Delete Node Method 1
    It will delete the node from binary search tree of given data

    Example:
    Binary Search Tree

                                              17
                                            /   \
                                           /     \
                                          4       20
                                         / \     /  \
                                        /   \   /    \
                                       1     9  18    23
                                                       \
                                                        \
                                                        34

    delete(20)

    To delete the node with value 20,
    start from root node
    is the 20 less than or greater than root node value

    20 is greater value

    decline the left side of tree and traverse right side

    if the value is equal to the cur node

    find min value of right sub tree from cur node i.e min(23, 34)

    min is 23

    copy the value and update to the cur node

    now remove duplicate.

    Final BST will look like:

                                              17
                                            /   \
                                           /     \
                                          4       23
                                         / \     /  \
                                        /   \   /    \
                                       1     9  18    34

## 09. Binary Search Trees: Using list - Delete Node Method 2

    Binary Search Trees: Using list - Delete Node Method 2
    It will delete the node from binary search tree of given data

    Example:
    Binary Search Tree

                                              17
                                            /   \
                                           /     \
                                          4       20
                                         / \     /  \
                                        /   \   /    \
                                       1     9  18    23
                                                       \
                                                        \
                                                        34

    delete(20)

    To delete the node with value 20,
    start from root node
    is the 20 less than or greater than root node value

    20 is greater value

    decline the left side of tree and traverse right side

    if the value is equal to the cur node

    find max value of left sub tree from cur node i.e max(18)

    there is only one node in the left sub tree.

    max is 18

    copy the value and update to the cur node

    now remove duplicate.

    Final BST will look like:

                                              17
                                            /   \
                                           /     \
                                          4       18
                                         / \        \
                                        /   \        \
                                       1     9        23
                                                       \
                                                        \
                                                         34

## 10. Binary Search Trees: Lowest Common Ancestor of a Binary Search Tree

[Leetcode Problem URL](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

    Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”!

Example 1:
![BST](assets/binarysearchtree_improved.png)

    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
![BST](assets/binarysearchtree_improved.png)

    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
    Output: 2
    Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:

    Input: root = [2,1], p = 2, q = 1
    Output: 2

## 11. Binary Search Trees: Validate

[Leetcode Problem URL](https://leetcode.com/problems/validate-binary-search-tree/)

    Given the root of a binary tree, determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Example 1:

![BST](assets/tree1.jpg)

    Input: root = [2,1,3]
    Output: true

Example 2:

![BST](assets/tree2.jpg)

    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.

## 12. Binary Search Trees: Kth Smallest Element

[Leetcode Problem URL](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

    Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of
    all the values of the nodes in the tree.

Example 1:

![BST](assets/kthtree1.jpg)

    Input: root = [3,1,4,null,2], k = 1
    Output: 1

Example 2:

![BST](assets/kthtree2.jpg)

    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3
