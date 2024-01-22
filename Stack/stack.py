"""
Stack using linked list
"""

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
    
# stk = Stack()
# stk.push(10)
# stk.push(12)
# stk.push(7)
# stk.push(14)
# stk.push(6)
# stk.push(4)
# print(stk.get_top())
# print(stk)
# stk.reverse()
# print(stk.get_top())
# print(stk)
# stk.reverse()
# print(stk)
# stk.print_reverse()
# stk.pop()
# stk.pop()
# print(stk)
# stk.pop()
# print(stk)
# stk.sort()
# print(stk.get_top())
# print(stk)