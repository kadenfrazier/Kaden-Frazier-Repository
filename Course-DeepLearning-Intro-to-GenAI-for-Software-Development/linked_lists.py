import threading  # Used to make the class thread-safe

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Added for the doubly linked list

class LinkedList:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None  # Reference to the last node
        self.size = 0
        self.max_size = max_size
        self.lock = threading.Lock()

    def append(self, data):
        # Allow any data type to be appended, check length only for strings
        if isinstance(data, str) and len(data) > 1000:
            raise ValueError("Data size exceeds maximum limit")
        with self.lock:
            if self.max_size is not None and self.size >= self.max_size:
                raise ValueError("Linked list is full")
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                self.tail = new_node  # Initialize tail
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node  # Update tail
            self.size += 1

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()  # New line after printing

    def print_list_reverse(self):
        current = self.tail  # Start from the tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()  # New line after printing in reverse
