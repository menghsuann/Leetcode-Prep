class Solution:
    def climbStairs(self, n: int) -> int:
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current
        return current
      #n=1, 1 --> output=1
      #n=2, 1+1, 2 --> output = 2
      #n=3, 1+1+1, 1+2, 2+1 -->output = 3 = (1+2)
      #n=4, 1+1+1+1, 2+2, 1+1+2, 2+1+1, 1+2+1  --> output = 5 = (2+3)
      #n=5, 1+1+1+1+1, 1+1+1+2(4)..., 2+2+1(3)... --> output = 8 = (3+5)
      #n=6, 1+1+1+1+1+1, 2+2+2, 1+1+2+2(6), 1+1+1+1+2(5) --> output = 13 = (5+8)
      #Fibonacci Sequence
    
 #https://www.youtube.com/watch?v=NgamBohlrf8
