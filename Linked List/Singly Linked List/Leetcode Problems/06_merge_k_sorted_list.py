import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    
    # Add the first node of each linked list to the min heap
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i))
            lists[i] = lists[i].next
    
    dummy = ListNode()
    curr = dummy
    
    # Process the nodes from the min heap until it's empty
    while heap:
        val, idx = heapq.heappop(heap)
        curr.next = ListNode(val)
        curr = curr.next
        
        # Move to the next node in the linked list from which the current node was extracted
        if lists[idx]:
            heapq.heappush(heap, (lists[idx].val, idx))
            lists[idx] = lists[idx].next
    
    return dummy.next


if __name__ == "__main__":
        
    # Example 1
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)

    lists = [l1, l2, l3]
    result = mergeKLists(lists)

    # Print the merged linked list
    while result:
        print(result.val, end=" ")
        result = result.next
    # Output: 1 1 2 3 4 4 5 6
