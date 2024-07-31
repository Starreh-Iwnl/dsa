""" Stacks
"""

class Stack:

    def __init__(self, size):
        self.size = size
        self.stack = []
    
    def __stackSize(self):
        return len(self.stack)

    def __isOverflow(self):
        if self.__stackSize() >= self.size:
            return True
        return False
    
    def __isUnderflow(self):
        if self.__stackSize() <= 0:
            return True
        return False
    
    def push(self, data):
        if not self.__isOverflow():
            self.stack.append(data)
    
    def pop(self):
        if not self.__isUnderflow():
            return self.stack.pop()
    
    def peek(self):
        if not self.__isUnderflow():
            return self.stack[-1]
    
