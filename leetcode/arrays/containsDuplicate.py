
#dictionary lookup, create entry if not present. 
def containsDuplicate(self, nums: List[int]) -> bool:
        a={}
        for num in nums:
            if num in a:
                return True
            else:
                a[num]=1
        return False


#sort list, if current matches prev, return true O(n)
def containsDuplicate2(self, nums: List[int]) -> bool:
        nums.sort()
        prev=None
        for num in nums:
            if num==prev:
                return True
            prev=num
        return False