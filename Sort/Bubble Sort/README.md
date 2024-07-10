# Bubble Sort Data-Structures and Algorithms

### 01. Bubble Sort

    Bubble Sort
    Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the
    wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

    Example:

    Input: arr[] = {5, 1, 4, 2, 8}

    First Pass:

    Bubble sort starts with very first two elements, comparing them to check which one is greater.
        ( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
        ( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
        ( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
        ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

    Second Pass:

        Now, during second iteration it should look like this:
            ( 1 4 2 5 8 ) –> ( 1 4 2 5 8 )
            ( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2
            ( 1 2 4 5 8 ) –> ( 1 2 4 5 8 )
            ( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 )

### 02. Bubble Sort Using Key

    Bubble Sort Using Key

    Implement bubble_sort function such that it can sort following list of transactions,

    elements = [
        { 'name': 'varaliya',   'amount': 1000, 'device': 'iphone-14'},
        { 'name': 'mohammed', 'amount': 400,  'device': 'google pixel'},
        { 'name': 'sameer',  'amount': 200,  'device': 'vivo'},
        { 'name': 'subhashish',  'amount': 800,  'device': 'iphone-12'},
    ]

    bubble_sort function should take key from an elements record and sort the list as per that key. For example,

    bubble_sort(elements, key='amount')
    This will sort elements by amount and your sorted list will look like,

    elements = [
        { 'name': 'sameer',  'amount': 200,  'device': 'vivo'},
        { 'name': 'mohammed', 'amount': 400,  'device': 'google pixel'},
        { 'name': 'subhashish',  'amount': 800,  'device': 'iphone-12'},
        { 'name': 'varaliya',   'amount': 1000, 'device': 'iphone-14'},
    ]

    But if you call it like this,

    bubble_sort(elements, key='name')
    This will sort elements by name and your sorted list will look like,

    elements = [
        { 'name': 'mohammed', 'amount': 400,  'device': 'google pixel'},
        { 'name': 'sameer',  'amount': 200,  'device': 'vivo'},
        { 'name': 'subhashish',  'amount': 800,  'device': 'iphone-12'},
        { 'name': 'varaliya',   'amount': 1000, 'device': 'iphone-14'},
    ]

    and if you call it like this,

    bubble_sort(elements, key='device')
    This will sort elements by device and your sorted list will look like,

    elements = [
        { 'name': 'mohammed', 'amount': 400,  'device': 'google pixel'},
        { 'name': 'varaliya',   'amount': 1000, 'device': 'iphone-14'},
        { 'name': 'subhashish',  'amount': 800,  'device': 'iphone-12'},
        { 'name': 'sameer',  'amount': 200,  'device': 'vivo'},
    ]
