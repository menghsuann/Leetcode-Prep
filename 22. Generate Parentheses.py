class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s, left, right):
            #ending case: return the result from backtrack
            if len(s) == n * 2:
                res.append(s)
            else:
                #if left is larger than right, add right bracket
                if left > right:
                    backtrack(s + ")", left, right + 1)
                #if left is smaller than n, add left bracket
                if left < n:
                    backtrack(s + "(", left + 1, right)
        #starting case
        backtrack("", 0, 0)
        return res

    #遞歸就是讓各自狀況散出去把result傳回來
    #https://www.youtube.com/watch?v=kXqqiGFlAus
