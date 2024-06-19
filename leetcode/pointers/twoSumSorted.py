def twoSum(self, numbers,target):
        i=0
        length=len(numbers)
        seen=[]
        while i<length-1:
            if numbers[i] not in seen:
                addend1=numbers[i]
                j=i+1
                while j<length and numbers[j]<=target-addend1:
                    if addend1+numbers[j]==target:
                        return [i+1,j+1] 
                    j+=1
                seen.append(numbers[i])
            i+=1
        return []