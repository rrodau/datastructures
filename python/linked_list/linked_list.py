class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, new_node):
        self.next_node = new_node


class LinkedList:

    def __init__(self, value=None):
        self.head = Node(value)
    
    def get_head(self):
        return self.head
    
    def insert_beginning(self, new_value):
        """
        A function that appends a new node at the beginning

        @param:
            new_value -> the value that needs to be inserted
        
        @return:
            None
        """
        new_node = Node(new_value)  # create a new node with the value
        new_node.set_next_node(self.head)   # set the new nodes next node to the head node
        self.head = new_node       # update the head node to be the new node

    def append(self, new_value):
        """
        A function that appends a new node at the end
        
        @param:
            new_value -> the value that needs to be appended
        
        @return:
            None
        """
        if type(new_value) == type([]): # if list of values is given
            for value in new_value: # call append for each value in list
                self.append(value)
            return
        new_node = Node(new_value)  # create the new node
        current_node = self.head
        while current_node.get_next_node(): # while end not reached
            current_node = current_node.get_next_node() # update current_node to be the next node
        current_node.set_next_node(new_node)    # update last nodes next node to be the new_node

    def __str__(self):
        """
        A function that returns the string represantation of the linkedlist
        """
        string_list = "["
        current_node = self.head    # set the current node to be the head node
        while current_node: # continue until the end is reached
            if current_node.get_value() != None: # skip nodes with value None
                string_list += str(current_node.get_value()) + ", " 
            current_node = current_node.get_next_node() # update the current node to be the next node
        string_list = string_list[:-2] + "]" if string_list[-2:] == ", " else string_list + "]"     # the end will have probably an unecessary ", " that needs to be removed
        return string_list

    def remove_node(self, value_to_remove):
        """
        A function that will remove a node which holds a specific value

        @param:
            value_to_remove -> the value that needs to be removed

        @return:
            None
        """
        current_node = self.head    # set the current node to be the head node
        if current_node.get_value == value_to_remove:   # if the value is in the head node
            self.head = current_node.get_next_node()    # set the head node to be the next node of the current head node
        else:
            while current_node: # continue until found or the end is reached
                next_node = current_node.get_next_node() # update the next node to be the next node of the current node
                if next_node is None:   # end reached and value not found
                    print("Element not in List")
                    break
                if next_node.get_value() == value_to_remove:    # found the value in next node
                    current_node.set_next_node(next_node.get_next_node())   # set the currents node next node to be the node after the next node
                    current_node = None # break the while loop
                else:
                    current_node = next_node    # if the value is not in the next node update current node to be the next node
    
    def swap_nodes(self, value1, value2):
        """
        A function that swaps two nodes in the linkedlist

        @param:
            value1 -> the first value that needs to be swapped
            value2 -> the second value that needs to be swapped

        @return:
            None
        """
        node1 = self.head   # set the first node to be the head node (for searching)
        node2 = self.head   # set the second node to be the head node (for searching)
        node1_prev = None   # set the prevsnodes to be None (will be needed for updating)
        node2_prev = None

        if value1 == value2: 
            print("The elements are the same. No swapping is needed")
        while node1:    # as long the end is not reached
            if node1.get_value() == value1: # node found
                break
            else:
                node1_prev = node1  # update node1_prev to be node1
                node1 = node1.get_next_node()   # update node1 to be the next node
        # same for node2
        while node2:
            if node2.get_value() == value2:
                break
            else:
                node2_prev = node2
                node2 = node2.get_next_node()
        
        # One or both values not found
        if node1 is None:
            print(f"{value1} is not in List")
            return
        elif node2 is None:
            print(f"{value2} is not in List")
            return
        
        # node1 is head node. Update node2 to be head node
        if node1_prev is None:
            self.head = node2
        else:
            node1_prev.set_next_node(node2) # node1 is not head. Update node1 previous node to point to node2
        
        # node2 is head node. Update node1 to be head node
        if node2_prev is None:
            self.head = node1
        else:
            node2_prev.set_next_node(node1) # node2 is not head. Update node1 previous node to point to node1

        # change the next_nodes of node1 and node2
        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)


ll = LinkedList()
for i in range(10):
  ll.append(i)
ll.append([i for i in range(10, 20)])
ll.append(100)
print(ll)
ll.swap_nodes(0, 100)
print(ll)