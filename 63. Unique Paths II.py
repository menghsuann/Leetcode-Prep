class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #exlcude extreme cases
        if not obstacleGrid:
            return 0
        #m = row, n = col
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        #input all grid as 0
        cache = [[0]*n for i in range(m)]
        #set the starting point as 1
        cache[0][0]=1
        #recursive search
        for i in range(m):
            for j in range(n):
                #find the obstacle and make the element 0
                if obstacleGrid[i][j]==1:
                    cache[i][j]=0
                else:
                #calculate the sum of # and excluding first row and first col
                    if i > 0:
                        cache[i][j]+=cache[i-1][j]
                    if j > 0:
                        cache[i][j]+=cache[i][j-1]
        return cache[-1][-1]
     #https://www.bilibili.com/s/video/BV1gz4y1Q7Yu
