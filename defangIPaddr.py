class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=""
        for i in address:
          if i!=".":
             ans=ans+i
          else:
             ans=ans+"[.]"
        return ans
"""
        ans= address.replace(".","[.]")
        return ans
"""
address = "192.168.1.1"
print(Solution().defangIPaddr(address))
