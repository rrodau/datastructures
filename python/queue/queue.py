import sys
sys.path.insert(0, './nodes/')
from nodes import Node

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = max_size


    def enqueue(self, value):
        """
        A function that places a value back to the queue

        @params:
            value -> the value of the node which will be appended
        
        @returns:
            None
        """
        # Check if the queue has space to hold an additional node
        if self.has_space():
            item_to_add = Node(value)
            print(f"Adding {value} to the queue!")
            # if the queue was empty than the new node is both head and tail
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            # else add it to the tail node and mark it as the new tail
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Queue is at maximum capacity.")


    def dequeue(self):
        """
        A function that removes the next node from the queue 
        which is the one at head position

        @returns:
            the value that the removed node holds: Any
        """
        # check if there is atleast one node in a queue
        if not self.is_empty():
            item_to_remove = self.head
            print(f"Removing {self.head.get_value()} from the queue!")
            # if there was only one node than both head and tail will be none
            if self.size == 1:
                self.head = None
                self.tail = None
            # else the new head node will be the successor of the head node
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("Queue holds no values.")
        

    def peek(self):
        """
        A function that returns the value of the next node in the queue

        @returns:
            the value that the head node holds: Any
        """
        if not self.is_empty():
            return self.head.get_value()
        print("Nothin to see here!")


    def get_size(self):
        """
        A helper function that returns the number of 
        nodes in the queue

        @returns:
            size of queue: Integer
        """
        return self.size
  

    def has_space(self):
        """
        A helper function that returns if there is 
        space in the queue to add a node

        @returns:
            wether there is space or not: Boolean
        """
        if self.max_size is not None:
            return self.size < self.max_size
        return True