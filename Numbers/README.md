# Data-Structures And Algorithms


### 01. Product of Two Numbers

    Product of Two Numbers
    Given two numbers, find their product using recursion.

    Example:
            x = 5
            y = 4

    x * y = 20

    using recursion:
    addition of x with y times
    It means:
            x = 5
            y = 4

    5 + 5 + 5 + 5 = 20

### 02. Numbers: Convert Integer To Binary

    Numbers: Convert Integer To Binary Number
    The algorithm works by repeatedly doubling a variable power until it is greater than the integer n. 
    It then divides power by 2 to get the largest power of 2 less than n. 
    This value of power is used to determine which digits in the binary representation should be set to 1.

    The algorithm then repeatedly divides power by 2 and checks if the current value of power is less than or equal to n. 
    If it is, the algorithm subtracts power from n and adds a "1" to the binary representation. 
    If it is not, the algorithm adds a "0" to the binary representation. 
    This process continues until power becomes 0, at which point the binary representation is complete.

    Example:

                n = 10
                power = 1
                result = ""

        Everytime double the power varibale until the n is greater
        power = 2
        power = 4
        power = 8

        check if the number is less than or equal to n
        if yes
        add "1" to the result string
        otherwise add "0"

                        int :    8   4   2    1
                        result:  1   0   1    0                    

        final binary string is : "1010" of integer 10 

### 03. Numbers: Convert Binary To Integer

        Numbers: Convert Binary To Integer
        Initialize a variable result to 0. 
        This will be used to store the integer representation of the binary number.

        Initialize a variable power to 1. 
        This will be used to keep track of the current power of 2.

        Initialize a variable i to the length of the binary number minus 1. 
        This will be used as an index to iterate through the binary number from least significant digit to most significant digit.

        While i is greater than or equal to 0, do the following:

                If the i-th digit of the binary number is 1, add power to result.
                Multiply power by 2.
                Decrement i by 1.
                Return result as the integer representation of the binary number.

        Example:
                
                bunary_number = "1010"

                result = 0
                power = 1
                i = len(binary_number) - 1
            i.e i = 4 - 1
                i = 3

                While i is greater than or equal to 0, do the following:
                        
                ----->  if the number at index bunary_number[i] is 1 so:
                                add the value of power to result
                                i.e result = 0 + 1
                                    result = 1
                        
                        And make the power double:
                        i.e power = 1*1
                            power = 2
                        and decrement the value of i so we get all the indexes
                        i = 3 - 1
                        i = 2

                ----->  Now check again

                        if the number at index bunary_number[i] is 1 so:
                                add the value of power to result
                                i.e result = 1 + 2
                                    result = 3
                        
                        And make the power double:
                        i.e power = 2*2
                            power = 4
                        and decrement the value of i so we get all the indexes
                        i = 2 - 1
                        i = 1

                ----->  Now check again

                        if the number at index bunary_number[i] is 0 so:
                        
                        make the power double:
                        i.e power = 4*2
                            power = 8
                        and decrement the value of i so we get all the indexes
                        i = 1 - 1
                        i = 0 

                ----->  Now check again

                        if the number at index bunary_number[i] is 1 so:
                                add the value of power to result
                                i.e result = 3 + 8
                                    result = 11
                        
                
                return reseult
                The integer of binary number 1011 is 11








