class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:

    def serialize(self, root: 'TreeNode'):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def preorder_dfs(node):
            if not node:
                res.append("Null")
                return
            res.append(str(node.val))
            preorder_dfs(node.left)
            preorder_dfs(node.right)

        preorder_dfs(root)

        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.i = 0

        def preorder_dfs():
            if vals[self.i] == "Null":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = preorder_dfs()
            node.right = preorder_dfs()
            
            return node
        
        return preorder_dfs()
        


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
    
    serializer = BinaryTree()

    deserializer = BinaryTree()
