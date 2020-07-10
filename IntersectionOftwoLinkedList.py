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
    def getintersectionNode(self, headA, headB):
        if not headA and not headB:
            return None
        a,b = headA,headB
        while a !=b:
            if not a:
                a = headB
            else:
                a = a.next
            if not b:
                b = headA
            else:
                b = b.next
        return b
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.push(12)
#llist.printList()
print(llist.getintersectionNode(headA, headB)