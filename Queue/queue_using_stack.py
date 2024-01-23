class Node():
    data = None
    next = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node: " + str(self.data) + ">"

class Stack() :
    def __init__(self):
        self.top = None

    def push(self, value):
        if isinstance(value, Node):
            value.next = self.top
            self.top = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if not self.top:
            return
        deleted_node = self.top
        self.top = self.top.next
        deleted_node.next = None
        return deleted_node
    
    def get_top(self):
        return self.top
    
    def print_reverse(self):
        if self.top is None:
            return
        else:
            current_node = self.pop()
            self.print_reverse()
            print(current_node)
            self.push(current_node)

    def __reverse_recursive(self, element):
        """
        before inserting empty the stack
        then insert at the very bottom
        """
        if not self.top:
            self.push(element)
            return

        element2 = self.pop()
        self.__reverse_recursive(element)
        self.push(element2)

    def reverse(self):
        if self.top:
            element = self.pop()
            self.reverse()
            self.__reverse_recursive(element)

    def __sort_recursive(self, element):
        if self.top is None or self.top.data > element.data:
            self.push(element)
            return
        
        element2 = self.pop()
        self.__sort_recursive(element)
        self.push(element2)

    def sort(self):
        if self.top:
            element = self.pop()
            self.sort()
            self.__sort_recursive(element)
    
    def __repr__(self):
        if self.top is None:
            return "--- empty ---"
        current = self.top
        nodes = []

        while current:
            if current == self.top:
                nodes.append("Top: [%s]" % current.data)
            else: 
                nodes.append("[%s] " % current.data)
            current = current.next
        return "-> ".join(nodes)

class Queue(Stack):

    def __init__(self):
        super().__init__()

    def enqueue(self, element):
        super().push(element)

    def dequeue(self):
        super().reverse()
        deleted = super().pop()
        super().reverse()
        return deleted
    
    def __repr__(self):
        super().reverse()
        result = super().__repr__()
        super().reverse()
        return result