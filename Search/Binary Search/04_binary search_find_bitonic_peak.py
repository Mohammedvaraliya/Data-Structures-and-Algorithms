'''
Define a bitonic sequence as a sequence of integers such that:
    x_1 <= ... <= x_k >= ... >= x_n-1 for some k, 0 <= k < n.

For example:
    1, 2, 3, 4, 5, 4, 3, 2, 1

is a bitcoin sequence. write a program to find the largest element in
such a sequence. In the above example, the program should return "5".

we assume that such a peak element exists.
'''



def find_highest_number(array):
    low = 0
    high = len(array) - 1
    
    # Require at least 3 element for a valid bitonic sequence
    if len(array) < 3:
        return "The array must be length of 3 or more..."

    while low <= high:
        mid = (low + high) // 2

        mid_left = array[mid - 1] if mid - 1 > 0 else float("-inf")
        mid_right = array[mid + 1] if mid + 1 < len(array) else float("inf")

        if mid_left < array[mid] and mid_right > array[mid]:
            low = mid + 1

        elif mid_left > array[mid] and mid_right < array[mid]:
            high = mid - 1

        if mid_left < array[mid] and mid_right < array[mid]:
            return array[mid]



if __name__ == "__main__":
    # Peak element is "5"
    A = [1, 2, 3, 4, 5, 4, 3, 2, 1]

    # Peak element is "4"
    B = [1, 2, 3, 4, 1]

    # Peak element is "6"
    C = [1, 6, 5, 4, 3, 2, 1]

    X = find_highest_number(A)
    print(X)

    Y = find_highest_number(B)
    print(Y)

    Z = find_highest_number(C)
    print(Z)


