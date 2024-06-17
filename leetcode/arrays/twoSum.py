def twoSum(self, nums: List[int], target: int) -> List[int]:
    #track seen values in dictionary, if seen difference between the current value and target, found valid two sum
    vals={}
    for i in range(len(nums)):
        num=nums[i]
        dif=target-num
        if dif in vals:
            return [vals[dif],i]
        vals[num]=i
    return []