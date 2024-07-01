""" Linked List
"""

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None
    
    def insert(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        
        else:
            ptr = self.head

            while ptr.next != None:
                ptr = ptr.next
            
            ptr.next = node
    
    def deletion(self, val):
        if not self.head:
            return
        
        if self.head.data == val:
            self.head = self.head.next
        
        prev, curr = self.head, self.head.next
        
        while curr:
            if curr.val == val:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next

        return self.head

    def display(self):
        ptr = self.head

        while ptr:
            print(ptr.val)
            ptr = ptr.next
