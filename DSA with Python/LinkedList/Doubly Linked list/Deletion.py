#Deletion Opration of the doubly linked list

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

    #Print the values of the nodes in the doubly linked list in forward order.
    def print_LL(self):
        print("Forward Traversal")
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
        print("Backward traversal")
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

    #delete the node from the beginning of the list
    def delete_begin(self):
        if self.head is None:
            print("LL is empty so cant delete")
            return
        if self.head.nref is None:
            self.head = None
            print("LL is empty after delete the node")
        else:
            self.head = self.head.nref
            self.head.pref = None

    #delete the node from the end of the list
    def delete_end(self):
        if self.head is None:
            print("LL is empty so cant delete")
            return
        if self.head.nref is None:
            self.head = None
            print("LL is empty after delete the node")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None

    #delete the node by the given value of the list
    def delete_by_value(self,x):
        if self.head is None:
            print("LL is empty so cant delete")
            return
        if self.head.nref is None:
            if x== self.head.data :
                self.head = None
            else:
                print("x is not present in Dll")
            return
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        n = self.head
        while n.nref is not None:
            if x == n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data==x:
                n.pref.nref = None
            else:
                print("x is not present in Dll")

# Call the function
dl1 = doublyLL()
dl1.insert_empty(5)
dl1.add_begin(4)
dl1.add_begin(8)
dl1.add_end(6)
#dl1.delete_begin()
#dl1.delete_end()
dl1.delete_by_value(9)
dl1.print_LL()
dl1.print_LL_reverse()