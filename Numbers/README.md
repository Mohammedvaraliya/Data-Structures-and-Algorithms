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

### 02. Numbers: Convert Integer To Binary Number

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



