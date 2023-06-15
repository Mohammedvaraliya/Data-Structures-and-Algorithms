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

    def hasCycle(self):
        pass



if __name__ == "__main__":

    llist = SinglyLinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    llist.append(5)

    llist.print_list()
    print("\n")

    

    