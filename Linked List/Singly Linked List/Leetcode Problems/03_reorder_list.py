class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def reorderList(self):
        slow, fast = self.head, self.head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = self.head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            




if __name__ == "__main__":
    
    llist1 = SinglyLinkedList()
    llist1.append(1)
    llist1.append(2)
    llist1.append(3)
    llist1.append(4)

    llist1.print_list()
    print("\n")

    llist1.reorderList()

    llist1.print_list()
    
    llist2 = SinglyLinkedList()
    llist2.append(1)
    llist2.append(2)
    llist2.append(3)
    llist2.append(4)
    llist2.append(5)

    llist2.print_list()
    print("\n")

    llist2.reorderList()

    llist2.print_list()