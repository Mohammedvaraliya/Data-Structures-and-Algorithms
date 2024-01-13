class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ConstructBinaryTree:

    def buildTree(self, postorder: list[int], inorder: list[int]) -> 'TreeNode':
        if not postorder or not inorder:
            return None
        
        root = TreeNode(postorder[0])
        mid = inorder.index(postorder[0])
        root.left = self.buildTree(postorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(postorder[mid + 1:], inorder[mid + 1:])
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

    postorder1 = [9,15,7,20,3]
    inorder1 = [9,3,15,20,7]
    root1 = builder.buildTree(postorder1, inorder1)
    result1 = print_tree(root1)
    print(result1)

    postorder2 = [-1]
    inorder2 = [-1]
    root2 = builder.buildTree(postorder2, inorder2)
    result2 = print_tree(root2)
    print(result2)
