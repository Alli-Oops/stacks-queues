# from stacks_queues.linked_list import LinkedList

class StackEmptyException(Exception):
    pass

class Stack:
    def __init__(self):
        # self.store = LinkedList()
        self.st = []

    def push(self, element):
        """ Adds an element to the top of the Stack.
            Returns None
        """
        # self.store.add_first(item)
        self.st.append(element)
        

    def pop(self):
        """ Removes an element from the top
            Of the Stack
            Raises a StackEmptyException if
            The Stack is empty.
            returns None
        """
        # return self.store.remove_first()
        if (len(self.st)>0):
            result = self.st.pop()
            return result

    def empty(self):
        """ Returns True if the Stack is empty
            And False otherwise
        """
        # return self.store.length() == 0
        return len(self.st) == 0

    def __str__(self):
        """ Returns the Stack in String form like:
            [3, 4, 7]
            Starting with the top of the Stack and
            ending with the bottom of the Stack.
        """
        # return str(self.store)
        return str(self.st)
