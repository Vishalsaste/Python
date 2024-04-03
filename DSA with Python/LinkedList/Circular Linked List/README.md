
# Circular Linkedlist

The circular linked list is a linked list where all nodes are connected to form a circle. In a circular linked list, the first node and the last node are connected to each other which forms a circle. There is no NULL at the end. 

## There are generally two types of circular linked lists:

### 1 - Circular singly linked list
In a circular Singly linked list, the last node of the list contains a pointer to the first node of the list. We traverse the circular singly linked list until we reach the same node where we started. The circular singly linked list has no beginning or end. No null value is present in the next part of any of the nodes.

### 2 - Circular Doubly linked list
Circular Doubly Linked List has properties of both doubly linked list and circular linked list in which two consecutive elements are linked or connected by the previous and next pointer and the last node points to the first node by the next pointer and also the first node points to the last node by the previous pointer.


### Operations - 
     
- insertion
- deletion


#### 1 - insertion

     Add / insert element in Circular Linkedlist

     - Insertion at the beginning of the list
     - Insertion at the end of the list
     - Insertion in between the nodes

#### 2 - deletion

     Delete / remove element in Circular Linkedlist

     - Delete the node only if it is the only node in the circular linked list
     - Deletion of the last node
     - Delete any node from the circular linked list: We will be given a node and our task is to delete that node from the circular linked list
