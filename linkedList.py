class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data %s>" %self.data
    

class LinkedList:

    def __init__(self):
        self.head = None
    
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def __repr__(self):
        current = self.head
        nodes = []

        while current:
            if current == self.head:
                nodes.append("[Head]: %s" % current.data)
            elif current.next_node == None:
                nodes.append("[Tail]: %s" % current.data)
            else: 
                nodes.append("[%s] " % current.data)
            current = current.next_node
        return "-> ".join(nodes)