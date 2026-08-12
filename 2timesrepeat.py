from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        k=1
        for i in range(2,n):
                if nums[i]!=nums[k-1]:
                    k+=1
                    nums[k]=nums[i]
        return k+1,nums[:k+1]
n=int(input("enter the list size= "))
nums=list(map(int,input().split()))
print(Solution().removeDuplicates(nums))