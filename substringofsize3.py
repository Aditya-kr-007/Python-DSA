class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        s1=list(s)
        count=0
        for i in range(n-2):
            if s1[i]!=s1[i+1] and s1[i+1]!=s1[i+2] and s1[i]!=s1[i+2]:
                count+=1
        return count
s=input("enter the string: ")
print("the number of good substrings are",Solution().countGoodSubstrings(s))