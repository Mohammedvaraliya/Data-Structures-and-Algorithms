def count_element_less_than_b(A, B):
    left, right = 0, len(A)

    while left < right:
        mid = (right + left) // 2

        if A[mid] <= B:
            left = mid + 1

        else:
            right = mid

    return left



if __name__ == "__main__":

    A1 = [1, 3, 4, 4, 6]
    B1 = 4
    print(count_element_less_than_b(A1, B1))

    A2 = [1, 2, 5, 5]
    B2 = 3
    print(count_element_less_than_b(A2, B2))