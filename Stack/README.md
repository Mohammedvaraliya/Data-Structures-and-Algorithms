# Data-Structures And Algorithms


### 01. The Stack data Structure

    Stack Data Structure
    Stack in FILO(First In Last Out) or LIFO(Last In First Out) Data structure
        
       | D |
       | C |
       | B |
       | A |
       -----
    
    Example:
    This is stack

            |   |
            -----
    
    When you push an element 'A' to stack 
    stack will look like

                        | A |
                        -----
    
    Now if you add some more element, it will add one above one
    final stack:

                | D |
                | C |
                | B |
                | A |
                -----

    When you to pop the element from stack, it will pop from top of the stack or the recent pushed element 

                | C |
                | B |
                | A |
                -----

### 03. Determine if parenthesis are balanced

    Determine if parenthesis are balanced
    Use a stack to check whether or not a string has
    balanced usage of parenthesis.

    Example:
        (), ()(), (({{[]}})) <== Balanced.
        ((),  {{{)}], [][]]] <== Not Balanced.

    Balanced Example: {[]}

    Non-Balanced Example: (()

    Non-Balanced Example: ]]

### 04. Convert integer to binary

    Convert integer to binary
    Use a stack data structure to convert integer values to binary.

    Example : 242

    242 / 2 = 121 -> 0    # 0 is a remainder as number is even
    121 / 2 = 60  -> 1    # 1 is a remainder as number is odd
    60 / 2  = 30  -> 0    # 0 is a remainder as number is even
    30 / 2  = 15  -> 0    # 0 is a remainder as number is even
    15 / 2  = 7   -> 1    # 1 is a remainder as number is odd
    7 / 2   = 3   -> 1    # 1 is a remainder as number is odd
    3 / 2   = 1   -> 1    # 1 is a remainder as number is odd
    1 / 2   = 0   -> 1    # 1 is a remainder as number is odd

    11110010 is the binary number of integer 242

