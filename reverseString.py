from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        print("the reverse string is =","".join(s))
s=list(input("enter the string ="))
Solution().reverseString(s)