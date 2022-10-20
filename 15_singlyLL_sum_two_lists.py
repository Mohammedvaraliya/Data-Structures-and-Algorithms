'''
Singly Linked Lists -- Sum Two Lists

llist 1 : 3 6 5 and

llist 2 : 2 4 8

365 + 248 = 613
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

    def sum_two_lists(self, llist):
        
        p = self.head
        q = llist.head

        sum_llist = SinglyLinkedList()

        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            # print("S :" + str(s))
            if s>= 10:
                carry = 1
                remainder = s % 10
                sum_llist.prepend(remainder)
            else:
                carry = 0
                sum_llist.prepend(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_llist.print_list()


    
llist1 = SinglyLinkedList()
llist1.append(5)
llist1.append(6)
llist1.append(3)

llist1.print_list()
print("\n")

llist2 = SinglyLinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)

llist2.print_list()
print("\n")

print(365 + 248)
llist1.sum_two_lists(llist2)
