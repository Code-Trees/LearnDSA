class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self,element):
        new_element = Node(element)
        new_element.next = self.head
        self.head = new_element
        
    def pop(self):
        p = self.head
        self.head = self.head.next
        p.next = None
        p.data = None
        
        
a = Stack()
a.push(10)
a.push(11)
a.push(12)
a.push(13)
a.pop()
a.pop()
