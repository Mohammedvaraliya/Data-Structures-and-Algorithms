'''
Given two arrays, A and B, determine their intersection. That is, what elements are common to A and B?
'''

A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

print(set(A))
print(set(B))

print(set(A).intersection(B))
print("\n")


# Using function
def intersect_sorted_array(array1, array2):
    i = 0
    j = 0
    intersection = []

    while i < len(array1) and j < len(array2):
        if array1[i] == array2[j]:
            if i == 0 or array1[i] != array1[i-1]:
                intersection.append(A[i])
            i += 1
            j += 1
        elif array1[i] < array2[j]:
            i += 1
        else:               # array1[i] > array2[j]
            j += 1
    
    return intersection



print(intersect_sorted_array(A, B))



