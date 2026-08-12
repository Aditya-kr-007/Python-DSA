from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        if len(nums) == 0:
            return 0
        curr_sum=0
        max_sum=nums[0]
        for i in range(n):
            curr_sum=curr_sum+nums[i]
            if curr_sum>max_sum:
                max_sum=curr_sum
            if curr_sum<0:
                curr_sum=0
        return max_sum
n=int(input("enter the list size= "))
nums=list(map(int,input().split()))
print(Solution().maxSubArray(nums))