class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:

    def maxPathSum(self, root: 'TreeNode') -> int:
        res = [root.val]

        # Return max path sum without split
        def dfs(root):
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Compute max path sum with split
            res[0] = max(res[0], root.val + leftMax + rightMax)

            return root.val + max(leftMax, rightMax)
        
        dfs(root)

        return res[0]
        


# Helper function to build a BT from a list
def buildBT(nums):
    if not nums:
        return None

    root = TreeNode(nums[0])
    nodes = [root]
    i = 1

    while i < len(nums):
        current_node = nodes.pop(0)

        if nums[i] is not None:
            current_node.left = TreeNode(nums[i])
            nodes.append(current_node.left)

        i += 1

        if i < len(nums) and nums[i] is not None:
            current_node.right = TreeNode(nums[i])
            nodes.append(current_node.right)

        i += 1

    return root


if __name__ == "__main__":
    
    binary_tree = BinaryTree()

    nums1 = [1, 2, 3]
    # Building BinaryTree
    root1 = buildBT(nums1)
    result1 = binary_tree.maxPathSum(root1)
    print(result1)

    nums2 = [-10, 9, 20, None, None, 15, 7]
    # Building BinaryTree
    root2 = buildBT(nums2)
    result2 = binary_tree.maxPathSum(root2)
    print(result2)
