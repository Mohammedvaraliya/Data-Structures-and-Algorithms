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

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum


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

    print("searching...",bst.search(17))
    print("\n")

    print("Min:",bst.find_min())
    print("\n")

    print("Max:",bst.find_max())
    print("\n")

    print("Sum:", bst.calculate_sum())


