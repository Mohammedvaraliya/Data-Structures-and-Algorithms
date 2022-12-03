# Data-Structures And Algorithms


### 01. Quick Sort: Hoare Partition

    Quick Sort : Hoare Partition
    Hoare partition is an algorithm that is used to partition an array about a pivot. 

    In the Hoare partition scheme, usually the first element of the list is chosen as the pivot element.

    All elements smaller than the pivot are on it's left (in any order) and all elements greater than the pivot are on it's right (in any order).

    Example:
    given array:

                elements = [11, 9, 29, 7, 2, 15, 28]
            
    let pivot is the first element of the array i.e pivot = 11
    let initialize two pointer start and end.

    start is the pointer after the pivot i.e start = 9
    end is the last element from the array i.e end = 28

    perform while loop such as start is less than end.
    a = check if element[start] <= pivot
            i.e 11 is less or equal to 11 -> yes it is equal

    b = increment start with 1

    now start is 1

    repeat step a and b until start > pivot



### 02. Quick Sort: Lomuto Partition

    Quick Sort: Lomuto Partition
    Lomuto partition scheme, which is used in the famous Quicksort algorithm. 
    It is an algorithm to partition an array into two parts based on a given condition.

    In the Lomuto partition scheme, usually the last element of the list is chosen as the pivot element.