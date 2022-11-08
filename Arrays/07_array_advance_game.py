'''
"array advance game"

you are given an array of non-negative integers. For example:
 
 [3,3,1,0,2,0,1].

Each number represents the maximum you can advance in the array. 

Question:
Is it possible to advance from the start of the array to the last element?
'''

def array_advance(array):
    furtest_reached = 0
    last_idx = len(array) - 1
    i = 0
    while i <= furtest_reached and furtest_reached < last_idx:
        furtest_reached = max(furtest_reached, array[i] + i)
        i += 1

    return furtest_reached >= last_idx


if __name__ == "__main__":
    A = [3, 3, 1, 0, 2, 0 , 1]
    print(array_advance(A))

    B = [3, 2, 0, 0, 2, 0, 1]
    print(array_advance(B))