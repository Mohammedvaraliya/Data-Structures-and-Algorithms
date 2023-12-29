class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def levelOrder(self, root: 'TreeNode'):
        res = []

        q = Queue()
        q.enqueue(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.dequeue()
                if node:
                    level.append(node.val)
                    q.enqueue(node.left)
                    q.enqueue(node.right)
            if level:
                res.append(level)
        
        return res


# Helper function to build a BT from a list
def buildBT(nums):
    if not nums:
        return None

    root = TreeNode(nums[0])
    queue = Queue()
    queue.enqueue(root)

    i = 1
    while i < len(nums):
        current_node = queue.dequeue()

        if nums[i] is not None:
            current_node.left = TreeNode(nums[i])
            queue.enqueue(current_node.left)

        i += 1

        if i < len(nums) and nums[i] is not None:
            current_node.right = TreeNode(nums[i])
            queue.enqueue(current_node.right)

        i += 1

    return root



if __name__ == "__main__":

    nums = [3, 9, 20, None, None, 15, 7]

    # Building BinaryTree
    binary_tree = BinaryTree()
    root = buildBT(nums)

    # Performing level order traversal
    result = binary_tree.levelOrder(root)
    print(result)