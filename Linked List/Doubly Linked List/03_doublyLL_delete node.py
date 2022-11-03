class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def delete(self, key):
        pass


dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)

dllist.print_list()
