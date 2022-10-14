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

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        cur_node = self.head
        self.head = new_node
        new_node.next = cur_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def remove_duplicates(self):
        cur_node = self.head
        prev = None
        dup_values = dict()
        while cur_node:
            if cur_node.data in dup_values:
                # Remove node:
                prev.next = cur_node.next
                cur_node = None
            else:
                # Have not encountered element before
                dup_values[cur_node.data] = 1
                prev = cur_node
            cur_node = prev.next


llist = SinglyLinkedList()
llist.append(1)
llist.append(2)
llist.append(7)
llist.append(2)
llist.append(1)
llist.append(7)
llist.append(1)

llist.print_list()
print("\n")

llist.remove_duplicates()
llist.print_list()