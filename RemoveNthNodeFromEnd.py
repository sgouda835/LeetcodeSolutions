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
    
    def NthNodefromEnd(self, n):
        fast = slow = self.head
        count = 0
        
        for i in range(0,n-1):
            fast = fast.next
            count = count + 1
            
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        return slow.data
    
    def removeNthFromEnd(self, n):
        fast = slow = self.head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return self.head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return self.head

    
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.push(12)
llist.printList()
print()
print("The nth Node from the end is: ", llist.NthNodefromEnd(3))
llist.removeNthFromEnd(2)
llist.printList()

