def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def partition(elements, start, end):
    pivot_index = end
    pivot = elements[pivot_index]
    partition_index = start

    for i in range(start, end):
        if elements[i] <= pivot:
            swap(i, partition_index, elements)
            partition_index += 1
        
    swap(partition_index, end, elements)

    return partition_index


def quick_sort(elements, start, end):
    if len(elements)== 1:
        return
    if start < end:
        partition_index = partition(elements, start, end)
        quick_sort(elements, start, partition_index-1) # Left partition
        quick_sort(elements, partition_index+1, end) # Right Partition



if __name__ == "__main__":

    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)

    