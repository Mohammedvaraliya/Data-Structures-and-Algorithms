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

    def insert_after(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                new_node.next = nxt
                cur.next = new_node
            cur = cur.next

        if cur is None:
            print("Previous Node is not present in the list")
            return

    def delete_node(self, key):

        # Case 1
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        # Case 2
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            print("The Node is not present in the list")
            return

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            count += 1
            cur_node = cur_node.next

        if cur_node is None:
            print("The Node is not present in the list")
            return

        prev.next = cur_node.next
        cur_node = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def print_holder(self, node, name):
        if node is None:
            print(name + " : None ")
        else:
            print(name + " : " + node.data)

    def reverse_iterative(self):

        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev

            self.print_holder(prev, "PREV")
            self.print_holder(cur, "CUR")
            self.print_holder(nxt, "NXT")
            print("\n")

            prev = cur
            cur = nxt

        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur = self.head, prev = None)


if __name__ == "__main__":

    llist = SinglyLinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")

    llist.reverse_iterative()
    llist.print_list()
    print("\n")
    llist.reverse_recursive()
    llist.print_list()
