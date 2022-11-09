'''
Given:
    An array of non-negative digits that represent a decimal integer.

Problem:
    Add one to the integer. Assume the solution still works even if implemented in a language with finite-precision arithmetic.
'''
 
A = [1, 4, 9]
B = [9, 9, 9]
ex1 = ''.join(map(str, A))
print(ex1)
print(int(ex1) + 1)
print("\n")
ex2 = ''.join(map(str, B))
print(ex2)
print(int(ex2) + 1)
print("\n")


def plus_one(array):
    array[-1] += 1
    for i in reversed(range(1, len(array))):
        if array[i] != 10:
            break
        array[i] = 0
        array[i - 1] += 1
    if array[0] == 10:
        array[0] = 1
        array.append(0)
    return array


if __name__ == "__main__":
    A = [1, 4, 9]
    B = [9, 9, 9]

    X = plus_one(A)
    print(X)

    Y = plus_one(B)
    print(Y)


