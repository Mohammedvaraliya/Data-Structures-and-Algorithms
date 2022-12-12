'''
# Function to find minimum element from array
def find_min_element(arr):
    min = float('inf')
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min
'''



def selection_sort(arr):

    size = len(arr)
    for i in range(size - 1):
        min_index = i
        for j in range(min_index + 1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]





if __name__ == "__main__":

    elements = [78, 12, 15, 8, 61, 53, 23, 27]
    # elements = [64, 25, 12, 22, 11]
    selection_sort(elements)
    print(elements)