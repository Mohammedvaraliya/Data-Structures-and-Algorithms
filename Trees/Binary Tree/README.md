# Data-Structures And Algorithms


### 01. Binary Trees: Traversal Algorithms Pre-order

    Binary Trees: Traversal Algorithms

    There are three recursive depth-first search traversal algorithms (preorder, inorder, and postorder) and implement those recursively in Python.

    Pre-Order Traversal:

                    1
                /       \
               2          3
             /   \       /  \  
            4      5    6     7

    In preorder traversal, first, root node is visited, then left sub-tree and after that 
    right sub-tree is visited. The process of preorder traversal can be represented as -

                              (root → left → right)

    so, above preorder traversal output will be : 
                                            1-2-4-5-3-6-7
                                            
### 02. Binary Trees: Traversal Algorithms In-order

    Binary Trees: Traversal Algorithms

    There are three recursive depth-first search traversal algorithms (preorder, inorder, and postorder) and implement those recursively in Python.

    In-Order Traversal:
    
                    1
                /       \
               2          3
             /   \       /  \  
            4      5    6     7

    This technique follows the 'left root right' policy. It means that first left subtree is visited after that root node is traversed, and finally, the right subtree is traversed. As the root node is traversed between the left and right subtree, it is named inorder traversal.

    So, in the inorder traversal, each node is visited in between of its subtrees.

                              (root → left → right)

    so, above inorder traversal output will be : 
                                            4-2-5-1-6-3-7-
    
