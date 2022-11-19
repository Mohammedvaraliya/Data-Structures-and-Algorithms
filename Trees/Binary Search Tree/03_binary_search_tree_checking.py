class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
                
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        
        else:
            print("Value already present in the tree.")

    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)
            
    def _inorder_print_tree(self, cur_node):
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print(str(cur_node.data))
            self._inorder_print_tree(cur_node.right)

    def is_bst_satisfied(self):
        if self.root:
            is_satisfied = self._is_bst_satisfied(self.root, self.root.data)

            if is_satisfied is True:
                return True
            return False
        return True

    def _is_bst_satisfied(self, cur_node, data):
        if cur_node.left:
            if data > cur_node.left.data:
                return self._is_bst_satisfied(cur_node.left, cur_node.left.data)
            else:
                return False

        if cur_node.right:
            if data < cur_node.right.data:
                return self._is_bst_satisfied(cur_node.right, cur_node.right.data)
            else:
                return False
                
        return True







'''
    In-Order Traversal
    
                    8
                /       \
               3          10
             /   \       /  \  
            1      6    9     11

    1
    3
    6
    8
    9
    10
    11

'''            


if __name__ == "__main__":

    bst = BinarySearchTree()
    bst.insert(8)
    bst.insert(3)
    bst.insert(10)
    bst.insert(1)
    bst.insert(6)
    bst.insert(9)
    bst.insert(11)

    bst.inorder_print_tree()
    print(bst.is_bst_satisfied())
    print("\n")

    tree = BinarySearchTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)

    tree.inorder_print_tree()
    print(tree.is_bst_satisfied())

    


            
        

