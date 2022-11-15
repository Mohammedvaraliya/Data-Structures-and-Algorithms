# Data-Structures And Algorithms


### 01. Binary Trees: Traversal Algorithms

    Binary Trees: Traversal Algorithms

    There are three recursive depth-first search traversal algorithms (preorder, inorder, and postorder) and implement those recursively in Python.

    preorder:

                    1
                /       \
               2          3
             /   \       /  \  
            4      5    6     7
                                \
                                  8 

    In preorder traversal, first, root node is visited, then left sub-tree and after that 
    right sub-tree is visited. The process of preorder traversal can be represented as -

                              (root → left → right)

    so, above preorder traversal output will be : 
                                            1-2-4-5-3-6-7-8-
    
