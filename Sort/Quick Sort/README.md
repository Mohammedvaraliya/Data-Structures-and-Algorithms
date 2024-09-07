# Quick Sort Data-Structures and Algorithms

## 01. Quick Sort: Hoare Partition

    Quick Sort : Hoare Partition
    Hoare partition is an algorithm that is used to partition an array about a pivot.

    In the Hoare partition scheme, usually the first element of the list is chosen as the pivot element.

    All elements smaller than the pivot are on it's left (in any order) and all elements greater than the pivot are on it's right (in any order).

    Example:
    given array:

                elements = [11, 9, 29, 7, 2, 15, 28]

    let pivot is the first element of the array i.e index of pivot = 0 and value is 11
    let initialize two pointer start and end.

    start is the pointer after the pivot i.e index of start = 0
    end is the last element from the array i.e index of end = 6

    perform while loop such that start is less than end.

        i)  perform while loop such that start is less than or equal to pivot.
            a = check if element[start] <= pivot
                    i.e 11 is less or equal to 11 -> yes it is equal

            b = increment start with 1

            now start is 1

            repeat step a and b until start <= pivot

        ii) perform while loop such that end is greater than pivot.
            a = check if element[start] <= pivot
                    i.e 11 is less or equal to 11 -> yes it is equal

            b = decrement end with 1

            now end is 5

            repeat step a and b until end > pivot

    break the loop

    And swap start with end

    repeat above till start < end

    final sorted array will look like:

                           [2, 7, 9, 11, 15, 28, 29]

---

## 02. Quick Sort: Lomuto Partition

    Quick Sort: Lomuto Partition
    Lomuto partition scheme, which is used in the famous Quicksort algorithm.
    It is an algorithm to partition an array into two parts based on a given condition.

    In the Lomuto partition scheme, usually the last element of the list is chosen as the pivot element.

    Example:
    given array:

                elements = [11, 9, 29, 7, 2, 15, 28]

    let pivot is the last element of the array i.e index of pivot = 6 and value is 28
    let initialize two pointer start and end.

    start is the pointer after the pivot i.e index of start = 0
    end is the last element from the array i.e index of end = 6

---
