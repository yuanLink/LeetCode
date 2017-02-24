class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp_answer = {}
        for i,num in enumerate(nums):
            if target - num in temp_answer:
                return [temp_answer[target-num],i]
            temp_answer[num] = i