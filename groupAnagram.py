
def sortstr(s):
        s1=list(s)
        s1.sort()
        return "".join(s1)
def groupAnagrams(strs):
        freq={}
        for s in strs:    
            key=sortstr(s)
            if key in freq:
                freq[key].append(s)
            else:
                freq[key]=[s]
        return list(freq.values())
strs=["eat","tea","tan","bat","ate","tab","ant"]
print(groupAnagrams(strs))
     
    

        