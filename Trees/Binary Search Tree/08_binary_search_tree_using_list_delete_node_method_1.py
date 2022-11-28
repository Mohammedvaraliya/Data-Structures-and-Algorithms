class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        element = []

        # visit left sub tree
        if self.left:
            element += self.left.in_order_traversal()

        # visit root BinarySearchTreeNode
        if self.data:
            element.append(self.data)

        # visit right sub tree
        if self.right:
            element += self.right.in_order_traversal()

        return element

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self. left = self.left.delete(val)

        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
            
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root



if __name__ == "__main__":

    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    bst = build_tree(elements)
    print(bst.in_order_traversal())
    print("\n")

    bst.delete(20)
    print("After deleting 20 : ",bst.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]
    print("\n")

    bst.delete(1)
    print("After deleting 1 : ",bst.in_order_traversal()) # this should print [4, 9, 17, 18, 23, 34]
    print("\n")

    


