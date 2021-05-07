class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = 0
        a = abs(x)
        while(a != 0):
            temp = a % 10 #get the unit digit
            num = num * 10 + temp #push num to the left to store unit digit from new temp
            a = int(a / 10)  #divide the original a without unit digit
        if x >= 0 and x == num:
            return True
        else:
            return False
