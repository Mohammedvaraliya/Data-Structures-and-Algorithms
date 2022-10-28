'''
A fixed point in an array "A" is an index "i" such that A[i] is equal to "i".

Given an array of n distinct integers sorted in ascending order, write a function that returns a "fixed point" in the array. If there is not a 
fixed point return "None".

Problem is to find only one fixed point.

Examples:
    # Fixed point is 3:
    A = [-10, -5, 0, 3, 7]

    # Fixed point is 0:
    A = [0, 2, 5, 8, 17]

    # No fixed point. Return "None":
    A = [-10, -5, 3, 4, 7, 9]
'''

# Time complexity : O(n)
# Space complexity : O(1)
def find_fixed_point_linear(array):
    for i in range(len(array)):
        if array[i] == i:
            return array[i]
    return None

# Time Complexity : O(log n)
# Space Complexity : O(1)
def find_fixed_point(array):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] < mid:
            low = mid + 1

        elif array[mid] > mid:
            high = mid - 1

        else:
            return array[mid]
        
    return None

        

if __name__ == "__main__":
    A = [-10, -5, 0, 3, 7]
    B = [0, 2, 5, 8, 17]
    C = [-10, -5, 3, 4, 7, 9]

    print(find_fixed_point_linear(A))
    print(find_fixed_point_linear(B))
    print(find_fixed_point_linear(C))
    print("\n")

    print(find_fixed_point(A))
    print(find_fixed_point(B))
    print(find_fixed_point(C))