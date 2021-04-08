# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nodes = []
        #returning result
        dummy = ListNode(-1)
        head = dummy
        #1. save all values in nodes by 遍歷給我們的linked list，把值全部存在一個新的list
        for list in lists:
            #avoid list is null
            while list:
                nodes.append(list.val)
                #update pointer
                list = list.next
        #2. sort the new linked list and save to another new list
        for val in sorted(nodes):
            head.next = ListNode(val)#returning a linked list; not only val
            head = head.next #update pointer
        #3. return the new linked list
        return dummy.next
  #https://www.youtube.com/watch?v=YC7jKAr8FJ0
