from node import Node

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0
        
    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print("Adding " + str(item_to_add.get_value()) + " to the queue! \n")
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")
        
    def dequeue(self):
        if self.is_empty() != True:
            item_to_remove = self.head
            print("Removing " + str(item_to_remove.get_value()) + " from the queue!" )

            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = item_to_remove.get_next_node()

            self.size -= 1
            return item_to_remove.get_value()
        print("This queue is totally empty!")

    def peek(self):
        if self.is_empty():
            print("Nothing to see here!")
        else:
            return self.head.get_value()

    def view_queue(self):
        
        head_of_queue = self.head
        contents_list = []
        contents = ""
        if self.is_empty():
            print("No one in the queue!")
            return
        else:
            while head_of_queue:
                contents_list.append(head_of_queue.get_value())
                head_of_queue = head_of_queue.get_next_node()
            
            contents_list.reverse()
            list_length = len(contents_list)
            last_idx = list_length - 1

            for idx in range(list_length):
                if idx == last_idx:
                    contents += "{} at front of queue.".format(contents_list[idx])
                else:
                    contents += "{} -> ".format(contents_list[idx])
            return contents

    def get_size(self):
        return self.size
    
    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()
        
    def is_empty(self):
        return self.size == 0

q = Queue()
q.enqueue("John")
q.enqueue("Jean")
q.enqueue("Matt")
print(q.view_queue())

# print(q.get_size())
# print(q.get_size())
# print(q.get_size())

# q.dequeue()
# q.dequeue()
# q.dequeue()
# print(q.get_size())

# print(q.peek())



