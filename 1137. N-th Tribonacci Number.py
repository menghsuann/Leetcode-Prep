def printTribRec(n) :
    if (n == 0 or n == 1 or n == 2) :
        return 0
    elif (n == 3) :
        return 1
    else :
        return (printTribRec(n - 1) +
                printTribRec(n - 2) +
                printTribRec(n - 3))
#O(3^N)

def tribonacci(self, n: int) -> int:
        dp = [0,1,1]+[0 for _ in range(3,n+1)]
        for x in range(3,n+1):
            dp[x] = dp[x-1]+dp[x-2]+dp[x-3]
        return dp[n]
#O(n)
#create a dp list
#add previous three values so the current value become to store the current result
#We iterate all dp array, it will cost O(n), each value will add up last two value as result, it will cost (1+3), in total will be O(n+3n) --> O(n)
