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

    def is_circular_linked_list(self, input_list):
        cur = input_list.head
        while cur.next:
            cur = cur.next
            if cur.next == input_list.head:
                return True
        return False

        



cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)

llist = SinglyLinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print("Circular Linked List")
cllist.print_list()
print("\n")

print("Singly Linked List")
llist.print_list()
print("\n")

print(cllist.is_circular_linked_list(cllist))
print(cllist.is_circular_linked_list(llist))