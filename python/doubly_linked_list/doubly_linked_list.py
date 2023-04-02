import sys
sys.path.insert(0, './nodes/')
from nodes import Node


class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
    
    def add_to_head(self, new_value):
        """
        A function that adds a new node to the head of the LinkedList

        @params:
            new_value -> the value the new nodes will hold
        
        @returns:
            None
        """ 
        print(f"Adding Node with value {new_value} to the head.")
        new_head = Node(new_value)  
        current_head = self.head_node   # get the head in a temporary variable as it will be overwritten   

        # if there was a node as the head update the pointers
        if current_head is not None:    
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)

        self.head_node = new_head

        # if there was no tail, the new node will also be the tail
        if self.tail_node is None:
            self.tail_node = new_head

    def add_to_tail(self, new_value):
        """
        A function that adds a new node to the tail of the LinkedList

        @params:
            new_value -> the value the new node will hold
        
        @returns:
            None
        """
        print(f"Adding Node with value {new_value} to the tail")
        new_tail = Node(new_value)
        current_tail = self.tail_node

        # if there was a tail, update the pointers
        if current_tail is not None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)

        self.tail_node = new_tail

        # if ther was no head, the new node will also be the head
        if self.head_node is None:
            self.head_node = new_tail


    def remove_head(self):
        """
        A function that removes the head of the LinkedList

        @returns:
            The value the head node holded
        """
        removed_head = self.head_node
        # if there was no head node return None
        if removed_head is None:
            print("Nothing to remove.")
            return None
        # set the new head node to be the successor of the old headnode
        self.head_node = removed_head.get_next_node()
        # set the precedor of the new head to None if it is a valid Node
        if self.head_node is not None:
            self.head_node.set_prev_node(None)
        # if the head was also the tailnode call remove_tail function
        if removed_head == self.tail_node:
            self.remove_tail()

        return removed_head.get_value()
    

    def remove_tail(self):
        """
        A function that removes the tail of the LinkedList

        @returns:
            The value the tail node holded
        """
        removed_tail = self.tail_node

        # if there was no tail node return None
        if removed_tail is None:
            return None
        # set the new tail node to be the precedor of the old tailnode
        self.tail_node = removed_tail.get_prev_node()
        # set the successor of the new tail to None if it is valid Node
        if self.tail_node is not None:
            self.tail_node.set_next_node(None)
        # if the tail was also the headnode call remove_head function
        if removed_tail == self.head_node:
            self.remove_head()

        return removed_tail.get_value()

    def remove(self, value_to_remove):
        """
        A function that removes a node which holds a specific value

        @params:
            value_to_remove -> the value which needs to be removed
        
        @return:
            None if there is no Node with this value
            else return the value
        """
        node_to_remove = None
        current_node = self.head_node
        # search the whole list until the node is found or the end is reached
        while current_node is not None:
            # update node_to_remove if the node was found and break out the loop
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break
            # go to the next node
            current_node = current_node.get_next_node()
        # return None if no Node was found
        if node_to_remove is None:
            return None
        # if the node is the head call remove head
        elif node_to_remove == self.head_node:
            return self.remove_head()
        # if the node is the tail call remove tail
        elif node_to_remove == self.tail_node:
            return self.remove_tail()
        # otherwise get the precedor and successor node an update their pointers
        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()
            next_node.set_prev_node(prev_node)
            prev_node.set_next_node(next_node)

        return node_to_remove.get_value()


    def __str__(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value())
            current_node = current_node.get_next_node()
            if current_node is not None:
                string_list += " <-> "
        return string_list

