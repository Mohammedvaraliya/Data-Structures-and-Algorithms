class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev, curr = None, head

    # Time Complexity : O(n)
    # Space Complexity : O(1)
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev

def recursive_reverseList(head):
    
    if not head:
        return None
    
    newHead = head
    if head.next:
        newHead = recursive_reverseList(head.next)
        head.next.next = head
    head.next = None

    return newHead

if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Pass the head to the reverseList function
    reversed_head1 = reverseList(head)

    # Print the reversed linked list
    current = reversed_head1
    while current:
        print(current.val)
        current = current.next