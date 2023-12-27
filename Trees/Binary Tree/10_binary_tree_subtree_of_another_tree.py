# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class SubTree:

    def isSubtree(self, s, t) -> bool:
        if not t:
            return True
        
        if not s:
            return False
        
        if self.sameTree(s, t):
            return True
        
        return (self.isSubtree(s.left, t) or self.isSubtree(s.right, t))



    def sameTree(self, s, t):
        if not s and not t:
            return True
        
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))
        
        return False



if __name__ == "__main__":

    tree1 = TreeNode(3)
    tree1.left = TreeNode(4)
    tree1.right = TreeNode(5)
    tree1.left.left = TreeNode(1)
    tree1.left.right = TreeNode(2)

    tree2 = TreeNode(4)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(2)

    initialize_result = SubTree()
    
    result = initialize_result.isSubtree(tree1, tree2)
    
    print(result)