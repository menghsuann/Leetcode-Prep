# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #extreme case
        if root is None:
            return True
        #recursive function(add self before function)
        return self.ifSym(root.left, root.right) #start with root(need to define which left, right)
    
    def ifSym(self, left, right):
        #extreme case still true
        if left is None and right is None:
            return True
        #false condition
        if left is None or right is None or left.val != right.val:
            return False
        #recursive function for child(add self before function)
        return self.ifSym(left.left, right.right) and self.ifSym(left.right, right.left)
        
       #https://www.youtube.com/watch?v=ZXi6HLVe4uk
