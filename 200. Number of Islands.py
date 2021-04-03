class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #extreme case: not a valid grid
        if not grid or not grid[0]:
            return 0
        count = 0
        
        #search process
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    count +=1
                    self.dfs(grid,i,j)
        return count
    
    def dfs(self, grid, i, j):
        #stop condition: out of range / not an island
        if i < 0 or j < 0 or i >=len(grid) or j >=len(grid[0]) or grid[i][j] != '1':
            return
        
        #replace original 1 to avoid repetitive result
        grid[i][j] ='@'

        #recursive steps
        self.dfs(grid, i, j+1)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j-1)
        
        
    #time complexity O(MN)
    #space complexity O(MN)