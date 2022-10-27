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

    def __len__(self):

        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        
        return count

    def split_list(self):
        size = len(self)

        if size == 0:
            return "No node present in the list"

        if size == 1:
            return self.head
        
        mid = size//2
        count = 0

        prev = None
        cur = self.head
        
        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        split_cllist = CircularLinkedList()
        head_of_the_split = cur
        while cur.next != self.head:
            split_cllist.append(cur.data)
            cur = cur.next
        split_cllist.append(cur.data)
        cur.next = head_of_the_split

        self.print_list()
        print("\n")
        split_cllist.print_list()


cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.append("E")
cllist.append("F")

cllist.print_list()
print("\n")

# print(len(cllist))
cllist.split_list()

