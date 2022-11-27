# Data-Structures And Algorithms

##### Note. The name of function which is same but _ before name is helper function.

### 02. Binary Search Trees: Insertion

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

### 03. Binary Search Trees: Searching

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

### 04. Binary Search Trees: Checking the BST Property

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


    

