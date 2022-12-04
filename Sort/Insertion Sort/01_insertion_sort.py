def insertion_sort(elements):
    
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = anchor




if __name__ == "__main__":

    elements = [
        [11, 9, 29, 7, 2, 15, 28],
        [12, 11, 13, 5, 6],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for element in elements:
        insertion_sort(element)
        print(element)