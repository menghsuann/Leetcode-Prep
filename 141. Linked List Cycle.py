# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        #iniital condition
        fast, slow = head, head
        #stopping condition
        while fast and fast.next:
            #changing pointer
            fast, slow = fast.next.next, slow.next
            #matching condition
            if fast == slow:
                return True
        return False
    
    #https://www.youtube.com/watch?v=9SD2ccDW5CY
    #https://www.youtube.com/watch?v=6xdqa_8xgls
