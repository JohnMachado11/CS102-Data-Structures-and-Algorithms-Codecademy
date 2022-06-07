class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node
        
    def set_link_node(self, link_node):
        self.link_node = link_node
        
    def get_link_node(self):
        return self.link_node
    
    def get_value(self):
        return self.value


john = Node("likes sports")
matt = Node("likes coding")
jean = Node("likes music")

jean.set_link_node(matt) # jean -> matt
john.set_link_node(jean) # john -> jean

matts_data = jean.get_link_node().get_value()
jeans_data = john.get_link_node().get_value()

print(matts_data)
print(jeans_data)