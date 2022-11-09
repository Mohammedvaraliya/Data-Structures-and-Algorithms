'''
Given:
    An array of non-negative digits that represent a decimal integer.

Problem:
    Add one to the integer. Assume the solution still works even if implemented in a language with finite-precision arithmetic.
'''

A = [1, 4, 9]

S = ''.join(map(str, A))
print(S)
print(int(S) + 1)


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


print(plus_one(A))


