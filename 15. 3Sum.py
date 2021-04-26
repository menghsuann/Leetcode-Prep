class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        #sort first
        nums.sort()
        #last three digit
        for i in range(n-2):
            #if all greater than zero
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            #if the smallest number is too small, cotinue to next indext directly
            if nums[i] + nums[n-2] + nums[n-1] < 0:
                continue
            #if duplicate value
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #兩頭往中間找
            l, r = i+1, n-1
            #交叉後停止
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                #if = 0
                if temp == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    #check if duplicate, update pointer
                    while l+1 < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r-1 and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                #if < 0  
                elif temp < 0:
                    l += 1
                #if > 0
                else:
                    r -= 1
        return result
        
#https://www.youtube.com/watch?v=CW6G30xQCbw
#https://www.youtube.com/watch?v=WOpdLrqzOOw
