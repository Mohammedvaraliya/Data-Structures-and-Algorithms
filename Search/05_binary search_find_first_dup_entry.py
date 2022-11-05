'''
writing a function that takes an array of sorted integers and a key and returns the index of the first occurrence of that key from the array.

Example:
    Index:      0   1   2   3    4    5    6    7    8    9
    Array:   [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    Target:  108

    Returns index 3 since 108 appear for the first time at index 3.
'''


def find_meth1(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return "No element exist"

def find_meth2(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if array[mid] < target:
            low = mid + 1
        
        elif array[mid] > target:
            high = mid - 1

        else:
            if mid - 1 < 0:
                return mid
            if array[mid - 1] != target:
                return mid
            high = mid - 1

    return "No element exist"






if __name__ == "__main__":
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    target = 108

    X = find_meth1(A, target)
    print(X)

    Y = find_meth2(A, target)
    print(Y)
