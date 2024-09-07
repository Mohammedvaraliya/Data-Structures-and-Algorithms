# Queue Data-Structures and Algorithms

## 01. Queue Data Structure

    Queue Data Structure.
    Queue is FIFO(First In First Out) or LILO(Last In Last Out) data structure.

    Example:
            queue = []

    Now, insert an element 1 at index 0

            queue = [1]

    Now, insert some more elements at index 0
    So, every element which was placed on index 0 will push by 1 when you try to insert at index 0
    queue will look like

            queue = [5, 4, 3, 2, 1]

    if i use pop() to queue
    it will return the last element in the list which is 1
    hence FIFO proved

---

## 02. Queue Data Structure : Using dequeue

    Queue Data Structure : Using dequeue
    deque is using Doubly Linked List data structure to store the element.

---

## 03. Queue Data Structure : Producer Consumer Problem

    Queue Data Structure : Producer Consumer Problem
    This problem is a producer,consumer problem where producer thread is producing data whereas consumer
    thread is consuming the data which has already produced.

---

## 04. Queue Data Structure : Print Binary Numbers From 1 to 10 Using Queue

    Queue Data Structure : Print Binary Numbers From 1 to 10 Using Queue
    The binary number In mathematics and in computing systems, a binary digit, or bit, is the smallest unit of data.

    declare two different stings
    s1 = "0"
    s2 = "1"

    enqueue() element "1" to queue and print front() of queue which returns [-1] element from the queue.

    Now, enqueue() front + s1, and front + s2 to th queue.

    Now dequeue() the element from queue which removes the first entered element.

    print the front of the queue

    repeat above steps to nth times.

    Output:

        The 0 number is :  1
        The 1 number is :  10
        The 2 number is :  11
        The 3 number is :  100
        The 4 number is :  101
        The 5 number is :  110
        The 6 number is :  111
        The 7 number is :  1000
        The 8 number is :  1001
        The 9 number is :  1010

    Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are second number (i.e. 10) + 0 and second
    number (i.e. 10) + 1.

    For more clarification, please take a look on my code.

---
