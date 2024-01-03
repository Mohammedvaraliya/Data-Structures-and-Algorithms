class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def isValidBST(self, root: 'TreeNode') -> bool:

        def valid(node, left, right):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("+inf"))

# Helper function to build a BT from a list
def buildBT(nums):
    if not nums:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in nums]
    for i in range(len(nums)):
        if nodes[i]:
            if 2 * i + 1 < len(nums):
                nodes[i].left = nodes[2 * i + 1]
            if 2 * i + 2 < len(nums):
                nodes[i].right = nodes[2 * i + 2]

    return nodes[0]

if __name__ == "__main__":
    # Example 1
    input1 = [2, 1, 3]
    tree1 = buildBT(input1)
    bst1 = BinarySearchTree()
    bst1.root = tree1
    print(bst1.isValidBST(bst1.root))  # Output: True

    # Example 2
    input2 = [5, 1, 4, None, None, 3, 6]
    tree2 = buildBT(input2)
    bst2 = BinarySearchTree()
    bst2.root = tree2
    print(bst2.isValidBST(bst2.root))  # Output: False
