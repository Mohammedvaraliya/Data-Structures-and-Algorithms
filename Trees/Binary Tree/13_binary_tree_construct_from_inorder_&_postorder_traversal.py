class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ConstructBinaryTree:

    # Time Complexity O(n^2)
    def buildTree1(self, inorder: list[int], postorder: list[int]) -> 'TreeNode':
        if not postorder or not inorder:
            return None
        
        root = TreeNode(postorder.pop())
        idx = inorder.index(root.val)
        root.right = self.buildTree1(inorder[idx + 1:], postorder)
        root.left = self.buildTree1(inorder[:idx], postorder)
        return root

    # Time Complexity O(n)
    def buildTree2(self, inorder: list[int], postorder: list[int]) -> 'TreeNode':

        def buildTreeHelper(left, right):
            if left > right:
                return None

            rootVal = postorder.pop()
            rootNode = TreeNode(rootVal)

            idx = inorderIndexMap[rootVal]
            rootNode.right = buildTreeHelper(idx + 1, right)
            rootNode.left = buildTreeHelper(left, idx - 1)
            return rootNode

        inorderIndexMap = {}
        for (i, val) in enumerate(inorder):
            inorderIndexMap[val] = i

        return buildTreeHelper(0, len(postorder) - 1)
    

def print_tree(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


if __name__ == "__main__":
    
    builder = ConstructBinaryTree()

    postorder1 = [9,15,7,20,3]
    inorder1 = [9,3,15,20,7]
    root1 = builder.buildTree2(inorder1, postorder1)
    result1 = print_tree(root1)
    print(result1)

    postorder2 = [-1]
    inorder2 = [-1]
    root2 = builder.buildTree1(inorder2, postorder2)
    result2 = print_tree(root2)
    print(result2)
