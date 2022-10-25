class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):

        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.head.next = self.head

        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = new_node
        new_node.next = self.head


    def prepend(self, data):
        
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        
        while cur.next != self.head:
            cur = cur.next
        cur.next = new_node
        self.head = new_node

    def remove(self, key):

        if self.head.data == key:
            cur = self.head
            nxt = self.head.next
            while cur.next != self.head:
                cur = cur.next
            cur.next = nxt
            self.head = nxt
            cur = None
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next

    def print_list(self):

        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break


cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")

cllist.print_list()
print("\n")

cllist.remove("A")
cllist.remove("B")
cllist.remove("C")
cllist.print_list()
