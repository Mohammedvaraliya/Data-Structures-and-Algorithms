class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def kthSmallest(self, root: 'TreeNode', k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right

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
    solution = BinarySearchTree()

    nums_1 = [3,1,4,None,2]
    k1 = 1
    root1 = buildBST(nums_1)
    result1 = solution.kthSmallest(root1, k1)
    print(result1)

    nums_2 = [5,3,6,2,4,None,None,1]
    k2 = 3
    root2 = buildBST(nums_2)
    result2 = solution.kthSmallest(root2, 3)
    print(result2)


        