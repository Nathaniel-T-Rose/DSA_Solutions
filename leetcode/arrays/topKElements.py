def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create dict of frequencies
        freqs={}
        for num in nums:
            freqs[num] = freqs.get(num,0) + 1
        # sorted list of item tuples, keys sorted descending by frequency
        sortedKeys = sorted(freqs.items(),key=lambda item: item[1],reverse=True)
        
        # return list of requested k most frequent keys 
        return [sortedKeys[i][0] for i in range(k)]