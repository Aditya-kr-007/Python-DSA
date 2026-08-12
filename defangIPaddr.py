class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = address.replace(".", "[.]")
        return ans


address = "192.168.1.1"
print(Solution().defangIPaddr(address))
