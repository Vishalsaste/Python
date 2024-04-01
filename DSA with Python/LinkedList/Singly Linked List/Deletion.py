class Node:
    #Initialize a node with the given data.
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList :
    #Initialize an empty linked list.
    def __init__(self):
        self.head = None

    #Print the elements of the linked list in order.
    def print_LL(self):
        if self.head is None:
            print("LL is empty")
        else:
            n =self.head
            while n is not None:
                print(n.data, "--->" , end=" ")
                n = n.ref

    #Insert a node to the beginning of the linked list.
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    #Delete a node to the beginning of the linked list.
    def delete_begin(self):
        if self.head is None:
            print("LL is empty i cant delete this node")
        else:
            self.head = self.head.ref

     #delete a node to the end of the linked list.
    def delete_end(self):
        if self.head is None:
            print("LL is empty i cant delete this node")
        elif self.head.ref is None:
            self.head = None
        else:
            n =self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    #delete a node to the middle / by value of the linked list.  
    def delete_by_value(self,x):
        if self.head is None:
            print("LL is empty i cant delete this node")
            return
        if x== self.head.data :
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x==n.ref.data :
                break
            n = n.ref
        if n.ref is None:
            print("node is not Found in LL")
        else:
            n.ref = n.ref.ref

#Call the function
#run the functions separately with commenting other below functions         
LL1 = LinkedList()
LL1.add_begin(30)
LL1.add_begin(40)
LL1.add_begin(50)
#LL1.delete_begin()
#LL1.delete_end()
LL1.delete_by_value(30)
LL1.print_LL()
