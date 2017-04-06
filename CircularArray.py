class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums == []:
            return False
        print nums
        """
        monitor a house, and we walk with step
        """
        for i in range(len(nums)):
            # next step is index
            index = (len(nums) + nums[i] + i)%len(nums)
            # remeber, all walk to self is not allow
            if index == 0 :
                continue
            # if next step is in the same direction with begin
            while nums[index]*nums[i]>0:
                # next step is 
                nextStep = (len(nums) + nums[index] + index)%len(nums)
                # if next step we have walked 
                if nums[nextStep] == 0:
                    return True
                # step this 
                nums[index] = 0
                # go to next
                index = nextStep
        print(nums)
        return False
            
            