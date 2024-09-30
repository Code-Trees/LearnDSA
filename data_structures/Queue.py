class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class queue:
    def __init__(self):
        self.head = None
        self.tail = None 
    
    def enqueue(self,data):
        new_element = Node(data)
        if self.head  is None:
            self.head  = new_element
            self.tail = new_element
            return
        self.tail.next = new_element
        self.tail = new_element


    def dequeue(self):
        de = self.head
        self.head = self.head.next
        de.next = None
        de.data = None
            
    def print_q(self):
        p = self.head
        while p is not None:
            print(f"{p.data}",sep = "->")
            p = p.next



q = queue()
q.enqueue(10)
q.enqueue(11)        
q.enqueue(12)
q.enqueue(13)       
q.dequeue()
q.enqueue(14)
q.print_q()

# NO elements are not handled in this code