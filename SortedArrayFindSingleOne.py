class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = 0
        # use xor to find ans quicklys
        for each in nums:
            val ^= each
        return val