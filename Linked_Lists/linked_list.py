
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_node_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_node):
        self.next_node = new_node

class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, value):
        new_node = Node(value)
        if self.head_node == None:
            self.head_node = new_node
        else:
            new_node.set_next_node(self.head_node)
            self.head_node = new_node

    def insert_end(self, value):
        new_node = Node(value)
        if self.head_node == None:
            self.head_node = new_node
        else:
            current_node = self.get_head_node()
            while current_node.get_next_node() != None:
                current_node = current_node.get_next_node()
            current_node.set_next_node(new_node)
            print("New node added {}".format(current_node.get_next_node().get_node_value()))

    def display_list(self):
        current_node = self.get_head_node()
        contents = ""
        while current_node:
            contents += "{} -> ".format(current_node.get_node_value())
            current_node = current_node.get_next_node()
        contents += "None"
        return contents

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_node_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_node_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node

    def nth_last_node(self, n):
        current = None
        tail_seeker = self.get_head_node()
        count = 1
        while tail_seeker:
            tail_seeker = tail_seeker.get_next_node()
            count += 1
            if count >= n + 1:
                if current is None:
                    current = self.get_head_node()
                else:
                    current = current.get_next_node()
        return current.get_node_value()

    def list_copy(self):
        current_node = self.get_head_node()
        results = []
        while current_node:
            results.append(current_node.get_node_value())
            current_node = current_node.get_next_node()
        return results

    def find_middle(self):
        fast = self.get_head_node()
        slow = self.get_head_node()
        while fast:
            fast = fast.get_next_node()
            if fast:
                fast = fast.get_next_node()
                slow = slow.get_next_node()
        return slow.get_node_value()

    # half speed version
    def find_middle_alt(self): 
        count = 0 
        fast = self.get_head_node() 
        slow = self.get_head_node() 
        while fast: 
            fast = fast.get_next_node() 
            if count % 2 != 0: 
                slow = slow.get_next_node() 
            count += 1 
        return slow.get_node_value() 



ll = LinkedList()
ll.insert_beginning(50) 
ll.insert_end(25)
ll.insert_end(15)
ll.insert_end(10)
ll.remove_node(10)
print(ll.display_list())