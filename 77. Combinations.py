class Solution:
    def backtrack(self, res, n, nums, k, current):
        if len(current) == k:
            res.append(current.copy())
        else:
            for i in range(nums, n+1):
                current.append(i)
                self.backtrack(res, n, i+1, k, current)
                current.pop()
                
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtrack(res, n, 1, k, [])
        return res
