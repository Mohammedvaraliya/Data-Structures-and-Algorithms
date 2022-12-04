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

    Merge sort is similar to the quick sort algorithm as it uses the divide and conquer approach to sort the elements. 
    It is one of the most popular and efficient sorting algorithm. It divides the given list into two equal halves, 
    calls itself for the two halves and then merges the two sorted halves. 
    We have to define the merge() function to perform the merging.

    The sub-lists are divided again and again into halves until the list cannot be divided further. 
    Then we combine the pair of one element lists into two-element lists, sorting them in the process. 
    The sorted two-element pairs is merged into the four-element lists, and so on until we get the sorted list.

    
