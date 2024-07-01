class TimeMap:

    def __init__(self):
        self.map={} # dictionary key -> [timestamp,value] pairs
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #maintain sorted list, because timestamps only increase should be able to always append to end of mapped list
        if key in self.map:
            self.map[key]+=[(timestamp,value)]
        else:
            self.map[key]=[(timestamp,value)]
    def get(self, key: str, timestamp: int) -> str:
        #binary search for insertion point in timestamps, return index-1 if has values but timestamp not there
        
        #check exists
        if key not in self.map:
            return ''
        else:
            pairs=self.map[key]
        #search pairs
        start=0
        end=len(pairs)
        while start<end:
            mid=(start+end)//2
            if pairs[mid][0]>timestamp:
                end=mid
            elif pairs[mid][0]<timestamp:
                start=mid+1
            else:
                return pairs[mid][1]
        #check there is value before target timestamp
        if start==end==0:
            return ''
        return pairs[start-1][1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)