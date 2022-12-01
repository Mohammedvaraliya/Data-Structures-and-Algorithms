'''
An array is "cyclically sorted" if it is possible to cyclically shift
its entries so that it becomes sorted.

The following list is an example of a cyclically sorted array:

    A = [4, 5, 6, 7, 1, 2, 3]

Write a function that determines the index of the smallest element
of the cyclically sorted array.
'''


def find(array):
    low = 0
    high = len(array) - 1

    while low < high:
        mid = (low + high) // 2
 
        if array[mid] > array[high]:
            low = mid + 1
        elif array[mid] <= array[high]:
            high = mid
    
    return low


if __name__ == "__main__":

    A = [4, 5, 6, 7, 1, 2, 3]
    B = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    
    indx1 = find(A)
    print("Index number is : ", indx1)
    print(A[indx1])

    indx2 = find(B)
    print("Index number is : ", indx2)
    print(B[indx2])

