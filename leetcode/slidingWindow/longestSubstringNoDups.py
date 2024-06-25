def lengthOfLongestSubstring(self, s):
        substrSet = set()
        maxLen = 0
        start=0
        for i in range(len(s)):
            #remove letters from charset and advance start of substring until dup removed
            while s[i] in substrSet:
                substrSet.remove(s[start])
                start+=1
            #add current letter to substring
            substrSet.add(s[i])
            #update maxLen with current substring
            maxLen=max(maxLen,i-start+1)
            print(start,maxLen)
        return maxLen

#Approach: for each char, assess if char already in subset
# if it is, we don't know where exactly it occurs since sets
# are unordered. Because of that, we'll remove the character
# at the substring start index counter, then advance it to the
# next index. If this removes the duplicate, we're finished,
# otherwise iterate until duplicate removed. 
# then we're golden to add the character we're currently on 
# for the exterior loop to the substring set since no 
# duplicates exist within, and assess the substring length
# against the current max length.
            
                
