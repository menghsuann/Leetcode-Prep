class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)
        return sorted(slist) == sorted(tlist)
