class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        for i in xrange(1, len(prices)):
            if prices[i-1] < prices[i]:
                res += prices[i] - prices[i-1]
        return res
#https://www.youtube.com/watch?v=bCbg9q3jIrk
