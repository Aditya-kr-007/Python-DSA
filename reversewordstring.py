class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        s=s.split()
        s.reverse()
        return " ".join(s)
s=input("enter the String=")
print(Solution().reverseWords(s))
