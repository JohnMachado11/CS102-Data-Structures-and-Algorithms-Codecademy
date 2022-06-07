from node import Node


class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
            print("Adding {} to the stack!".format(value))
        else:
            print("No room for {}!".format(value))

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            print("Removing {} from the stack.".format(item_to_remove.get_value()))
            
            return item_to_remove.get_value()
        else:
            print("The stack is totally empty.")

    def peek(self):
        
        if not self.is_empty():
            return self.top_item.get_value()
        
        print("Nothing to see here!")

    def has_space(self):    
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0



books = Stack(4)

books.push("Lord of the Rings")
books.push("Star Wars")
books.pop()
books.pop()
books.pop()
