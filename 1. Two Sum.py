class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        #check if difference is in the dict or keep the i
        for i in range(len(nums)):
            if target-nums[i] not in dict:
               dict[nums[i]] = i
            else:
                return [dict[target-nums[i]],i]
              
             # https://www.youtube.com/watch?v=OTtbG8lNNW8
