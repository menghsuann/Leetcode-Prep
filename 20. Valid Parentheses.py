class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {"(":")", "{":"}", "[":"]"}
        for i in s:
            if i in lookup:
                stack.append(i)
            #adding left p
            elif len(stack)==0 or lookup[stack.pop()] != i:
                return False
            #checking if p is in stack or 左括號有否對應到lookup裡面的右括號
        return len(stack)==0 #有對應到才return true
        #https://www.youtube.com/watch?v=4z5fmKMr9lU
        
