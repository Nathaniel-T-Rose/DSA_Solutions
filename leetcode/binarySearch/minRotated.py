def findMin(self, nums: List[int]) -> int:
        end=len(nums)-1
        start=0
        minimum=nums[end]
        while start<end:
            k=(start+end)//2
            if nums[k+1]<nums[k] or nums[k]>minimum:
                start=k+1
            else:
                end=k
                minimum=nums[k]
        return minimum