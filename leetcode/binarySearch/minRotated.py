class Solution:
    def findMin(self, nums: List[int]) -> int:
        end=len(nums)-1
        start=0
        while start!=end:
            k=(start+end)//2
            print(k,start,end)
            if nums[k+1]<nums[k]:
                start=k+1
            else:
                end=k
        return nums[start]

#currently failing on min on edge