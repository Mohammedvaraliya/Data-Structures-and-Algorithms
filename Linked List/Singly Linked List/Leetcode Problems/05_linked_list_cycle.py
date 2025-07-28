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
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")
    
    def make_cycle(self, pos):
        if pos < 0:
            return

        cycle_node = self.head
        for _ in range(pos):
            if cycle_node is None:
                return
            cycle_node = cycle_node.next

        if cycle_node is None:
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = cycle_node

    def hasCycle(self):
        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def hasCycle_method2(self):
        visited = set()

        current = self.head
        while current.next:
            if current in visited:
                return True
            visited.add(current)
            current = current.next

        return False



if __name__ == "__main__":

    llist = SinglyLinkedList()
    llist.append(3)
    llist.append(2)
    llist.append(0)
    llist.append(-4)

    llist.print_list()

    llist.make_cycle(1)  # Create a cycle at position 1

    print(llist.hasCycle())
    

    