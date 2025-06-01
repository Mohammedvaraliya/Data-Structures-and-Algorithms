'''
Assign tasks to workers such that the time it takes to complete all tasks is minimized.
here, the elements in an array is duration of time
'''

A = [6, 3, 2, 7, 5, 5]

A = sorted(A)
print(A)

for i in range(len(A)//2):
    print(A[i], A[~i])
    # print(A[i], A[-i-1])

print("\n")


# Using function
Array = [6, 3, 2, 7, 5, 5]

def optimal_task_assignment(array):

    array = sorted(array)
    print(array)
    m = 1

    for i in range(len(array)//2):
        print(f"Worker {m} : ",array[i], array[~i])
        m += 1


if __name__ == "__main__":
    optimal_task_assignment(Array)