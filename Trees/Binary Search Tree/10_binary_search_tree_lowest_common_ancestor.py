class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinarySearchTreeNode:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

# Helper function to build a BST from a list
def buildBST(nums):
    if not nums:
        return None

    root = TreeNode(nums[0])
    for num in nums[1:]:
        if num is not None:
            root = insert(root, num)

    return root

# Helper function to insert a value into a BST
def insert(root, val):
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    
    return root





if __name__ == "__main__":
    solution = BinarySearchTreeNode()

    nums_1 = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p_val_1, q_val_1 = 2, 8
    root1 = buildBST(nums_1)
    p1 = TreeNode(p_val_1)
    q1 = TreeNode(q_val_1)
    result1 = solution.lowestCommonAncestor(root1, p1, q1)
    print(result1.val)

    nums_2 = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    p_val_2, q_val_2 = 2, 4
    root2 = buildBST(nums_2)
    p2 = TreeNode(p_val_2)
    q2 = TreeNode(q_val_2)
    result2 = solution.lowestCommonAncestor(root2, p2, q2)
    print(result2.val)

    nums_3 = [2, 1]
    p_val_3, q_val_3 = 2, 1
    root3 = buildBST(nums_3)
    p3 = TreeNode(p_val_3)
    q3 = TreeNode(q_val_3)
    result3 = solution.lowestCommonAncestor(root3, p3, q3)
    print(result3.val)