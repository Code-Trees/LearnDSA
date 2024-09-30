
# Node class for doubly linked list
class Node:
    def __init__(self, data=None):
        self.data = data  # The value of the node
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Head points to the first node of the list

    # Method to add a new node at the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty, set head to the new node
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        last.next = new_node  # Set the next of the last node to the new node
        new_node.prev = last  # Set the previous of the new node to the last node

    # Method to add a new node at the beginning of the list
    def prepend(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty, set head to the new node
            self.head = new_node
            return
        new_node.next = self.head  # Point the new node's next to the current head
        self.head.prev = new_node  # Set the current head's prev to the new node
        self.head = new_node  # Update head to the new node

    # Method to print the list in forward direction
    def print_list_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # Method to print the list in backward direction (from the last node)
    def print_list_backward(self):
        current = self.head
        if current is None:  # If the list is empty
            return
        # Traverse to the last node
        while current.next:
            current = current.next
        # Print in reverse order
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# Example usage
if __name__ == "__main__":
    # Create a doubly linked list
    dll = DoublyLinkedList()

    # Append data to the list
    dll.append(10)
    dll.append(20)
    dll.append(30)
    
    # Prepend data to the list
    dll.prepend(5)

    # Print the list forward
    print("Forward traversal:")
    dll.print_list_forward()

    # Print the list backward
    print("Backward traversal:")
    dll.print_list_backward()

