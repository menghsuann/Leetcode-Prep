class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #temporary number for the whole list: ex. 12
        dp = [amount + 1] * (amount + 1)
        #initial the first value 0
        dp[0] = 0
        #starting from the second value to the last #
        #the number of coin is smaller than the targeted amount
        #sub-problem for every i: what is the minimum way of change
        for i in range(1, amount + 1):
            for j in range(0, len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
                    #the answer = min(the number from previous stage, #-the coin i have +1)
        return -1 if dp[-1] > amount else dp[-1]
      
      #https://www.youtube.com/watch?v=jgiZlGzXMBw
      #https://www.youtube.com/watch?v=6igPE6zlvCY
      
