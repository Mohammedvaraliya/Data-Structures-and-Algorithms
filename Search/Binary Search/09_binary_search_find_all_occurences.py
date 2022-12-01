def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low+high) // 2
        if target == data[mid]:
            return mid
        elif(target < data[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return False

def find_all_occurances(data, target):
    index = binary_search(data, target)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if data[i] == target:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(data):
        if data[i] == target:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)


if __name__ == "__main__":
    data = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    target = 15

    print(binary_search(data, target))

    indices = find_all_occurances(data, target)
    print(f"Indices of occurences of {target} are {indices}")