class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, cur_min = 0, float('inf')
        for p in prices:
            res = max(res, p - cur_min)
            cur_min = min(cur_min, p)
        return res
      #O(n)
      #https://maxming0.github.io/2020/09/18/Best-Time-to-Buy-and-Sell-Stock/
