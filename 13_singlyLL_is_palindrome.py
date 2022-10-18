'''
Example Palindrome:  RACECAR, RADAR

Example non-palindrome:  TEST, HELLO, ABC
'''


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

    def is_palindrome_meth1(self):
        
        # Method 1
        s = ""
        p = self.head
        while p:
            s += p.data
            p = p.next
        return s == s[::-1]

    def is_palindrome_meth2(self):
        
        # Method 2
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True

    def is_palindrome_meth3(self):

        # Method 3
        p = self.head
        q = self.head
        prev = []

        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1
        q = prev[i - 1]

        count = 1
        while p and count <= i//2 +1:
            if prev[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True




    
llist1 = SinglyLinkedList()
llist1.append("R")
llist1.append("A")
llist1.append("C")
llist1.append("E")
llist1.append("C")
llist1.append("A")
llist1.append("R")

llist1.print_list()
print(llist1.is_palindrome_meth1())
print(llist1.is_palindrome_meth2())
print(llist1.is_palindrome_meth3())
print("\n")

llist2 = SinglyLinkedList()
llist2.append("H")
llist2.append("E")
llist2.append("L")
llist2.append("L")
llist2.append("O")

llist2.print_list()
print(llist2.is_palindrome_meth1())
print(llist2.is_palindrome_meth2())
print(llist2.is_palindrome_meth3())
print("\n")