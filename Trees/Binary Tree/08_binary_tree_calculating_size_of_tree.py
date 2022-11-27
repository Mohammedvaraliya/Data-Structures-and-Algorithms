class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def size(self):
        return len(self.items)
    
    def __len__(self):
        return self.size()

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        
    def height(self, node):
        if node is None:
            return -1
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def size(self):
        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1

        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)

        return size
    
    def size_(self, node):
        if node is None:
            return 0
        
        return 1 + self.size_(node.left) + self.size_(node.right)



        


    
'''
    Calculating Size of Tree
    
                      
                      1       
                    /   \    
                   2      3
                  /  \           
                 4     5     

    5
    
'''

        

if __name__ == "__main__":

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    X = tree.size()
    print(X)

    Y = tree.size_(tree.root)
    print(Y)