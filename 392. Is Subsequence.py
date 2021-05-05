class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        q = list(s)
        for c in t:
            if not q: return True
            if c == q[0]:
                q.pop(0)
        return not q
    #O(n)
    #https://maxming0.github.io/2020/06/09/Is-Subsequence/
