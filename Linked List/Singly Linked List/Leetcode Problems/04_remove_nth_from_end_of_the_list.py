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

    def removeNthFromEnd(self, n):

        dummy = Node(0)
        dummy.next = self.head

        left = dummy
        right = self.head

        while right and n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next

        # Delete the nth node
        n_node = left.next
        left.next = left.next.next
        n_node = None



if __name__ == "__main__":

    llist = SinglyLinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.append(5)

    llist.print_list()
    print("\n")

    llist.removeNthFromEnd(2)

    llist.print_list()
    print("\n")

    llist.removeNthFromEnd(1)

    llist.print_list()

    