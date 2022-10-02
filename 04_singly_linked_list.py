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

    def len_iterative(self):

        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):

        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 and curr_2:
            print("No Nodes found")
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

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

    # def reverse_recursive(self):

    #     def _reverse_recursive(cur, prev):



llist = SinglyLinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.insert_after("D", "S")

print(llist.len_iterative())

llist.prepend("E")

llist.delete_node("A")
llist.delete_node_at_pos(1)

llist.print_list()

print(llist.len_recursive(llist.head))

print("\n\n")

swappingNode = SinglyLinkedList()
swappingNode.append("A")
swappingNode.append("B")
swappingNode.append("C")
swappingNode.append("D")

swappingNode.swap_nodes("A", "D")

swappingNode.print_list()

print("\n\n")

llist3 = SinglyLinkedList()
llist3.append("A")
llist3.append("B")
llist3.append("C")
llist3.append("D")

llist3.reverse_iterative()
llist3.print_list()
