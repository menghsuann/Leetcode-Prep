class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        point_a = 0
        point_b = len(numbers) -1
        while point_a < point_b:
            curr_num = numbers[point_a] + numbers[point_b]
            if curr_num == target:
                return [point_a +1, point_b +1]
            if curr_num > target:
                point_b -= 1
            else:
                point_a += 1
        return [-1,-1]
        #https://www.youtube.com/watch?v=QDPD9B9h37k
