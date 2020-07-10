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
            
    def detectLoop(self):
        fast = slow = self.head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
            if (fast == slow):
                return True
        return False
    
    # def removeLoop(self):
    #     slow = fast= self.head
    #     while slow.next != fast.next:
    #         slow =slow.next
    #         fast = fast.next
    #     fast.next = None
            
            
            
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)
llist.printList()
llist.head.next.next.next.next = llist.head
print(llist.detectLoop())
llist.removeLoop()
llist.printList()

        