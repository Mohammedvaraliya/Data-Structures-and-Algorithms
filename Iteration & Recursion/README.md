# Data-Structures And Algorithms


### 01. Understanding Iterative Approach

    Understanding Iterative Approach
    The repeated execution of some groups of code statements in a program is called iteration.

    Example:
    
    To find a sum of given n number
    we will iterate n + 1 number and add the number into sum variable. i.e

    find_sum(5)

    initialize sum = 0

    we will iterate to n + 1 number which is 5, and add a number into sum variable
    i = 0   i.e 0 + 0   = 0
    i = 1   i.e 0 + 1   = 1
    i = 2   i.e 1 + 2   = 3
    i = 3   i.e 3 + 3   = 6
    i = 4   i.e 6 + 4   = 10
    i = 5   i.e 10 + 5  = 15

### 02. Understanding Recursive Approach

    Understanding Recursion Approach
    Recursion is a process in which a function calls itself directly or indirectly. 
    Recursive algorithms are widely used in computer science to solve complex problems by breaking them down into simpler ones.

    Given a number n, find sum of first n natural numbers. To calculate the sum, we will use a recursive function find_sum().

    Examples : 

    To find a sum of given n number

    Example 1: Let n = 5

               Therefore, the sum of the first 5 natural numbers = 1 + 2 + 3 + 4 + 5 = 15.

               Thus, the output is 15.

    Example 2: Let n = 7

               Therefore, the sum of the first 7 natural numbers = 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
   
               Thus, the output is 28.

    Example 3: Let n = 6

               Therefore, the sum of the first 6 natural numbers = 1 + 2 + 3 + 4 + 5 + 6 = 21.
           
               Thus, the output is 21.

### 03. Fibonacci Number Using Recursion

    Fibonacci Number Using Recursion

    The Fibonacci numbers are the numbers in the following integer sequence.
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..

    In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation

    Fn = Fn-1 + Fn-2
    with seed values 

    F0 = 0 and F1 = 1.

    Given a number n, print n-th Fibonacci Number. 

    Examples: 

    Input  : n = 2
    Output : 1

    Input  : n = 9
    Output : 34
    
    For example, if n = 0, then fib() should return 0. If n = 1, then it should return 1. For n > 1, it should return Fn-1 + Fn-2

    For n = 9
    Output:34

### 04. Recursion: List sum

    Recursion: List sum
    To find the sum of list recursively

    Example:

            list = [1, 2, [3,4],[5,6]]
    
    Initialize variable: total = 0
        
    Here the program iterate through each element of the list and add the element value to a variable (total).
    If the element exist where the another list found

    Call that element as recursively, so the above step will execute again for that list

    Example:

        1st iteration:

            element = 1

            so, add element to the (total) variable 

            total = 1

        2nd iteration:

            element = 2

            so, add element to the (total) variable 

            total = 3
        
        3rd iteration:

            element = [3, 4]

            here, we found element with another list

            call recursively, so we get total number

            1st iteration:

                element = 3

                so, add element to the (total) variable

                total = 3
            
            2nd iteration:

                element = 4

                so, add element to the (total) variable

                total = 7

            total = 3 + 7
            total = 10

        4th iteration:

            element = [5, 6]

            here, we found element with another list

            call recursively, so we get total number

            1st iteration:

                element = 5

                so, add element to the (total) variable

                total = 5
            
            2nd iteration:

                element = 6

                so, add element to the (total) variable

                total = 11

            total = 11 + 10
            total = 21

    The final output of the sum_of_list is 21

### 05. Recursion: Get Sum Of Integer

    Recursion: Get Sum Of Integer
    Given a number, the sum of its digits.

    Examples : 

            Input: n = 345
            Output: 12

            Input: n = 687
            Output: 21

            Input: n = 12
            Output: 3

    The below steps to solve the problem:

    1. Get the number

    2. Declare a variable to store the sum and set it to 0

    3. Repeat the next two steps till the number is not 0

    4. Get the rightmost digit of the number with help of the remainder ‘%’ operator by dividing it 
       by 10 and adding it to the sum.

    5. Divide the number by 10 with help of ‘/’ operator to remove the rightmost digit.

    6. Print or return the sum

### 06. Recursion: Sum Of Positive Integer

    Recursion: Sum Of Positive Integer
    Sum of positive integer

    Example:
            sum_series(6) -> 12
            sum_series(10) -> 30

    sum_series of number 6 will be
    n = 6
    when n == 0 
    return 0

    Otherwise, n+(n-2)+(n-4)... (until n-x =< 0)
    The following step to get the sum of intefer
                    n = 6
                    n = 4
                    n = 2
                    n = 0

                    return 0
                    
                    0 + 2 = 2
                    2 + 4 = 6
                    6 + 6 = 12

            12 is the output

    sum_series of number 10 will be
    n = 10
    when n == 0 
    return 0

    Otherwise, n+(n-2)+(n-4)... (until n-x =< 0)
    The following step to get the sum of intefer
                    n = 10
                    n = 8
                    n = 6
                    n = 4
                    n = 2
                    n = 0

                    return 0
                    
                    0 + 2 = 2
                    2 + 4 = 6
                    6 + 6 = 12
                    12 + 8 = 20
                    20 + 10 = 30 

            30 is the output








