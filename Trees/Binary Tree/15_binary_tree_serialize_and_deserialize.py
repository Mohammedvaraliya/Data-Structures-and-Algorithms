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
        

# Helper function to build a BT from a list in preorder traversal
def buildBT(nums):
    def build(index):
        if index >= len(nums) or nums[index] is None:
            return None, index + 1
        node = TreeNode(nums[index])
        node.left, index = build(index + 1)
        node.right, index = build(index)
        return node, index

    root, _ = build(0)
    return root


if __name__ == "__main__":
    
    nums1 = [1, 2, None, None, 3, 4, None, None, 5, None, None]
    # Building BinaryTree
    root1 = buildBT(nums1)
    bt1 = BinaryTree()
    serializer1 = bt1.serialize(root1)
    print(f"Serialized: {serializer1}")
    deserializer1 = bt1.deserialize(serializer1)
    print(f"Deserialized: {bt1.serialize(deserializer1)}")
    
    nums2 = []
    # Building BinaryTree
    root2 = buildBT(nums2)
    bt2 = BinaryTree()
    serializer2 = bt2.serialize(root2)
    print(f"Serialized: {serializer2}")
    deserializer2 = bt2.deserialize(serializer2)
    print(f"Deserialized: {bt2.serialize(deserializer2)}")

