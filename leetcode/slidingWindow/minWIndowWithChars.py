
def minWindow(self, s: str, t: str) -> str:
    start=0
    end=0
    charCounts={char:t.count(char) for char in t}
    results={key:list() for key in charCounts}

    #create list of indices for each required letter
    #take x last indices from index
    #slice from beginning to end

    for i in range(len(s)):
        if s[i] in results:
            results[s[i]].append(i)
            #guaranteed ordered for occurence
    
    fullList=[]
    for key in results:
        #get last n occurences for each character
        fullList+=results[key][len(results[key])-charCounts[key]:]
    if len(fullList)<len(t):
        return ""
    fullList.sort()
    
    return s[fullList[0]:fullList[-1]+1]

# Approach: Need to find the final slice which includes all 
# requisite letters. 
# double dicitonary approach, one associates letter to number of counts needed
# other associates to list of all index occurences
# takes final n indices for each letter, then returns slice from smallest to greatest