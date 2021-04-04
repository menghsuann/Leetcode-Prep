class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #extreme case
        if m == n == 1:
            return 1
        #set up recursion conditions: intialize all col, row to 1
        dp = [[1]*m]*n
        #for loop: sum of left and up; can only move either down or right
        for row in range(1, len(dp)):
            for col in range(1, len(dp[row])):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        #the final right down corner would be our anwser
        return dp[-1][-1]
  #dynamic programming
  #https://www.youtube.com/watch?v=gp_wfYhjALw
