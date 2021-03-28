class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        def dfs(candidates, temp, remainder, index):
            if remainder ==0:
                self.res.append(temp[:])
                return
            if remainder < 0:
                return
            for i in range(index, len(candidates)):
                temp.append(candidates[i])
                dfs(candidates, temp, remainder - candidates[i], i)
                temp.pop()
        dfs(candidates, [], target, 0)
        return self.res
#https://www.youtube.com/watch?v=HdS5dOaz-mk
