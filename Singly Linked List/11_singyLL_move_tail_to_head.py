'''
Singly Linked Lists -- Move Tail to Head

Example - singly LL is : A B C D E F

Ater move tail to head : F A B C D E
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

    def move_tail_to_head(self):

        last = self.head
        second_to_last = None
        
        while last.next:
            second_to_last = last
            last = last.next
            
        last.next = self.head
        second_to_last.next = None
        self.head = last


    
llist = SinglyLinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.append("F")

llist.print_list()
print("\n")

llist.move_tail_to_head()
llist.print_list()
