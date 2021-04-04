class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # extreme case that the number is not include in + 
        if max(nums) < 0:
            return max(nums)
        #initial condition
        local_max, global_max = 0,0
        #recursive to search max
        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(global_max, local_max)
        return global_max
    
#https://www.youtube.com/watch?v=eQGgk8zwIGI
