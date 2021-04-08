# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #initial value
        curr = dummy = ListNode(0)
        #recursive condition
        while l1 and l2:
            #compare value and add to curr
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        #if 1 one the list is null
        curr.next = l1 or l2
        #return the full list
        return dummy.next
     #https://www.youtube.com/watch?v=Z7VOBq6S5n8
