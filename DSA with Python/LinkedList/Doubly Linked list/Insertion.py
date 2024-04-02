#Insersion Opration of the doubly linked list

#A node class to represent a doubly linked list node.
class Node:
    #Initialize a node with the given data.
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

#A doubly linked list class to represent a linked list of nodes.
class doublyLL:
    #Initialize an empty doubly linked list.
    def __init__(self):
        self.head = None

    #Print the values of the nodes in the doubly linked list in order.
    def print_LL(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->" , end=" ")
                n = n.nref

    #Print the values of the nodes in the doubly linked list in reverse order.
    def print_LL_reverse(self):
        print()
        if self.head is None:
            print("LL is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data, "--->" , end=" ")
                n=n.pref

    #Insert a node with the given data at the beginning of the doubly linked list if it is empty, otherwise print an error message.
    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("LL is not empty")

    #Add a node with the given data at the beginning of the doubly linked list.
    def add_begin(self , data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    #Add a node with the given data at the end of the doubly linked list.
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    #Add a node with the given data after the node with the given data in the doubly linked list.If the node is not found, print an error message.
    def add_after(self, data, x):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("node is not Found in LL")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node

    #Add a node with the given data before the node with the given data in the doubly linked list. If the node is not found, print an error message.
    def add_before(self, data, x):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("node is not Found in LL")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

# Call the function
dl1 = doublyLL()
dl1.insert_empty(5)
dl1.add_begin(4)
dl1.add_begin(8)
dl1.add_end(6)
dl1.add_after(7,4)
dl1.add_before(9,4)
dl1.print_LL()
dl1.print_LL_reverse()



