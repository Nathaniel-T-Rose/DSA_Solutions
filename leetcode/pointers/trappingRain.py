def trap(self, height):
        trapped=0
        length=len(height)
        maxLeft=[0]*length
        maxRight=[0]*length
        curMax=0
        for i in range(length):
            if height[i]>curMax:
                curMax=height[i]
            maxLeft[i]=curMax
        curMax=0
        for j in range(length-1,-1,-1):
            if height[j]>curMax:
                curMax=height[j]
            maxRight[j]=curMax
        for k in range(length):
            #if maxLeft[k]>0 and maxRight[k]>0:
            trapped+=min(maxLeft[k],maxRight[k])-height[k]
        return trapped