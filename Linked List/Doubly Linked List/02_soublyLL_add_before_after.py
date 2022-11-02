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

    def add_after_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
            cur = cur.next
                

    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
            cur = cur.next
    


dllist1 = DoublyLinkedList()
dllist1.append(1)
dllist1.append(2)
dllist1.append(3)
dllist1.append(4)

dllist1.add_after_node(1, 11)
dllist1.add_after_node(2, 12)
dllist1.add_after_node(4, 14)

dllist1.print_list()
print("\n")

dllist2 = DoublyLinkedList()
dllist2.append(1)
dllist2.append(2)
dllist2.append(3)
dllist2.append(4)

dllist2.add_before_node(1, 11)
dllist2.add_before_node(2, 12)
dllist2.add_before_node(4, 14)

dllist2.print_list()
