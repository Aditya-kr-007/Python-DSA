class Solution:
    def firstUniqChar(self, s: str) -> int:
        n=len(s)
        dict1={}
        for i in s:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for i in range(n):
            if dict1[s[i]]==1:
                return i
        
        return -1
s=input("enter your string= ")
print("the unique char index is",Solution().firstUniqChar(s))
