
class Solution:
    #initial approach, will time out on larger 
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #what do i care about? - distance to next maximum 
        #iterate from end, store index:temp val
        #for each, iterate up through hash vals to find next 

        futureTemps={}
        days=[0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            j=i+1
            found=False
            #search future
            while (j<len(temperatures) and (not found)):
                if futureTemps[j]>temperatures[i]:
                    days[i]=j-i
                    found=True
                j+=1
            #record this for next loop
            futureTemps[i]=temperatures[i]
        return days
    
    #use stack
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0]*len(temperatures)

        #iterate from end
        offset=0
        for i in range(len(temperatures)-1,-1,-1):
            days=0
            offset=0
            curTemp = temperatures[i]
            found=False
            while stack!=[] and not found:
                #print(stack, days, offset)
                # check top of stack
                # if current temp not greater, need to keep in stack for future
                if stack[-1][0]>curTemp:
                    found=True
                else:
                    temp,adj=stack.pop()
                    days+=adj
                    offset+=adj
                    offset+=1
                days+=1
            if not found: #i'm new maximum, reset day offset
                days=0
                offset=0
            stack.append((curTemp,offset))
            answer[i]=days
        return answer
    
