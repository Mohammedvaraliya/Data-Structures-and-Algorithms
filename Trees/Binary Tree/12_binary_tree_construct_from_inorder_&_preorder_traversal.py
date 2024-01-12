class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ConstructBinaryTree:

    def buildTree(self, preorder: list[int], inorder: list[int]) -> 'TreeNode':
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
    

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

    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    root1 = builder.buildTree(preorder1, inorder1)
    result1 = print_tree(root1)
    print(result1)

    preorder2 = [-1]
    inorder2 = [-1]
    root2 = builder.buildTree(preorder2, inorder2)
    result2 = print_tree(root2)
    print(result2)
