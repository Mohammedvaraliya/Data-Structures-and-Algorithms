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
    
    def count_occurences_iterative(self, data):

        count = 0
        cur_node = self.head
        while cur_node:
            if cur_node.data == data:
                count +=1
            cur_node = cur_node.next
        return count
        
    def count_occurences_recursive(self, node, data):

        if not node:
            return 0
        
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)


    
llist = SinglyLinkedList()
llist.append(1)
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(1)
llist.append(4)
llist.append(1)
llist.append(2)

llist.print_list()
print("\n")

print(llist.count_occurences_iterative(1))
print("\n")

print(llist.count_occurences_recursive(llist.head, 1))