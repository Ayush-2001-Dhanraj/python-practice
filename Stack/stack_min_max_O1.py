from stack import Stack

class Stack_min_O1(Stack):

    min_element = None

    def __init__(self):
        super().__init__()

    def push(self, element):
        if not self.min_element:
            super().push(element)
            self.min_element = element
        elif element > self.min_element:
            super().push(element)
        else:
            super().push(2 * element - self.min_element)
            self.min_element = element

    def pop(self):
        y = super().pop()
        if y.data > self.min_element:
            return y.data
        min = self.min_element
        self.min_element = 2*self.min_element - y.data
        return min

    def get_min(self):
        return self.min_element
    
class Stack_max_O1(Stack):

    max_element = None

    def __init__(self):
        super().__init__()

    def push(self, element):
        if not self.max_element:
            super().push(element)
            self.max_element = element
        elif element < self.max_element:
            super().push(element)
        else:
            super().push(2 * element - self.max_element)
            self.max_element = element

    def pop(self):
        y = super().pop()
        if y.data < self.max_element:
            return y.data
        min = self.max_element
        self.max_element = 2*self.max_element - y.data
        return min

    def get_max(self):
        return self.max_element

class Stack_min_max_O1(Stack):

    min_element = None
    max_element = None

    def __init__(self):
        super().__init__()

    def push(self, element):
        if not self.top:
            super().push(element)
            self.min_element = element
            self.max_element = element
        elif element > self.min_element:
            if element > self.max_element:
                super().push(2 * element - self.max_element)
                self.max_element = element
            else:
                super().push(element)
        else:
            super().push(2 * element - self.min_element)
            self.min_element = element

    def pop(self):
        if not self.top:
            return
        
        y = super().pop()
        deleted = y.data

        if y.data > self.min_element:
            if y.data > self.max_element:
                deleted = self.max_element
                self.max_element = 2 * self.max_element - y.data
            else:
                deleted = y.data
        else:
            deleted = self.min_element
            self.min_element = 2 * self.min_element - y.data

        if not self.top:
            self.min_element = None
            self.max_element = None
        
        return deleted

    def get_min(self):
        return self.min_element
    
    def get_max(self):
        return self.max_element


# stk = Stack_max_O1()
stk = Stack_min_max_O1()
stk.push(3)
stk.push(5)
stk.push(2)
stk.push(1)
stk.push(1)
stk.push(-1)
stk.push(8)
print(stk)
print("Min:", stk.get_min())
print("Max:", stk.get_max()) 
# print(stk.get_max())
stk.pop()
stk.pop()
stk.pop()
print(stk)
print("Min:", stk.get_min())
print("Max:", stk.get_max()) 
stk.pop()
stk.pop()
stk.pop()
print(stk)
print("Min:", stk.get_min())
print("Max:", stk.get_max()) 
stk.pop()
# stk.pop()
# stk.pop()
# stk.pop()
# print(stk)
# print(stk.get_max())
print(stk)
print("Min:", stk.get_min())
print("Max:", stk.get_max()) 