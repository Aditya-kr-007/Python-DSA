"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        while n%3==0:
            n=n//3
        if n==1:
            return True
        else :
            return False
n=int(input("enter the number to check= "))
print(Solution().isPowerOfTwo(n))
"""

#RECURSION
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:            #base condition
            return False
        if n==1:             #base condition
            return True
        if n%3!=0:           #base condition
            return False
                             #recursive condition
        return self.isPowerOfTwo(n//3)
        
n=int(input("enter the number to check= "))
print(Solution().isPowerOfTwo(n))