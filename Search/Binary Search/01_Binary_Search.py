from calculate_time_decorator import time_it

@time_it
# Linear Search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            print(f"At index Number :",i)
            return True

    return False

@time_it
# Iterative Binary Search
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low+high) // 2
        if target == data[mid]:
            return True
        elif(target < data[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return False

# Recursive Binary Search
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif(target < data[mid]):
            return binary_search_recursive(data, target, low, mid - 1)
        else:
            return binary_search_recursive(data, target, mid + 1, high)




if __name__ == "__main__":

    data = [2,4,5,6,7,8,55,65,76,86,90,89,90,111,209,879]
    target = 209

    low = 0
    high = len(data) - 1

    # Finding the mid point
    mid = (low + high) // 2
    print(data[mid])
    print("\n")

    print(linear_search(data, target))
    print("\n")

    print(binary_search_iterative(data, target))
    print(binary_search_recursive(data, target, 0, len(data) - 1))
    print("~"*20, "end", "~"*20)
    print("\n")

    data = [i for i in range(100002)]
    target = 100001

    low = 0
    high = len(data) - 1

    # Finding the mid point
    mid = (low + high) // 2
    print(data[mid])
    print("\n")

    print(linear_search(data, target))
    print("\n")

    print(binary_search_iterative(data, target))
    print(binary_search_recursive(data, target, 0, len(data) - 1))




