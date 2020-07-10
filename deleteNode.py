# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end =" ")
            temp = temp.next
    def deleteNode(self,node):
            node.data, node.next= node.next.data , node.next.next
    

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.push(12)
#llist.deleteNode(.data)
llist.deleteNode()
llist.printList()


