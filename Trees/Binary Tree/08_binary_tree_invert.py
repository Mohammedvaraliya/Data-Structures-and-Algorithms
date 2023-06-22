class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "inverted_levelorder_tree":
            self.invertTree(self.root)
            return self.levelorder_print(self.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False
        
    def levelorder_print(self, start):
        if start is None:
            return 

        queue = Queue()
        queue.enqueue(start)

        traversal = []
        while len(queue) > 0:
            traversal.append(queue.peek())
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal
    
    def invertTree(self, root):
        if not root:
            return None
        
        # Swap the children 
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)

    

if __name__ == "__main__":
    tree = BinaryTree(4)
    tree.root.left = Node(2)
    tree.root.right = Node(7)
    tree.root.left.left = Node(1)
    tree.root.left.right = Node(3)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(9)

    inverted_tree = tree.print_tree("inverted_levelorder_tree")
    print(inverted_tree)
