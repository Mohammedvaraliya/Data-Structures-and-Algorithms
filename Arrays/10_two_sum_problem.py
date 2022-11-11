'''
Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''


# Time Complexity : O(n^2)
# Space Complexity : O(1)
def two_sum_bruteforce(array, target):

    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                print(f"[{array[i]}, {array[j]}]")
                return True
    return False


# Time Complexity : O(n)
# Space Complexity : O(n)
def two_sum_hash_table(array, target):
    ht = dict()
    for i in range(len(array)):
        if array[i] in ht:
            print(f"[{ht[array[i]]}, {array[i]}]")
            return True
        else:
            ht[target - array[i]] = array[i]

    return False


# Time Complexity : O(n)
# Space Complexity : O(1)
def two_sum(array, target):
    i = 0
    j = len(array) - 1
    
    while i <= j:
        if array[i] + array[j] == target:
            print(f"[{array[i]}, {array[j]}]")
            return True
        elif array[i] + array[j] < target:
            i += 1
        else:
            # the case where array[i] + array[j] > target:
            j -= 1

    return False



if __name__ == "__main__":

    A = [-2, 1, 2, 4, 7, 11]
    target = 13

    X = two_sum_bruteforce(A, target)
    print(X)
    print("\n")

    Y = two_sum_hash_table(A, target)
    print(Y)
    print("\n")

    Z = two_sum(A, target)
    print(Z)
    print("\n")

