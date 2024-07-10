# Shell Sort Data-Structures and Algorithms

### 01. Shell Sort

    Shell Sort
    Shell sort is mainly a variation of Insertion Sort.
    In insertion sort, we move elements only one position ahead.
    When an element has to be moved far ahead, many movements are involved.
    The idea of ShellSort is to allow the exchange of far items.
    In Shell sort, we make the array h-sorted for a large value of h.
    We keep reducing the value of h until it becomes 1.
    An array is said to be h-sorted if all sublists of every h'th element are sorted.

### 02. Shell Sort: Remove Duplicates

    Shell Sort: Remove Duplicates
    It will remove the duplicates from the list while sorting

    Example:
            index_no:   0  1  2  3  4  5  6  7  8  9  10 11 12
            elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]

    Here at index no 1 and 7 have the element with value 1
    So, it will remove one element from index 1 and 7

    At index no 0, 4, and 8 have the element with value 2
    So, it will remove two element from index no 0, 4, and 8

    Final sorted array will look like

                            [0, 1, 2, 3, 5, 7, 8, 9]
