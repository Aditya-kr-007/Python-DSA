class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        s=s.split() # split the string into a list of words
        s.reverse()
        return " ".join(s)
s=input("enter the String=")
print(Solution().reverseWords(s))
 