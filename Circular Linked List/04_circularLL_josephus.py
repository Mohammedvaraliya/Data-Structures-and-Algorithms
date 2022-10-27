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

    def remove_node(self, node):

        if self.head == node:
            cur = self.head
            nxt = self.head.next
            while cur.next != self.head:
                cur = cur.next
            cur.next = nxt
            self.head = nxt
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def josephus_circle(self, step):
        cur = self.head

        while len(self) > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            print("Removed : " + str(cur.data))
            self.remove_node(cur)
            cur = cur.next
        



cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)
cllist.append(5)
cllist.append(6)

cllist.print_list()
print("\n")

cllist.josephus_circle(2)
cllist.print_list()

