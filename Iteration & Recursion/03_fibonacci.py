'''
Fibonacci Number:
first 6 fibonacci number is:

                index_num:   0, 1, 2, 3, 4, 5, 6        
                           ---------------------- 
                fibo_num:    0, 1, 1, 2, 3, 5, 8
'''

# Iterative approach
def fib_iterative(n):
    
    num = [0, 1]

    for i in range(2, n+1):
        a = i-1
        b = i-2
        num.append(num[a] + num[b])
    
    return num[n]

# Recursive Approach
def fib_recursive(n):

    if n == 0 or n == 1:
        return n

    return fib_recursive(n - 1) + fib_recursive(n - 2)

if __name__ == "__main__":
    print(fib_iterative(4))
    print(fib_recursive(4))