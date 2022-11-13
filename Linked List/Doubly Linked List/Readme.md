# Data-Structures And Algorithms


### 01. Doubly Linked Lists -- Append and Prepend

    Doubly Linked Lists -- Append and Prepend
    Append - Add the Node from end of the list
    Prepend - Add the Node from front of the list

### 02. Doubly Linked Lists -- Add Node Before/After

    Doubly Linked Lists -- Add Node Before/After

    Add Node Before and After will add the node respectively

    Add Node Before Example:
                            1
                            2
                            3
                            4
                            5
                    
    Addbeforenode(2) = 1
    final list will be:     1
                            1
                            2
                            3
                            4
                            5
    
    Add Node After Example:
                            1
                            2
                            3
                            4
                            5
                    
    Addafternode(2) = 2
    final list will be:     1
                            2
                            2
                            3
                            4
                            5

### 03. Doubly Linked Lists -- Delete Node

    Doubly Linked Lists -- Delete Node
    It will delete the node list

### 04. Doubly Linked Lists -- Reverse

    Doubly Linked Lists -- Reverse
    It will reversed the Doubly Linked List 

    Example:
            1
            2
            3
            4
            5
    
    reversed_list :
                    5
                    4
                    3
                    2
                    1

### 05. Doubly Linked Lists -- Remove Duplicates

    Doubly Linked Lists -- Remove Duplicates
    It will remove the duplicate Node from the list

    Example:
            1
            1
            2
            2
            3
            4
            5
    
    After removing the duplicate from the Doubly Linked list
    Doubly Linked List will be:
                                1
                                2
                                3
                                4
                                5

### 06. Doubly Linked Lists -- Pairs with Sum

    Doubly Linked Lists -- Pairs with Sum
    It will return the pair of data of Node where the sum of 2 data of Node is equal to the given number

    Example:
    Doubly Linked List:
                        1
                        2
                        3
                        4
                        5

    pair_with_sum(6) will return 2 pairs
                                         ['(1, 5)', ('2, 4')]

    because 1 + 5 = 6
            2 + 4 = 6

    pair_with_sum(5) will return 2 pairs
                                         ['(1, 4)', ('2, 3')]

    because 1 + 4 = 5
            2 + 3 = 5

    pair_with_sum(0) will return Emplty List
                                         []

    because there is no pair exist which sum equal to given number

