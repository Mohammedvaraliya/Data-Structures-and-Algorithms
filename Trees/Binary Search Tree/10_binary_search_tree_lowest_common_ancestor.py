class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Problem Logic
    def lowestCommonAncestor(self, root, p , q):
        cur = root
        
        while cur:
            if p.data > cur.data and q.data > cur.data:
                cur = cur.right
            elif p.data < cur.data and q.data < cur.data:
                cur = cur.left
            else:
                return cur.data




if __name__ == "__main__":

    BST1 = BinarySearchTreeNode(6)
    BST1.left = BinarySearchTreeNode(2)
    BST1.right = BinarySearchTreeNode(8)
    BST1.left.left = BinarySearchTreeNode(0)
    BST1.left.right = BinarySearchTreeNode(4)
    BST1.left.right.left = BinarySearchTreeNode(3)
    BST1.left.right.right = BinarySearchTreeNode(5)
    BST1.right.left = BinarySearchTreeNode(7)
    BST1.right.right = BinarySearchTreeNode(9)

    p1 = BST1.left
    q1 = BST1.right
    print(BST1.lowestCommonAncestor(BST1, p1, q1))
    
    p2 = BST1.left
    q2 = BST1.left.right
    print(BST1.lowestCommonAncestor(BST1, p2, q2))

    BST2 = BinarySearchTreeNode(2)
    BST2.left = BinarySearchTreeNode(1)
    
    p3 = BST2
    q3 = BST2.left
    print(BST2.lowestCommonAncestor(BST2, p3, q3))


    