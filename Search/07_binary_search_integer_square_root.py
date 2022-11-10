'''
write a function that takes a non-negative integer and returns the largest integer whose square is less than or equal to the integer given:

Example:

    Assume input is integer 300.
        
    Then the expected output of the function should be 17 since 17 squared is 289 which is strictly less than 300. Note that 18 squared is 324 which is strictly greater than 300, so the number 17 is the correct response.
'''

 
def integer_square_root(number):
    
    low = 0
    high = number

    while low <= high:
        mid = (low + high) // 2
        mid_squared = mid * mid

        if mid_squared <= number:
            low = mid + 1
        else:
            high = mid - 1

    return low - 1

if __name__ == "__main__":
    
    K = 300
    L = 12

    X = integer_square_root(K)
    print(X)

    Y = integer_square_root(L)
    print(Y)
