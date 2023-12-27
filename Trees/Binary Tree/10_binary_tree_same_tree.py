from collections import deque

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_result(self, traversal_type, tree_2):
        if traversal_type == "is_same_tree_recursive":
            return self.isSameTree_DFS_recursive(self.root, tree_2.root)
        if traversal_type == "is_same_tree_iterative":
            return self.isSameTree_BFS_iterative(self.root, tree2.root)
        else:
            print("Depth type " + str(traversal_type) + " is not supported.")
            return False

    def isSameTree_DFS_recursive(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.value != q.value:
            return False
        
        return (self.isSameTree_DFS_recursive(p.left, q.left) and self.isSameTree_DFS_recursive(p.right, q.right))

    def isSameTree_BFS_iterative(self, p, q):
        queue = deque([(p, q)])

        while queue:
            node_p, node_q = queue.popleft()

            if not node_p and not node_q:
                continue

            if not node_p or not node_q or node_p.value != node_q.value:
                return False

            queue.append((node_p.left, node_q.left))
            queue.append((node_p.right, node_q.right))

        return True



        

if __name__ == "__main__":

    tree1 = BinaryTree(1)
    tree1.root.left = Node(2)
    tree1.root.right = Node(3)

    tree2 = BinaryTree(1)
    tree2.root.left = Node(2)
    tree2.root.right = Node(3)

    X = tree1.print_result("is_same_tree_recursive", tree2)
    print(X)

    Y = tree1.print_result("is_same_tree_iterative", tree2)
    print(X)


    