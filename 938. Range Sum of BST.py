class Solution:
    class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(root):
            if root:
                if low <= root.val <= high:
                    self.res += root.val
                if low < root.val:
                    dfs(root.left)
                if high > root.val:
                    dfs(root.right)
        self.res = 0
        dfs(root)
        return self.res
    #O(n)
    #if root.value with the range, add to result. 
    #if smaller, bfs left nodes. if larger, bfs right nodes.
