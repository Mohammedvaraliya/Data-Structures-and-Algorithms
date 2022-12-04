# Data-Structures And Algorithms


### 01. Merge Sort Two Sorted List

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
    
### 01. Merge Sort: One Unsorted List

    Merge Sort: One Unsorted List
    ....