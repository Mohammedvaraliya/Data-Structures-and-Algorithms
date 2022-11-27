class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            # add data in left subtree
            if self.left:
                pass
            else:
                self.left = Node(data)


        else:
            # add data in right subtree
            pass