def groupAnagrams(strs):
    
    # Use 'sorted' string as key to all anagrams in dictionary, return list of all anagram lists
    
    stringLsts={}
    for word in strs:
        sortedWord="".join(sorted(word))
        if sortedWord in stringLsts:
            stringLsts[sortedWord]+=[word]
        else:
            stringLsts[sortedWord]=[word]

    return [stringLsts[word] for word in stringLsts]