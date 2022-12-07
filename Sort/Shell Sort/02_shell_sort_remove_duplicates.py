def shell_sort(arr):
    size = len(arr)
    div = 2
    gap = size // div

    while gap > 0:
        index_to_delete = []
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] >= anchor:
                if arr[j - gap] == anchor:
                    index_to_delete.append(j)
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = anchor

        index_to_delete = list(set(index_to_delete))
        index_to_delete.sort()

        if index_to_delete:
            for i in index_to_delete[-1::-1]:
                del arr[i]

        div *= 2
        size = len(arr)

        gap = gap // div


if __name__ == "__main__":

    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9,  5, 8, 3]
    shell_sort(elements)
    print(elements)
