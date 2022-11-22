

class BinarySearchTree:

    def __init__(self, value, depth=1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                self.right.insert(value)

    def get_node_by_value(self, value):

        if self.value == value:
            return self
        elif self.left != None and value < self.value:
            return self.left.get_node_by_value(value)
        elif self.right != None and value > self.value:
            return self.right.get_node_by_value(value)
        else: 
            return None

    def depth_first_traversal(self):
        # "In Order" Traversal
        if self.left is not None:
            self.left.depth_first_traversal()
    
        print(f'Depth={self.depth}, Value={self.value}')
        
        if self.right is not None:
            self.right.depth_first_traversal()


root = BinarySearchTree(100)

"""
     100
    /   \
  50    125
 /  \   
25  75
"""

root.insert(50)
root.insert(125)
root.insert(75)
root.insert(25)

print(root.get_node_by_value(75).value)

root.depth_first_traversal()

# With depth-first traversal, we always traverse down each left-side branch of a tree
# fully before proceeding down the right branch. However, there are three traversal options:

#1
# Preorder is when we perform an action on the current node first,
# followed by its left child node and its right child node

#2
# Inorder is when we perform an action on the left child node first,
# followed by the current node and the right child node

#3
# Postorder is when we perform an action on the left child node first,
#  followed by the right child node and then the current node