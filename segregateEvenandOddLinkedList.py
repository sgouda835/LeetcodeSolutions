# # -*- coding: utf-8 -*-
#
# # -*- coding: utf-8 -*-
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def push(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node
#
#     def printList(self):
#         temp = self.head
#         while(temp):
#             print(temp.data, end =" ")
#             temp = temp.next
#     def oddEvenList():
#         dummy1 = odd = ListNode(0)
#         dummy2 = even = ListNode(0)
#         while head:
#             odd.next = head
#             even.next = head.next
#             odd = odd.next
#             even = even.next
#             head = head.next.next if even else None
#         odd.next = dummy2.next
#         return dummy1.next
#
# llist = LinkedList()
# llist.push(20)
# llist.push(4)
# llist.push(15)
# llist.push(10)
# llist.push(12)
# llist.printList()
