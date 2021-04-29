class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = -1
        max = 0
        d = {}
        #search through string
        for i in range(len(s)):
            # check if in d and not duplicate
            # d[s[i]] key
            # s[i] abc
            # i moving pointer
            if s[i] in d and d[s[i]] > start:
                start = d[s[i]]
                d[s[i]] = i
            else:
                d[s[i]] = i
                if i - start > max:
                    max = i - start
        return max
        #https://www.youtube.com/watch?v=tTHtBfakHIw
        #https://www.youtube.com/watch?v=COVvQ9I7XyI
