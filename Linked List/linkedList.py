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

    def search(self, key):
        current = self.head

        while(current):
            if current.data == key:
                return current
            current = current.next_node
        return None
    
    def insert(self, data, index):
        if index == 0:
            self.prepend(data)
        
        if index > 0 and index <= self.size():
            pos = 0
            current = self.head
            while pos != index -1:
                current = current.next_node
                pos += 1
            
            prev_node = current
            next_node = prev_node.next_node

            new_node = Node(data)

            prev_node.next_node = new_node
            new_node.next_node = next_node
    
    def delete(self, data):
        prev_node = self.head
        current = prev_node

        while current and current.data is not data:
            prev_node = current
            current = current.next_node

        if current:
            prev_node.next_node = current.next_node

            if current is self.head:
                self.head = self.head.next_node
        
        return current
    
    def nodeAtIndex(self, index):
        if index == 0:
            return self.head
        
        if index > 0 and index < self.size():
            pos = index
            current = self.head
            while pos > 0:
                current = current.next_node
                pos -= 1
            return current
        
    def deleteAtIndex(self, index):
        current = self.head
        if index == 0:
            self.head = current.next_node
            return current
        
        if index > 0 and index < self.size():
            pos = index
            while pos > 1:
                pos -= 1
                current = current.next_node

            deletedNode = current.next_node
            current.next_node = current.next_node.next_node
            
            return deletedNode       

    def __repr__(self):
        current = self.head
        nodes = []

        while current:
            if current == self.head:
                nodes.append("Head: [%s]" % current.data)
            elif current.next_node == None:
                nodes.append("[%s] : Tail" % current.data)
            else: 
                nodes.append("[%s] " % current.data)
            current = current.next_node
        return "-> ".join(nodes)