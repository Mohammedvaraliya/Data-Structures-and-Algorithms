class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        
        if traversal_type == "levelorder":
            return self.levelorder_print(self.root)

        elif traversal_type == "reverse levelorder":
            return self.reverse_levelorder_print(self.root)
        
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

        


    
'''
    Reverse Level-Order Traversal
    
                    1
                  /   \
                 2      3
                /  \          
               4    5     

    1-2-3-4-5-
'''

        

if __name__ == "__main__":

    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    X = tree.print_tree("reverse levelorder")
    print(X)