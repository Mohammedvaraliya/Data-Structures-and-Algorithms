# Merge Sort Data-Structures and Algorithms

## 01. Merge Sort Two Sorted List

    Merge Sort Two Sorted List
    The key idea to note here is that both the arrays are sorted.
    We have to create one array from two sorted array which should be sorted.

    Example:

                a = [5, 8, 12, 56]
                b = [7, 9, 45, 51]

        These are two sorted array

        Create an auxilary empty array.

        Put two pointers i and j and initialise them to 0.

        Pointer i points to the first array, whereas pointer j points to the second array.

        Traverse both the array simultaneously using the pointers, and pick the smallest elements
        among both the array and append it into the auxiliary array.

        Increment the pointers.

        After traversal, return the merged array.

        Our array will look like:

                [5, 7, 8, 9, 12, 45, 51, 56]

---

## 02. Merge Sort: One Unsorted List

    Merge Sort: One Unsorted List

    Merge sort is similar to the quick sort algorithm as it uses the divide and conquer approach to sort the elements.
    It is one of the most popular and efficient sorting algorithm. It divides the given list into two equal halves,
    calls itself for the two halves and then merges the two sorted halves.
    We have to define the merge() function to perform the merging.

    The sub-lists are divided again and again into halves until the list cannot be divided further.
    Then we combine the pair of one element lists into two-element lists, sorting them in the process.
    The sorted two-element pairs is merged into the four-element lists, and so on until we get the sorted list.

    Example:

                arr = [10, 3, 15, 7, 8, 23, 98, 29]

    make the halft list until only one elements left

                      [10, 3, 15, 7]             [8, 23, 98, 29]

                     [10, 3]    [15, 7]        [8, 23]     [98, 29]

                 [10]   [3]   [15]   [7]   [8]   [23]   [98]    [29]

    Now every single array is sorted.
    After dividing the array into smallest units, start merging the elements again based on comparison of size of elements
    Firstly, compare the element for each list and then combine them into another list in a sorted manner.

                       [3, 10]   [7, 15]    [8, 23]   [29, 98]

                       [3, 7, 10, 15]             [8, 23. 29, 98]

                            [3, 7, 8, 10, 15, 23, 29, 98]

---

## 03. Merge Sort: Using Key

    Merge Sort: Using Key

    Modify merge_sort function such that it can sort following list of athletes as per the key given,

    elements = [
        {'name': 'varaliya',   'age': 17, 'time_hours': 1},
        {'name': 'mohammed', 'age': 12,  'time_hours': 3},
        {'name': 'sameer',  'age': 21,  'time_hours': 2.5},
        {'name': 'subhashish',  'age': 24,  'time_hours': 1.5},
    ]

    merge_sort function should take key from an elements and sort the list as per that key. For example,

    merge_sort(elements, key='time_hours', descending=True)
    This will sort elements by time_hours and your sorted list will look like,

    elements = [
        {'name': 'mohammed', 'age': 12,  'time_hours': 3},
        {'name': 'sameer',  'age': 21,  'time_hours': 2.5},
        {'name': 'subhashish',  'age': 24,  'time_hours': 1.5},
        {'name': 'varaliya',   'age': 17, 'time_hours': 1},
    ]
    But if you call it like this,

    merge_sort(elements, key='time_hours')
    output will be,

    elements = [
            { 'name': 'vedanth',  'age': 17,  'time_hours': 1},
            { 'name': 'chinmay',   'age': 24, 'time_hours': 1.5},
            { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
            { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        ]

---
