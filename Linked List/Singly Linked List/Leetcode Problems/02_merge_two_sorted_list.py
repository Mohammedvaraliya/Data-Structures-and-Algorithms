class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):

    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return dummy.next




if __name__ == "__main__":

    # Create the first sorted linked list: [1 -> 2 -> 4]
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    # Create the second sorted linked list: [1 -> 3 -> 4]
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    # Merge the two sorted linked lists
    merged_list = mergeTwoLists(list1, list2)

    # Print the merged list
    current = merged_list
    while current:
        print(current.val)
        current = current.next