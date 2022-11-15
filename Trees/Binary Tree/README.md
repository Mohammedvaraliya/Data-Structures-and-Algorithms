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

    This technique follows the 'root left right' policy. It means that, first root node is visited after that the left subtree is traversed recursively, and finally, right subtree is recursively traversed. As the root node is traversed before (or pre) the left and right subtree, it is called preorder traversal.

    So, in a preorder traversal, each node is visited before both of its subtrees.

                              (root -> left -> right)

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

                              (root -> left -> right)

    so, above inorder traversal output will be : 
                                            4-2-5-1-6-3-7-

### 03. Binary Trees: Traversal Algorithms Post-order

    Binary Trees: Traversal Algorithms

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
                                            4-2-5-6-3-7-1-
    
