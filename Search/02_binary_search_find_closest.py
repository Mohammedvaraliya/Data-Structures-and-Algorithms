'''
given a sorted array and a target number. we need to find a number in the array that is closest to the target number.

The array may contain duplicate values and negative numbers.

Example 1:
    Input : arr[] = {1, 2, 4, 5, 6, 6, 8, 9}
    Target number = 11
    Output : 9
    9 is closest to 11 in given array

Example 2:
    Input :arr[] = {2, 5, 6, 7, 8, 8, 9};
    Target number = 4
    Output : 5
'''

def find_cosest_num(array, target):

    min_diff = float("inf")
    low = 0
    high = len(array) - 1
    closest_num = None
    
    # Edge cases for empty list or 
    # When the list is only one element.
 
    if len(array) == 0:
        return None
     
    if len(array) == 1:
        return array[0]
    
    if len(array) == 2:
        if abs(array[0]-target)> abs(array[1]-target):
            return array[1]
        else:
            return array[0]
    
    while low <= high:
        mid = (low + high) // 2

        # Ensure that we don't read beyond the bound of the list
        # And obtain the left and right difference values 
        if mid + 1 < len(array):
            min_diff_right = abs(array[mid + 1] - target)
        
        if mid > 0:
            min_diff_left = abs(array[mid - 1] - target)

        # Check if the absolute value between left and right
        # Elements are smaller than any seen prior.
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = array[mid + 1]

        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = array[mid - 1]

        # Move the mid point accordingly as is done
        # Via binary search.
        if array[mid] < target:
            low = mid + 1

        elif array[mid] > target:
            high = mid - 1

        # If the element is the targert itself, the closest 
        # Number to is itself
        else:
            return array[mid]
        
    return closest_num




if __name__ == "__main__":
    A = [1, 2, 4, 5, 6, 6, 8, 9]
    B = [2, 5, 6, 7, 8, 8, 9]
    C = [1, 2, 3, 4, 11, 14, 16, 17, 20]
    target1 = 11
    target2 = 4
    target3 = 10

    X = find_cosest_num(A, target1)
    print(X)

    Y = find_cosest_num(B, target2)
    print(Y)

    Z = find_cosest_num(C, target3)
    print(Z)