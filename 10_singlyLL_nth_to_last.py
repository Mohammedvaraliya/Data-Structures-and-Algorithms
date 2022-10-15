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

    def len_of_list(self):

        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count

    def print_nth_from_last_method1(self, n):
        
        # method-1:
        total_len = self.len_of_list()

        cur = self.head
        while cur:
            if total_len == n:
                print(cur.data)
                return cur
            total_len -= 1
            cur = cur.next
        if cur is None:
            return "No node present"

    def print_nth_from_last_method2(self, n):
        
        # method-2
        p = self.head
        q = self.head

        count = 0
        while q and count < n:
            q = q.next
            count += 1


        if not q and count < n:
            print(str(n) + " is greater than the number of nodes in list. ")
            return

        while p and q:
            p = p.next
            q = q.next
        return p.data


llist = SinglyLinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.append("F")

llist.print_list()
print("\n")

print(llist.print_nth_from_last_method1(3))
print("\n")
print(llist.print_nth_from_last_method2(3))