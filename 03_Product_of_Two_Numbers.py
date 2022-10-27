# Given two numbers, find their product using recursion.

x = 5
y = 4

def recursive_Multiply(x, y):

    if x < y:
        return recursive_Multiply(y, x)
    
    if y == 0:
        return 0

    return x + recursive_Multiply(x, y-1)


if __name__ == "__main__":
    print(x*y)
    print(recursive_Multiply(x, y))