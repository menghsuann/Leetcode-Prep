class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = ''
        #search through the list
        for i in range(len(s)):
            #scenario a: check if longer than existing p
            len1 = len(self.getlongest(s, i, i))
            if len1 > len(p):
                p = self.getlongest(s, i, i)
            #scenario bb: check if longer than existing p
            len2 = len(self.getlongest(s, i, i+1))
            if len2 > len(p):
                p = self.getlongest(s, i, i+1)
        return p 
    #
    def getlongest(self, s, l, r):
        #if inside the string and L=R, 向左右擴一格, return the longest length
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1 : r]
      #https://www.youtube.com/watch?v=nSFWpXuNfyw
        
