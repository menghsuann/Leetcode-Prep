# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #create dummy(null) to store temp list
        dummy = ListNode(float("inf"))
        #check if head is valid
        while head:
            #recursive
            dummy.next, head.next, head = head, dummy.next, head.next
        #the list after dummy is our desired output
        return dummy.next
  #https://www.youtube.com/watch?v=C6LzmH20GNk
