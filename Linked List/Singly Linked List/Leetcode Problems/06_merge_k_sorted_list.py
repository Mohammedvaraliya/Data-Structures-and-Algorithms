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


def mergeKLists(self, lists):
    if not lists or len(lists) == 0:
        return None
    
    while len(lists) > 1:
        mergedLists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i].head  # Access the head of the linked list
            l2 = lists[i + 1].head if (i + 1) < len(lists) else None  # Access the head of the linked list
            mergedLists.append(self.mergeList(l1, l2))
        lists = mergedLists
    return lists[0]


if __name__ == "__main__":
    input_list = []

    list1 = ListNode(1)
    list1.next = ListNode(4)
    list1.next.next = ListNode(5)
    input_list.append(list1)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    input_list.append(list2)

    list3 = ListNode(2)
    list3.next = ListNode(6)
    input_list.append(list3)

    print(input_list)
