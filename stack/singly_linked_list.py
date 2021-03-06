class Node:

    def __init__(self, value=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list. default to None
        self.next_node = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:

    def __init__(self):
        # reference to the head of the list
        self.head = None
        # reference to the tail of the list
        self.tail = None

    def add_to_tail(self, value):
        # wrap the input value in a node
        new_node = Node(value)

        # check if there is no head (i.e., the list is empty)
        if not self.head:
            # set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
    
        # we have a non-empty list, nonsingular list. Add the new node to the tail
        else:
        # set the current tail's next reference to our new node
            self.tail.set_next(new_node)
        # set the list's tail reference to the new node
            self.tail = new_node

    def remove_head(self):

        # return None if there is no head (i.e. the list is empty)
        if not self.head:
            return None

        # if head has no next, then we have a single element in our list
        if not self.head.get_next():
            # get a reference to the head
            head = self.head
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None

            # return the value
            return head.get_value()

        # otherwise we have more than one element in our list
        value = self.head.get_value()

        # set the head reference to the current head's next node in the list
        self.head = self.head.get_next()

        return value

    def contains(self, value):
        if not self.head:
            return False

        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head

        # check to see if we're at a valid node 
        while current:

            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True

            # update our current node to the current node's next node
            current = current.get_next()

        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):   
        # check for empty list     
        if not self.head:
            return None
        
        # set initial values
        max_val = 0
        current = self.head

        # iterrate through list
        while current:
            current_val = current.get_value()

            # compare values and update max when greater value presented
            if max_val < current_val:
                max_val = current_val

            current = current.get_next()

        return max_val

    def remove_tail(self):
        # check for empty list
        if not self.tail:
            return None
        
        # set intial values
        current = self.head

        # extract tail value
        value = self.tail.get_value()

        # iterrate through list
        while current:
            # check to see if we are on second to last node
            if current.get_next() == self.tail:

                # remove current tail and reassign to second to last node
                current.set_next = None
                self.tail = current
                break
            current = current.get_next()
        return value


        


