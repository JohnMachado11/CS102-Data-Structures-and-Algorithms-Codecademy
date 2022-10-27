
class TreeNode:
    def __init__(self, value):
        self.value = value
        print("initializing node...")
        self.children = []

    def add_child(self, child_node):
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        print("Removing " + child_node.value + " from " + self.value)
        # new removal method
        self.children = [child for child in self.children if child is not child_node]

        # "is" will return True if two variables point to the same object (in memory), 
        # == if the objects referred to by the variables are equal.

        #old removal method
        # new_children = []
        # for child in self.children:
        #     if child.value != child_node.value:
        #         new_children.append(child)
    
        # self.children = new_children

    def traverse(self):
        print("Traversing...")
        # new traverse method
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children
        
        # old traverse method
        # for child in self.children:
        #     print(child.value)

root = TreeNode("John")
child = TreeNode("John Jr")
child2 = TreeNode("Will Jr")
child3 = TreeNode("Will Jr Jr")

root.add_child(child)
root.add_child(child2)
child2.add_child(child3)

print()
root.traverse()