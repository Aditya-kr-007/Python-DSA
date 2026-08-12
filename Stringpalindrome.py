class Solution:
    def isalphanumeric(self,s):
        x=ord(s)
        if 97<=x<=122 or 65<=x<=90 or 48<=x<=57:
            return True
        else:
            return False
    
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        n=len(s)
        i=0
        j=n-1
        while i<j:
            if not self.isalphanumeric(s[i]):
                i+=1
            elif not self.isalphanumeric(s[j]):
                j-=1
            elif s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True
s=str(input("enter the string= "))
print(Solution().isPalindrome(s))

        