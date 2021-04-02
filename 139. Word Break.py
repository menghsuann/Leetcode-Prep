class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for w in wordDict:
                l = len(w)
                if dp[i-l] and s[:i].endswith(w):
                    dp[i] = True
        return dp[-1]

#https://www.youtube.com/watch?v=tSbBuiO1rXI
