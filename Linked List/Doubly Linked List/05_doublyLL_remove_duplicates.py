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

    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                
                # Case 2:
                else:
                    nxt = cur.next
                    cur.next = None
                    cur = None
                    nxt.prev = None
                    self.head = nxt
                    return

            elif cur == node:
                # Case 3:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return

                # Case 4:
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def remove_duplicates(self):
        cur = self.head
        seen = dict()
        while cur:
            if cur.data not in seen:
                seen[cur.data] = 1
                cur = cur.next
            else:
                nxt = cur.next
                self.delete_node(cur)
                cur = nxt







dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(1)
dllist.append(4)
dllist.append(2)
dllist.append(3)
dllist.append(6)
dllist.append(1)
dllist.append(3)
dllist.append(4)
dllist.append(3)
dllist.append(4)
dllist.append(5)
dllist.append(7)
dllist.append(7)
dllist.append(5)
dllist.append(7)


dllist.print_list()
print("\n")

dllist.remove_duplicates()
dllist.print_list()
