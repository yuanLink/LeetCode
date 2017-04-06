def circularArrayLoop(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if nums == []:
        return False
    for i in range(len(nums)):
        while nums[i] < 0:
            nums[i] += len(nums)
            
        nums[i] = (nums[i] + i)%len(nums)
    
    loop = False
    depth = 0
    # print nums
    """
    monitor a house, and we walk with step
    """
    for i in range(len(nums)):
        index = nums[i]
        if index == -1 :
            continue
        lastStep = index
        while True:
            nextStep = nums[index]
            if nextStep == -1:
                if lastStep == index:
                    break
                else:
                    # print(nums)
                    return True
            lastStep = index
            nums[index] = -1
            index = nextStep
            
        return False

if __name__ == "__main__":
    print(circularArrayLoop([1,3,-1,2,2]))