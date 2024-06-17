def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Use two reads, abc...]n from left, n...cb]a from right  
        # assemble abc...n incrementally from left
        #then fill in remaining parts of product from right
        #O(n) solution
        output=[1]*len(nums)

        prev = 1
        for i in range(len(nums)):
            output[i] *= prev
            prev *= nums[i]

        prev=1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= prev
            prev *= nums[i]
        
        return output

'''
x y z a

azy xza xya xyz

1 x xy xyz prev (4)

azy  az  a 1
'''