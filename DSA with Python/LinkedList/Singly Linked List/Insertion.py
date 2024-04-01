'''INSERTION METHOD IN SINGLY LINKED LIST
    there are three method 
    1- at beginning 
    2- at end 
    3- in between (before and after the node )
    and while LL is empty'''

# A node class to represent a single node in a linked list.
# Define a node Class
class Node:
    # Initialize a node with the given data.
    def __init__(self, data):
        self.data = data
        self.ref = None

# A linked list class to represent a singly linked list.
# Define a Linked list
class LinkedList :
    # Initialize an empty linked list.
    def __init__(self):
        self.head = None

# Print the elements of the linked list in order.
    def print_LL(self):
        if self.head is None:
            print("LL is empty")
        else:
            n =self.head
            while n is not None:
                print(n.data, "--->" , end=" ")
                n = n.ref
    
# Add a node to the beginning of the linked list.
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

# Add a node to the end of the linked list.
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
        else :
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

# Add a node after the node with the given data.
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is  None:
            print("node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

# Add a node before the node with the given data.
    def add_before(self,data,x):
        if self.head is None:
            print("LL is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data == x:
               break
            n = n.ref
        if n.ref is None:
                print("node is not Found in LL")
        else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node
        
# Insert a node at an empty position in the linked list.
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("LL is not Empty")

# Call the function
# run the functions separately with commenting other below functions
LL1 = LinkedList()
LL1.add_begin(20)
LL1.add_end(50)
LL1.add_begin(10)
LL1.add_after(30,20)
LL1.add_before(40,50)
LL1.insert_empty(60)
LL1.print_LL()