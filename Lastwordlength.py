class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       s=s.strip() 
       n=len(s)
       i=-1
       while i>=-1*n and s[i]!=" ": # loop is running from last index to first index of string and checking the last word length
            i=i-1
       i=i+1 # to get the last word length we are adding 1 to the index of space
       i=i*-1  # to convert the negative index to positive index
       return i 
s=input("enter the sentence= ")
print(Solution(). lengthOfLastWord(s))