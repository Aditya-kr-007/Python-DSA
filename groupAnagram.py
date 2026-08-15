from typing import List
class Solution:
    def sortstr(self,s):
        s1=list(s)
        s1.sort()
        return "".join(s1)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for s in strs:    
            key=self.sortstr(s)
            if key in freq:
                freq[key].append(s)
            else:
                freq[key]=[s]
        return list(freq.values())
strs=["eat","tea","tan","bat","ate","tab","ant"]
print(Solution().groupAnagrams(strs))
     
    

        